impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut ans : Vec<String> = vec![];
        let n: usize = nums.len();
        if n == 0 {return ans;}
        let mut small : i32 = nums[0];
        for i in 1..n{
            if nums[i-1] + 1 == nums[i]{
                continue;
            }
            if nums[i-1] == small {
                ans.push(nums[i-1].to_string());
            }else{
                ans.push(small.to_string() + "->" + &nums[i-1].to_string());
            }
            small = nums[i];
        }
        if nums[n-1] == small {
            ans.push(nums[n-1].to_string());
        }else{
            ans.push(small.to_string() + "->" + &nums[n-1].to_string());
        }
        return ans;
    }
}