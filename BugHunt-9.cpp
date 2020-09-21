// v0.4 10/26/2016

//
// Users have reported that there are several issues in this fictional but
// terrifyingly life-like system that wraps some of the functionality of
// a third party library.  It was refactored a while ago corresponding to the
// v3.0 drop from the vendor but wasn't ever fully tested.  Frequent issues
// including crashes are being reported by users now that the system is being
// exercised.
//
// Your task is to identify the broken pieces, explain why they're wrong, and
// suggest or implement one or more fixes to solve those issues.
//

#include <list>

//
// note:  functions beginning with frob_ are the external third party library
// (the frob library).  There is no external documentation.
//

enum FrobulizeType {
	FrobType_Fast=0,
	FrobType_Smooth,
	FrobType_Cubic,
	FrobType_Realistic
};

// Return the number of raw bytes contained in this buffer.  Negative values
// indicate error conditions.
int frob_GetBufferBytes(FrobBuffer *frob);

// Retrieve the raw Frob data from the specified buffer and write it to dst.
// The destination buffer must have the correct number of bytes to hold the
// Frob data as returned by frob_GetBufferBytes.  Returns -1 if the Frob
// buffer is malformed, 0 if the supplied destination buffer was invalid, and
// 1 if the data was written to the destination correctly.
int frob_GetBufferData(FrobBuffer *frob, byte *dst);

// Frobulize the specified buffer (see manual for details).  Returns -1 if
// the Frob buffer is malformed or the parameter combination is invalid and
// returns > 0 if the Frobulization completed successfully.  This function is
// deprecated in v3.0 and higher.
int frob_Frobulize(FrobBuffer *frob, bool goFast, float frobFreq);

// Frobulize the specified buffer (see manual for details).  Return < 0 if
// the Frob buffer is malformed, and > 0 if Frobulization completed
// successfully.  The frob_Frobulize2 is intended to replace the older
// frob_Frobulize from v2.14.  The frob_Frobulize function will be removed
// in a future release.
int frob_Frobulize2(FrobBuffer *frob, FrobulizeType frobType);

// Re-initialize the data in the specified buffer. Return > 0 if the data was
// cleared successfully and -1 if the buffer is malformed.  This effectively
// clears all the working data from the specified buffer.
int frob_ClearData(FrobBuffer *frob);

// Retrieve the ID from this buffer or -1 if buffer is malformed.  IDs are
// guaranteed to be unique.
int frob_GetBufferId(FrobBuffer *frob);

// Retire this frob from active use.  This will cleanup any resources
// associated with the specified buffer.  Returns > 0 if successful and
// -1 on failure.  This is a new requirement for v3.0 and higher.
int frob_RetireFrob(FrobBuffer *frob);

//
// Our code starts here.  FrobManager definition has been pasted below
// for brevity.
//

#include "SystemX.h"

// Our flags for buffer processing.
#define PROCOPT_NONE			0x0
#define PROCOPT_CLEAR			0x1
#define PROCOPT_FROBULIZE		0x2
#define PROCOPT_DEFRANGELATE	0x4

#define VERY_SMALL_EPSILON		0.000001f

#define DEFAULT_CHANNEL			0
#define DEFAULT_PROCESSFLAGS	PROCOPT_FROBULIZE

// Our manager class for frobs.
class FrobManager
{
	public:
		~FrobManager();
		void UpdateFrobs(float deltaTime);

		void AddIdToUpdateList(int id); // IDs are from frob_GetBufferId.
		void AddIdToNetworkList(int id);
		byte *ProcessBuffer(int channel, FrobBuffer *frob, int processFlags);
		byte *ProcessBufferForNetwork(int channel, FrobBuffer *frob, int processFlags);
		void AddFrob(FrobBuffer *frob);
		void RemoveFrob(FrobBuffer *frob);

	private:
		void AddToList(FrobBuffer *frob);
		void RemoveFromList(FrobBuffer *frob);
		FrobBuffer *GetFrobById(int id);

		std::list<FrobBuffer*>	m_frobs;
		std::list<int>			m_updateFrobs;
		std::list<int>			m_updateNetwork;
};

FrobManager::~FrobManager()
{
	for (std::list<FrobBuffer*>::iterator it=m_frobs.begin(); m_frobs.end()!=it; ++it)
	{
		delete (*it);
	}
}

void FrobManager::UpdateFrobs(float deltaTime)
{
	if (deltaTime < VERY_SMALL_EPSILON)
	{
		// updates smaller than this aren't useful (but we get a lot of them)
		return;
	}

	// process all frobs and hand off data to system X.
	for (std::list<int>::iterator it=m_updateFrobs.begin(); m_updateFrobs.end()!=it; ++it)
	{
		FrobBuffer *frob = GetFrobById(*it);
		if (frob)
		{
			byte *frobData = ProcessBuffer(DEFAULT_CHANNEL, frob, DEFAULT_PROCESSFLAGS);
			SystemX::Get()->PostProcessFrob(frob, frobData);
		}
	}

	// process network frobs
	for (std::list<int>::iterator it=m_updateNetwork.begin(); m_updateNetwork.end()!=it; ++it)
	{
		FrobBuffer *frob = GetFrobById(*it);
		if (frob)
		{
			byte *frobData = ProcessBufferForNetwork(DEFAULT_CHANNEL, frob, DEFAULT_PROCESSFLAGS);
			NetworkFrobManager::Get()->PostProcessFrob(frob, frobData);
		}
	}
}

void FrobManager::AddIdToUpdateList(int id)
{
	m_updateFrobs.push_back(id);
}

void FrobManager::AddIdToNetworkList(int id)
{
	// old code did both.  still needed?
	m_updateFrobs.push_back(id);
	m_updateNetwork.push_back(id);
}

byte *FrobManager::ProcessBuffer(int channel, FrobBuffer *frob, int processFlags)
{
	byte *bufferData;

	if (processFlags & PROCOPT_FROBULIZE)
	{
		// call into FrobCo's thing to do...something
		int retVal = frob_Frobulize(frob, false, 10.0f);
		if (retVal = 0 || retVal < 0)
		{
			return nullptr;
		}
	}

	if (processFlags & PROCOPT_CLEAR)
	{
		frob_ClearData(frob);
	}

	if (processFlags & PROCOPT_DEFRANGELATE)
	{
		// no longer supported
		return bufferData;
	}

	int byteCount = frob_GetBufferBytes(frob);
	bufferData = MALLOC(byteCount);
	memset(bufferData, 0, sizeof(bufferData));
	frob_GetBufferData(frob, bufferData);

	if (0 == bufferData[0])
	{
		// ignore bad frob data.
		return nullptr;
	}

	return bufferData;
}

// network specific frob processing.
byte *FrobManager::ProcessBufferForNetwork(int channel, FrobBuffer *frob, int processFlags)
{
	byte *bufferData;

	// fixme:  might need to handle other flags in here.

	if (processFlags & PROCOPT_FROBULIZE)
	{
		// call into FrobCo's thing to do...something
		int retVal = frob_Frobulize2(frob, FrobType_Fast);
		if (retVal = 0 || retVal < 0)
		{
			return nullptr;
		}
	}

	int byteCount = frob_GetBufferBytes(frob);
	bufferData = MALLOC(byteCount);
	memset(bufferData, 0, sizeof(bufferData));
	frob_GetBufferData(frob, bufferData);
	return bufferData;
}

void FrobManager::AddFrob(FrobBuffer *frob)
{
	m_frobs.push_back(frob);
}

void FrobManager::RemoveFrob(FrobBuffer *frob)
{
	RemoveFromList(frob);
}

void FrobManager::RemoveFromList(FrobBuffer *frob)
{
	for (std::list<FrobBuffer*>::iterator it=m_frobs.begin(); m_frobs.end()!=it; ++it)
	{
		if ((*it)==frob)
		{
			m_frobs.erase(it);
			return;
		}
	}
}

FrobBuffer *FrobManager::GetFrobById(int id)
{
	for (std::list<FrobBuffer*>::iterator it=m_frobs.begin(); m_frobs.end()!=it; ++it)
	{
		int itId = frob_GetBufferId(*it);
		if (itId && id == itId)
		{
			return *it;
		}
	}
	return nullptr;
}
