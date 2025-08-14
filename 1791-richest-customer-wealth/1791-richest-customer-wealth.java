class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxWealth = 0;
        for(int[] i: accounts){
            int currentWealth = 0;
            for(int j: i){
                currentWealth += j;
                maxWealth = Math.max(maxWealth ,currentWealth);

            }
        }
        return maxWealth;
    }
}