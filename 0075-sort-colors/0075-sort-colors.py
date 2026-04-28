class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start = 0
        end = len(nums)-1
        switch = 0
       
        while switch <= end:
            if nums[switch] == 0:
                nums[start], nums[switch] = nums[switch], nums[start]
                start +=1
                switch +=1
            elif nums[switch] == 1:
                switch +=1
            else:
                nums[switch], nums[end] = nums[end], nums[switch]
                end -= 1


        