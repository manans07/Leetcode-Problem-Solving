# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute Force: Use extra space
        # n = len(nums)
        # k = k%n
        # temp = [0] * n

        # for i in range(0,n):
        #     temp[(i+k)%n] = nums[i]

        # for i in range(0,n):
        #     nums[i] = temp[i]

        # return nums
        # Method 2: Divide the array from k%size, and swap the subarrays
        # k = k%(len(nums))
        # if k!=0:
        #     nums[:k],nums[k:] = nums[-k:],nums[:-k]
        # return nums

        # Method 3: Reverse the whole array once, then reverse the subarrays from k
        k = k%(len(nums))

        def reverse(left,right,nums):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
 
        reverse(0,len(nums)-1,nums)
        reverse(0,k-1,nums)
        reverse(k,len(nums)-1,nums)

        return nums
