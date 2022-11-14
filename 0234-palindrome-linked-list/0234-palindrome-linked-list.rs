// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn is_palindrome(mut head: Option<Box<ListNode>>) -> bool {
        let mut vector: Vec<i32> = vec![];
        while let Some(c) = head{ vector.push(c.val); head = c.next; }
        let size: usize = vector.len();
        for i in 0..size/2{ if vector[i] != vector[size - 1 - i]{return false;} }
        true
    }
}