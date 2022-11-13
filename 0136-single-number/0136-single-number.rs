impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut n = 0;
        for i in nums{ n ^= i; }
        n
    }
}