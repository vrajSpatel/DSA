'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
 element is distinct.
'''

def contains_duplicate(nums):
    seen = set(nums)
    if len(seen) < len(nums):
        return 'true'
nums = [1, 2, 3, 1]
print(contains_duplicate(nums))