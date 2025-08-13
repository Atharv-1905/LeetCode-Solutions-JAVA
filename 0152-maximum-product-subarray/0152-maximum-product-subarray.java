class Solution {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int maxSoFar = nums[0];
        int currentProduct = 1;
        for (int num : nums) {
            currentProduct *= num;
            maxSoFar = Math.max(maxSoFar, currentProduct);
            if (num == 0) {
                currentProduct = 1;
            }
        }
        currentProduct = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            int num = nums[i];
            currentProduct *= num;
            maxSoFar = Math.max(maxSoFar, currentProduct);
            if (num == 0) {
                currentProduct = 1;
            }
        }

        return maxSoFar;
    }
}