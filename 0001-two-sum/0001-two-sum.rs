use::std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        for (i, n) in nums.into_iter().enumerate(){
            let rem = target - n;
            if let Some(s) = map.get(&rem){
                if map.contains_key(&rem){
                    return vec![*s, i as i32];
                }
            }
            map.insert(n, i as i32);
        }
        return vec![];
    }
}