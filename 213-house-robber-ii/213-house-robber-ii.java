class Solution {
    public int rob(int[] nums) { 
        if(nums.length == 1) return nums[0];
        return Math.max(helper(nums, 1, nums.length), helper(nums, 0, nums.length-1));
    }
    int helper(int[] nums,int start,int end){
        int[] arr = new int[end-start+1];
        arr[0] = 0;
        arr[1] = nums[start];
        for(int i=start+1; i< end; i++){
            arr[i+1-start] = Math.max(arr[i-start], arr[i-1-start] + nums[i]);
        }
        return arr[end-start];
    }
}