class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        freq_list = []
        for num, count in counts.items():
            freq_list.append((count, num))

        freq_list.sort(reverse=True)    

        unique_list = []
        for pair in freq_list:
            unique_list.append(pair[1])

        return unique_list[:k]
       


        