class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        HashSet<Integer> hs = new HashSet<>();
        int res = 0, curr = 0;
        int l = 0, r = 0, len = nums.length;
        while(r < len){
            if(hs.contains(nums[r])){
                while(nums[l] != nums[r]){
                    curr -= nums[l];
                    hs.remove(nums[l]);
                    l++;
                }
                curr -= nums[l];
                l++;
            }
            curr += nums[r];
            res = Math.max(res, curr);
            hs.add(nums[r]);
            r++;
        }
        return res;
    }
}