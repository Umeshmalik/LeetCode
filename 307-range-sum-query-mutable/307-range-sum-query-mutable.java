class NumArray {
    int[] arr;
    int sum = 0;
    public NumArray(int[] nums) {
        arr = nums;
        for(int i : nums){
            sum += i;
        }
    }
    
    public void update(int index, int val) {
        int diff = val - arr[index];
        sum += diff;
        arr[index] = val;
    }
    
    public int sumRange(int left, int right) {
        int l = 0;
        for(int i=0; i<left; i++) l += arr[i];
        for(int i = right + 1; i < arr.length; i++) l += arr[i];
        return sum - l;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */