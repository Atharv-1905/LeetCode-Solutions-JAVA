class Solution {
    public boolean isPalindrome(int x) {
        int reverse = 0;
        int y = x;

        if(y<0 || y % 10 == 0 && y != 0 ){
            return false;
        }

    
        while(y>0){
            reverse = reverse * 10 + y % 10;
            y = y/10;
        }
        return x == reverse;
    }
}