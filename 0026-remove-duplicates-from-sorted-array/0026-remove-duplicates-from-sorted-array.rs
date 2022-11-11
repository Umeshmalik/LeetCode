impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut i : usize = 0;
        let mut j : usize = 0;
        let n : usize = nums.len();
        while j < n {
            let temp : i32 = nums[j];
            while j < n && nums[j] == temp { j += 1; }
            nums[i] = temp;
            i += 1;
        }
        return i as i32;
    }
}