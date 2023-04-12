/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    const res = [];
    const rec = (a, k) => {
        for(let i in a){
            if(typeof a[i] == "number" || k <= 0){
                res.push(a[i])
            }else{
                rec(a[i], k-1)
            }
        }
    }
    rec(arr, n)
    return res;
};