impl Solution {
    pub fn reverse_words(s: String) -> String {
        s.split(' ').filter(|n| n != &"").rev().collect::<Vec<_>>().join(" ")
    }
}