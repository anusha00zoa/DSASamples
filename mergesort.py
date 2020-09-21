import os, sys

def merge(arr, start, end):
  temp_index = 0
  size = end - start + 1
  temp_arr = [0] * size

  # sort both halves with element by element comparison
  i = start
  mid = (start + end) // 2
  j = mid + 1
  while i <= mid and j <= end:
    if arr[i] < arr[j]:
      temp_arr[temp_index] = arr[i]
      i += 1
    else:
      temp_arr[temp_index] = arr[j]
      j += 1
    temp_index += 1

  # copy any leftovers from both halves
  for x in range(i, mid+1):
    temp_arr[temp_index] = arr[x]
    temp_index += 1

  for x in range(j, end+1):
    temp_arr[temp_index] = arr[x]
    temp_index += 1

  # copy sorted array to actual arr
  j = 0
  for i in range(start, end + 1):
    arr[i] = temp_arr[j]
    j += 1



def mergeSort(arr, start, end):
  if start >= end:
    return

  mid = (start + end) // 2
  mergeSort(arr, start, mid)
  mergeSort(arr, mid + 1, end)
  merge(arr, start, end)


if __name__ == "__main__":
  arr = [12, 11, 13, 5, 6, 7, 77, 23, 99, 1]
  mergeSort(arr, 0, len(arr) - 1)
  print(arr)
