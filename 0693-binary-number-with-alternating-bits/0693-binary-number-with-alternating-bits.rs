impl Solution {
    pub fn has_alternating_bits(n: i32) -> bool {
        let b : String = format!("{:b}", n);
        let mut last : char = b.chars().next().unwrap();
        for i in b[1..].chars(){
            if last == i{return false;}
            last = i;
        }
        true
    }
}