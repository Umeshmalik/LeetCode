/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * unsafe fn guess(num: i32) -> i32 {}
 */

impl Solution {
    unsafe fn guessNumber(n: i32) -> i32 {
        let mut high : i64 = n as i64;
        let mut low : i64 = 0;
        while low <= high{
            let mid : i64 = (high + low) >> 1;
            match guess(mid as i32){
                0 => return mid as i32,
                -1 => high = mid - 1,
                1 => low = mid + 1,
                _ => return -2
            }
        }
        -1
    }
}