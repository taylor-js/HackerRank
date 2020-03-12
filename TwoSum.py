def TwoSum(nums, target):
    dictionary = {}
    for i, num in enumerate(nums):
        n = target - num # subtract the target from each value in the nums array
        if n not in dictionary:
            dictionary[num] = i
        else:
            return [dictionary[n], i]
            
arr = [1,3,4,5,6]
print(TwoSum(arr,5))
