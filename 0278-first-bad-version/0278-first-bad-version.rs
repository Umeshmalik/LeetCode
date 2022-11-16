// The API isBadVersion is defined for you.
// isBadVersion(version:i32)-> bool;
// to call it use self.isBadVersion(version)

impl Solution {
    pub fn first_bad_version(&self, n: i32) -> i32 {
		let mut low: i64 = 0;
        let mut high: i64 = n as i64;
        while low <= high{
            let mid : i64 = (low+high)/2;
            let fi = self.isBadVersion(mid as i32);
            let se = self.isBadVersion(mid as i32 - 1);
            if se == false && fi == true{
                return mid as i32;
            }else if fi == true && se == true{
                high = mid - 1;
            }else{
                low = mid + 1;
            }
        }
        0
    }
}