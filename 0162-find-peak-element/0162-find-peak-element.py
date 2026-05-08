class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # Scan left to right
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
                
        # If no downward step is found, the last element is the peak
        return len(nums) - 1
        