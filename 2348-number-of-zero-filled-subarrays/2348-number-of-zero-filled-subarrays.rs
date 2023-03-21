impl Solution {
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {
        let mut curr = 0;
        let mut ans = 0;
        for i in nums{
            if i == 0{
                curr += 1;
            }
            else{
                ans += ((curr+1)*curr/2);
                curr = 0;
            }

            }
        ans + ((curr+1)*curr/2)
    }
}