# bin search iterative
def binary_search(nums, target):
    (left, right) = (0, len(nums) - 1)
    while left <= right:
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle
        elif target < nums[middle]:
            right = middle -1
        else:
            left = middle + 1
    return -1

#recursive search
def recursive_reserch(nums, left, right, target):
    if left > right:
        return -1
    middle = (left + right) // 2

    if target == nums[middle]:
        return middle
    elif target < nums[middle]:
        return recursive_reserch(nums, left, middle - 1, target)
    else:
        return recursive_reserch(nums, middle + 1, right, target)

print('Enter your values')
values = sorted([int(it) for it in input().split()])
print (values)
print('Enter your target')
target = int(input())
print('Enter the way you want to find target: iterative or recursive way')
way = input()
if way == 'iterative':
    index = binary_search(values, target)
    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')
elif way == 'recursive':
    index = recursive_reserch(values,0, len(values) - 1, target)
    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')
else:
    print('Invalid command')
