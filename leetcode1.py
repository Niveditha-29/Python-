def twoSum(nums, target):
    d = {}  
    for i, num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff], i]
        d[num] = i
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))      
