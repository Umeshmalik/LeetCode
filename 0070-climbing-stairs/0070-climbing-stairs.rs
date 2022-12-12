impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n < 2{ return 1;}
        let mut a = 1;
        let mut b = 2;
        for i in 2..n{
            let t = a + b;
            a = b;
            b = t;
        }
        b
    }
}