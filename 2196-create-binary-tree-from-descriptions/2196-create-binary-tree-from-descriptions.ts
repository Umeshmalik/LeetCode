/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function createBinaryTree(descriptions: number[][]): TreeNode | null {
    const arr = new Set(descriptions.reduce((acc, curr) => [...acc, curr[0]], []));
    const mp = {};
    descriptions.forEach(([f, s, t]) => {
        mp[f] = new TreeNode(f)
        mp[s] = new TreeNode(s)
    })
    descriptions.forEach(([f, s, t]) => {
        if(t === 1) mp[f].left = mp[s]
        else mp[f].right = mp[s]
        if(arr.has(s)) arr.delete(s)
    })
    return mp[[...arr].pop()];
};