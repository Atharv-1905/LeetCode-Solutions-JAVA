
import java.util.ArrayList;

class Solution {
    public void rotate(int[] arr, int k) {
       int n=arr.length;
       k=k%n;
       ArrayList <Integer> l=new ArrayList<>();
      for(int i=n-k;i<n;i++){
        l.add(arr[i]);
      }
      for(int i=n-k-1;i>=0;i--){
        arr[i+k]=arr[i];
      }
      for(int i=0;i<k;i++){
        arr[i]=l.get(i);
      }
    }
}