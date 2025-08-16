class Solution {
    public int maximum69Number (int num) {
        String str = String.valueOf(num);
        char[] digit = str.toCharArray();
        for(int i=0; i<digit.length; i++){
            if(digit[i] == '6'){
                digit[i] = '9';
                break;

            }
           
        }
         String newstr = new String(digit);
            int newnum = Integer.parseInt(newstr);
        return newnum;
        
    }
}