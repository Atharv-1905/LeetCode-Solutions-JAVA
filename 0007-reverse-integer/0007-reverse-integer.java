class Solution {
    public int reverse(int x) {
        int reversed = 0;
        int rem;

        while (x != 0) {
           
            if (reversed > Integer.MAX_VALUE / 10 || reversed < Integer.MIN_VALUE / 10) {
                return 0; 
            }

            rem = x % 10;
            reversed = reversed * 10 + rem;
            x = x / 10;
        }
        return reversed;
    }
}