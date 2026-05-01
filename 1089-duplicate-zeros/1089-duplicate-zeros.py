class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                # Insert a zero at the next position
                arr.insert(i, 0)
                # Remove the element that was pushed out of bounds
                arr.pop()
                # Skip the newly inserted zero to avoid an infinite loop
                i += 1
            i += 1


        
        
        