class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen_numbers = {}

       for i in range(len(nums)):
            current_num = nums[i]
            compliment = target - current_num

            if compliment in seen_numbers:
                return[seen_numbers[compliment], i]
            seen_numbers[current_num] = i
       return[]     

