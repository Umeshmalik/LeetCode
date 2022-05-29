class Solution {
    public int maxProduct(String[] words) {
        int max = 0;
        int len = words.length;
        for(int i =0;  i < len; i++){
            for(int j = i+1; j < len; j++){
                if(!isMatch(words[i], words[j])){
                    int mul = words[i].length() * words[j].length();
                    max = max > mul ? max : mul;
                }
            }
        }
        return max;
    }
    boolean isMatch(String a, String b){
        char[] chs = new char[26];
        int aLen = a.length();
        for(int i =0; i< aLen; i++){
            chs[a.charAt(i) - 'a']++;
        }
        int bLen = b.length();
        for(int i =0; i<bLen; i++){
            if(chs[b.charAt(i) - 'a'] > 0)
                return true;
        }
        return false;
    }
}