def make_squares(arr):
    
    n = len(arr)
    square = [0 for i in range(n)]
    left, right = 0, n - 1
    highestIndex = n - 1

    while left <= right:
        if arr[left]**2 > arr[right]**2:
            square[highestIndex] = arr[left]**2
            left += 1
        else:
            square[highestIndex] = arr[right]**2
            right -=1
        highestIndex -= 1
    
    return square


    
def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()

# Time: O(n) Need loop through entire array once
# Space: O(n) Need n length output array
# Have two pointers at the beginning and end of the input array. append the greater number squared into an output array starting from the right.