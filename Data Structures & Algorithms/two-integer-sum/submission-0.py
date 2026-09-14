class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in nums that add up to target.
        Returns their indices as a list.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(n) - hash map stores up to n elements
        """
        # Dictionary to store number -> index mapping
        num_map = {}
        
        # Iterate through the array with index
        for i, num in enumerate(nums):
            complement = target - num
            
            # If complement exists in map, we found our solution
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, store the current number with its index
            num_map[num] = i
        
        # According to problem constraints, we'll always find a solution
        return []