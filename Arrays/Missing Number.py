# Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

# Input: nums = [0,1]

# Output: 2

# Explanation:

# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]

# Output: 8

# Explanation:

# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Method 1: Brute Force: O(N*N) -> compare each element of the list with (n-ith) element value, and check whether it is present or not.

        # Method 2: Hashing
        # freq = {}
        # result = -1
        # n = len(nums)

        # for num in nums:
        #     freq[num] = True
        
        # for i in range(0,n+1):
        #     if i not in freq:
        #         result = i
        #         break
        #     else:
        #         continue
            
        # return result

        # Method 3: Check the difference of (sum of first n numbers) and (sum of the elements present) in the array.

        # n = len(nums)

        # sum_first_n = (n)*(n+1)//2
        # sum_array = sum(nums)

        # return sum_first_n - sum_array

        # Method 4: Check the XOR of (XOR of first n numbers) and (XOR of the elements present) in the array.

        n = len(nums)
        
        xor_first_n = 0
        xor_array = 0

        for i in range(0,n+1):
            xor_first_n ^= i
            if i < n:
                xor_array ^= nums[i]
            else:
                continue
        
        return xor_first_n ^ xor_array   