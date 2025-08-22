class Solution {
    public boolean threeConsecutiveOdds(int[] nums) {
        int count = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] % 2 == 1){
                count++;
                if(count >= 3){
                   return true;
                }
            }else{
                count = 0;
            }
            
        }    
       
        return false;   
    }
}