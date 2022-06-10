class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> mp = new HashSet<>();
        int l = 0, m = 0;
        int size = s.length();
        for(int i = 0; i < size; i++){
            char ch = s.charAt(i);
            if(mp.contains(ch)){
                while(s.charAt(l) != ch){
                    char ch1 = s.charAt(l);
                    mp.remove(ch1);
                    l++;
                }
                char ch2 = s.charAt(l);
                mp.remove(ch2);
                l++;
            }
            mp.add(ch);
            m = Math.max(m, i - l + 1);
        }
        return m;
    }
}