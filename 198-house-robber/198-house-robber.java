class Solution {
    public int rob(int[] nums) {
        int[] arr = new int[nums.length+1];
        arr[0] = 0;
        arr[1] = nums[0];
        for(int i=1; i<nums.length; i++){
            arr[i+1] = Math.max(arr[i], arr[i-1] + nums[i]);
        }
        return arr[nums.length];
    }
}