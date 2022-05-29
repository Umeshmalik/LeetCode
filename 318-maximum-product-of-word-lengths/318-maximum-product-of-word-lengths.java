class Solution {
    public int maxProduct(String[] words) {
        int max = 0;
        for(int i =0;  i<words.length; i++){
            for(int j = i+1; j < words.length; j++){
                if(!isMatch(words[i], words[j]))
                    max = max > words[i].length() * words[j].length() ? max : words[i].length() * words[j].length();
            }
        }
        return max;
    }
    boolean isMatch(String a, String b){
        char[] chs = new char[26];
        for(int i =0; i< a.length(); i++){
            chs[a.charAt(i) - 'a']++;
        }
        for(int i =0; i<b.length(); i++){
            if(chs[b.charAt(i) - 'a'] > 0)
                return true;
        }
        return false;
    }
}