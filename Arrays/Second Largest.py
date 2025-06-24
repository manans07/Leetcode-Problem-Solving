# GFG
# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
# Input: arr[] = [10, 10, 10]   
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.


from heapq import heapify,heappush,heappop

class Solution:
    def getSecondLargest(self, arr2):
        # Code Here
        # Method 1: Sorting -> Set -> Return second last element
        # set_list = list(sorted(set(arr2)))
        # return set_list[-2] if len(set_list)>=2 else -1
        
        
        # Method 2: Heap
        # set_list = list(set([-num for num in arr2]))
        # heapify(set_list)
        
        # if len(set_list) > 1:
        #     result = -heappop(set_list)
        #     result = -heappop(set_list)
        # else:
        #     result = -1

        # Method 3: Maintain Two Variables : Optimal Solution

                # Method 3
        
        if len(arr2) < 2:
            return -1
            
        else:
            arr = list(set(arr2))
            result = -1
            largest = float('-inf')
            second_largest = float('-inf')
            
            for num in arr:
                if num > largest:
                    second_largest = largest
                    largest = num
                elif num > second_largest and num != largest:
                    second_largest = num
            
            result = second_largest if second_largest != float('-inf') else -1    
            
            return result