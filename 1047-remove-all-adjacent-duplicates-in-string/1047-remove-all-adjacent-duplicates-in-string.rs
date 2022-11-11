impl Solution {
    pub fn remove_duplicates(s: String) -> String {
        let mut arr = Vec::new();
        for i in s.chars(){
            if let Some(x) = arr.last(){
                if *x == i {
                    arr.pop();
                    continue;
                }
            }
            arr.push(i);
        }
        return arr.into_iter().collect();
    }
}