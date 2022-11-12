use std::collections::BinaryHeap;

struct MedianFinder {
    f:BinaryHeap<i32>,
    s:BinaryHeap<i32>
}

impl MedianFinder {

    fn new() -> Self {
        Self{f:BinaryHeap::new(), s:BinaryHeap::new()}
    }
    
    fn add_num(&mut self, num: i32) {
        if self.f.len()==0 {self.f.push(num); return;}
        if *self.f.peek().unwrap()<=num {self.s.push(-num);} else {self.f.push(num);}
        if self.s.len()>self.f.len() { self.f.push(-self.s.pop().unwrap());}
        if self.s.len()+1<self.f.len() { self.s.push(-self.f.pop().unwrap());}
    }
    
    fn find_median(&self) -> f64 {
        let mut ans = *self.f.peek().unwrap() as f64;
        if self.f.len()==self.s.len() {ans=(ans-*self.s.peek().unwrap() as f64)/2.0;}
        ans
    }
}