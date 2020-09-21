import os, math, sys

# swap two elements in an array
def swap(i, j, arr):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp


# This function takes last element as pivot,
# places the pivot element at its correct position in sorted array,
# and places all smaller (than pivot) to its left and all greater elements to its right
def partition (arr, low, high):
  pivot = arr[high]
  i = low - 1

  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      swap(i, j, arr)

  swap(i + 1, high, arr)
  return (i + 1)


# # This function takes middle element as pivot,
# # places all smaller than pivot to its left and all greater elements to its right
# def partition (arr, low, high):
#   pivot = arr[(low + high) // 2]
#   i = low
#   j = high
#   while i <= j:
#     while arr[i] < pivot:
#       i += 1
#     while arr[j] > pivot:
#       j -= 1
#     if i <= j:
#       swap(i, j, arr)
#       i += 1
#       j -= 1
#   return i


def quickSort(arr, low, high):
  if low >= high:
    return

  # pivot is partitioning index
  pivot = partition(arr, low, high)

  quickSort(arr, low, pivot - 1) # LHS
  quickSort(arr, pivot + 1, high) # RHS


if __name__ == "__main__":
  a = [1, 5, 4, 6, 88, 2, 34, 56]
  quickSort(a, 0, len(a) - 1)
  print(a)
