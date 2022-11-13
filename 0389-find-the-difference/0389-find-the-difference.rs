impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        let mut vec1 : [i32;32]  = [0; 32];
        let mut vec2 : [i32;32]  = [0; 32];
        for i in s.bytes(){ vec1[(i-97) as usize] += 1; }
        for i in t.bytes(){ vec2[(i-97) as usize] += 1; }
        for i in 0..26{
            if vec1[i] > vec2[i] {return (i + 97) as u8 as char;}
            else if vec1[i] < vec2[i] {return (i + 97) as u8 as char;}
        }
        ' '
    }
}