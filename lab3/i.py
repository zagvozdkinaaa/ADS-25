n = int(input())
nums = list(map(int, input().split()))
x = int(input())

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right)//2
        if x == nums[mid]:
            return 'Yes'
        elif x < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return 'No'

print(binary_search(nums, x))