/*
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

*/





class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        int size = nums.size();

        /* Method 1: Brute Force   TC: O(n*n) 

        for(int i=0;i<size;i++)
        {
            for(int j=i+1;j<size;j++)
            {
                if(nums[i]+nums[j] == target)
                {
                        return {i,j};
                }
            }
        }

        return {};
        */
      
        /* Method 2: Hashing with 2 loops
        // TC: O(n*n) SC: O(1)

        unordered_map<int,int> hash;

        for(int i=0;i<size;i++)
        {
            hash[nums[i]] = i;
        }

        for(int i=0;i<size;i++)
        {
            int diff = target - nums[i];
            
            // Check if the difference is present in the array or not, if present its index is different than i or not.
            if(hash.find(diff) != hash.end() and hash[diff] != i)
            {
                return {i,hash[diff]};
            }
        }
        return {};

        */

        /* Hashing with one loop
        unordered_map<int,int> hash;

        for(int i=0;i<size;i++)
        {
            int diff = target - nums[i];
            
            // Check if the difference is present in the array or not, if present its index is different than i or not.
            if(hash.find(diff) != hash.end() and hash[diff] != i)
            {
                return {i,hash[diff]};
            }
            hash[nums[i]] = i;
        }
        return {};
        
        */


        /* Two Pointers*/

        int left = 0;
        int right = size - 1;

        sort(nums.begin(),nums.end());

        while(left<right)
        {
            if(nums[left] + nums[right] > target) right--;
            else if(nums[left] + nums[right] < target) left++;
            else return {left,right}; 
        }

        return {};
    }
};
