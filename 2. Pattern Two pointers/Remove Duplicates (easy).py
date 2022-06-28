def remove_duplicates(arr):
    nextNonDuplicate = 1

    next = 0
    while next < len(arr):
        if arr[nextNonDuplicate - 1] != arr[next]:
            arr[nextNonDuplicate] = arr[next]
            nextNonDuplicate += 1
        next += 1

    return nextNonDuplicate

next = 2

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()

# Time: O(n)
# Space: O(1)
