impl Solution {
    pub fn reverse_words(s: String) -> String {
        let chunks = s.split(" ").filter(|n| n != &"");
        let mut string = String::from("");
        for i in chunks{
            string = i.to_string() + &" ".to_string() + &string;
        }
        String::from( string.trim())
    }
}