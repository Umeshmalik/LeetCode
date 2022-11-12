impl Solution {
    pub fn count_prime_set_bits(left: i32, right: i32) -> i32 {
        let primes : Vec<i32> = vec![2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31];
        let mut ans : i32 = 0;
        for i in left..right+1{
            let c : i32 = i.count_ones() as i32;
            for j in 0..primes.len(){
                if primes[j] == c {
                    ans += 1;
                    break;
                }
            }
        }
        return ans;
    }
}