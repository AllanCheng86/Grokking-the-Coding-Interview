def pair_with_targetsum(arr, target_sum):
    # left, right = 0, len(arr)-1

    # while left < right:
    #     current_sum = arr[left] + arr[right]
    #     if current_sum == target_sum:
    #         return [left,right]
    #     elif current_sum > target_sum:
    #         right -= 1
    #     else:
    #         left += 1
# Time: O(n)
# space: O(1)
# Use a left and right pointer. check if the number pointed by the two pointers is equal to target. if greater than target, decrement right pointer. if less than target, increase left pointer
# This doesn't always work and a hashtable is the more optimal solution. [2,6,7]

    dict = {}
    for i in range(len(arr)):
        currentNum = arr[i]
        if (target_sum - currentNum) in dict:
            return [dict.get(target_sum-currentNum), i]
        else:
            dict[currentNum] = i

    return [-1,-1]

def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()

# Time: O(n)
# space: O(n)

#Uses a HashMap. Iterate through the loop, for every iteration, check if target - currentNumber is in the hashMap, if so return 
# the index and current index. if not, add currentNumber and current Index as key value pairs into the hashMap