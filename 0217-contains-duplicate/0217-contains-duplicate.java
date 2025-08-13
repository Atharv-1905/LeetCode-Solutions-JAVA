class Solution {
    public boolean containsDuplicate(int[] nums) {
        int numsSize = nums.length;
      
        HashSet<Integer> h1 = new HashSet<>();
        for (int n : nums) {
            // h1.add(n);
            if(!h1.add(n)){
            return true;
        }
        }
        
        // int count = h1.size();

        
        return false;
    }
}