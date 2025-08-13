class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
       HashSet<Integer> h1 = new HashSet<>();
       HashSet<Integer> h2 = new HashSet<>();
       for(int n:nums1){
          h1.add(n);
       } 

       for(int n:nums2){
        if(h1.contains(n)){
          h2.add(n);
        }
       } 
       int[] nums = new int[h2.size()];
       int i = 0;
       for(int n:h2){
        nums[i] = n;
        i++;

       }
       return nums;
    }
}