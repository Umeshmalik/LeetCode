impl Solution {
    pub fn count_prime_set_bits(left: i32, right: i32) -> i32 {
        let primes : Vec<i32> = vec![2, 3, 5, 7, 11, 13, 17, 19];
        let mut ans : i32 = 0;
        for i in left..right+1{
            if primes.contains(&(i.count_ones() as i32)){ ans += 1; }
        }
        ans
    }
}