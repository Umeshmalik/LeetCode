impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        if n < 0 {return false;}
        let mut c : i32 = 0;
        let mut t : i32 = n;
        for i in 0..32{
            if t == 0{break;}
            c += t&1;
            t >>= 1;
        }
        return c == 1;
    }
}