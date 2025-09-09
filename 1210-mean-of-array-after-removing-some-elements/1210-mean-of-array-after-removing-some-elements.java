class Solution {
    public double trimMean(int[] arr) {
         Arrays.sort(arr);
        
        int n = arr.length;
        int elementsToRemove = n / 20;
        
        double sum = 0;
        for (int i = elementsToRemove; i < n - elementsToRemove; i++) {
            sum += arr[i];
        }
        
        double count = n - (2 * elementsToRemove);
        
        return sum / count;
    }
}