class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Method 1: Using temporary array
        # n = len(nums)
        # temp_array = [0]*n
        # index = 0

        # for i in range(0,n):
        #     if nums[i] != 0:
        #         temp_array[index] = nums[i]
        #         index+=1
        #     else:
        #         continue 
        # for i in range(0,n):
        #          nums[i] = temp_array[i] 

        # return nums
        
        # Method 2: Two Pointers
        
        left = 0
        right = 0
        n = len(nums)

        for i in range(0,n):
            if nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left+=1
                right+=1
            else:
                right += 1
        
        return nums