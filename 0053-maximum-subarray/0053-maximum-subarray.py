class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums == None:
            return 0

        maxsofar = nums[0]
        currentsum= nums[0]

        for i in range(1, len(nums)):
            currentsum = max(nums[i], currentsum+nums[i])

            maxsofar = max(maxsofar, currentsum)

        return maxsofar
            