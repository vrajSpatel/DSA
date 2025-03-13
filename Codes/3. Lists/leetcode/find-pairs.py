def findpairs(num_list,target):
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if num_list[j] == target-num_list[i]:
                print(f'{i} and {j}')

list1 = [0,1,3,4,0]
findpairs(list1,4)

'''

def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
 
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")
'''