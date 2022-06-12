/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    const obj = {};
    insert(obj, 0, 0);
    let sum = 0;
    let res = 0;
    for(let i = 0; i < nums.length; i++){
        sum += nums[i];
        if(obj[sum - k]){
            res += obj[sum - k].length;
        }
        insert(obj, sum, i);
    }
    return res;
};

const insert = (obj, key, value) => {
    if(obj[key]){
        obj[key].push(value);
    }else{
        obj[key] = [value];
    }
}