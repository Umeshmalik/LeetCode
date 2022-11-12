impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        s.split(" ").filter(|x| x != &"").last().unwrap().len() as i32
    }
}