class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nzero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nzero], nums[i] = nums[i], nums[nzero]
                nzero += 1

            
    


        