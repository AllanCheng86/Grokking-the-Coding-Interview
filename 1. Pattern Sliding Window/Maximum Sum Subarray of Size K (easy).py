def max_sub_array_of_size_k(k, arr):
    maxSum = 0
    window_start = 0
    window_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if(window_end >= k - 1):
            maxSum = max(window_sum, maxSum)
            window_sum -= arr[window_start]
            window_start += 1
    return maxSum

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))
main()

        
# Time: O(n)
# Space: O(1)
