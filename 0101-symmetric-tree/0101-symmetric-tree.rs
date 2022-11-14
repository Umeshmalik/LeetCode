// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn helper(left: &Option<Rc<RefCell<TreeNode>>>, right: &Option<Rc<RefCell<TreeNode>>>) -> bool {
            match (left, right) {
                (None, None) => true,
                (Some(l), Some(r)) =>{
                    let l = l.as_ref().borrow();
                    let r = r.as_ref().borrow();
                    if l.val != r.val {
                        return false;
                    }
                    helper(&l.left, &r.right) && helper(&l.right, &r.left)
                },
                _ => false,
            }
        }
        if root.is_none() {
            return true;
        }
        let root = root.unwrap();
        let left = &root.as_ref().borrow().left;
        let right = &root.as_ref().borrow().right;
        helper(left, right)        
    }
}