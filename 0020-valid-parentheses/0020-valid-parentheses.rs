impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut _vec : Vec<char> = vec![];
        for i in s.chars(){
            if _vec.len() == 0 && ( i == ']' || i == '}' || i == ')'){
                return false;
            }else if (i == '}' && _vec.last().unwrap() == &'{') || (i == ']' && _vec.last().unwrap() == &'[') || (i == ')' && _vec.last().unwrap() == &'('){
                _vec.pop();
            }else{
                _vec.push(i);
            }
        }
        if _vec.len() == 0{ return true;}
        return false;
    }
}