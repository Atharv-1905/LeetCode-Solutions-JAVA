class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Step 1: Count character frequencies
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
                
        length = 0
        has_odd = False
        
        # Step 2 & 3: Calculate length based on pairs and find odd counts
        for count in counts.values():
            # This mathematically extracts the largest even number 
            # (e.g., 5 // 2 * 2 = 4)
            length += (count // 2) * 2
            
            # If the count is odd, we can use one character for the center
            if count % 2 != 0:
                has_odd = True
                
        # Step 4: Add the center character if one exists
        if has_odd:
            length += 1
            
        return length