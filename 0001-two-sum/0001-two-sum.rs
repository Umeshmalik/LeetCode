use::std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        for i in 0..nums.len(){
            let rem = target - nums[i];
            if let Some(s) = map.get(&rem){
                if map.contains_key(&rem){
                    return vec![*s, i as i32];
                }
            }
            map.insert(nums[i], i as i32);
        }
        return vec![];
    }
}