from configparser import MAX_INTERPOLATION_DEPTH
import math

def smallest_subarray_sum(s, arr):
    min_length = math.inf
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
      window_sum += arr[window_end]
      while window_sum >= s:
         min_length = min((window_end - window_start + 1),  min_length)
         window_sum -= arr[window_start]
         window_start += 1
    return min_length  
      

# 7, [2, 1, 5, 2, 3, 2]
# output : 2
# window sum = 0
# window_start = 0
# min_length = inf

# First add each element until window_sum >= 7. Record the length of the array. and then contract the array and check if 
# window_sum is still >= 7. If so record the length the array and contract again until it is no longer >= 7. Expand the array and
# check if >= 7


def main():
  print("Smallest subarray length: " 
     + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " 
     + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " 
     + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))


main()