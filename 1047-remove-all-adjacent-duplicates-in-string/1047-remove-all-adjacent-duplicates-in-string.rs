impl Solution {
    pub fn remove_duplicates(s: String) -> String {
        let mut arr = Vec::new();
        let mut list : Vec<String> = Vec::new();
        for i in s.split(""){
            arr.push(i.to_string());
        }
        for i in 0..s.len()+1{
            if list.len() > 0 && list.last() == arr.get(i){
                list.pop();
            }else{
                list.push(arr[i].to_string());
            }
        }
        return list.join("");
    }
}