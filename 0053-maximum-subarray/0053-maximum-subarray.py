class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 0 or nums == None:
        #     return 0

        currentsum= 0
        maxsofar = nums[0]
        

        # for i in range(1, len(nums)):
        #     currentsum = max(nums[i], currentsum+nums[i])

        #     maxsofar = max(maxsofar, currentsum)

        # return maxsofar


        for num in nums:
            currentsum = currentsum + num
        
            if currentsum > maxsofar:
                maxsofar = currentsum

            if currentsum < 0:
                currentsum = 0

        return maxsofar
            