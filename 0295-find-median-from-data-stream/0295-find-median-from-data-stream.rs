struct MedianFinder {
    arr: Vec<i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {

    fn new() -> Self {
        return Self {
            arr: vec![]
        }
    }
    
    fn add_num(&mut self, num: i32) {
        self.arr.push(num);
    }
    
    fn find_median(&mut self) -> f64 {
        let size : usize = self.arr.len();
        self.arr.sort();
        let ans : f64;
        if size&1 == 1 {
            ans = self.arr[size>>1] as f64;
        }else{
            let n1 : f64 = self.arr[size>>1] as f64;
            let n2 : f64 = self.arr[(size>>1)-1] as f64;
            ans = ((n1 + n2) / 2.0) as f64;
        }
        return ans;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */