class Solution {
    public int minOperations(String[] logs) {
        int depth = 0;

        for (String op : logs) {
            if (op.equals("../")) {
                if (depth > 0) {
                    depth--;
                }
            } 
            else if (op.equals("./")) {
                continue;
            } 
            else {
                
                depth++;
            }
        }

        return depth;
    }
}