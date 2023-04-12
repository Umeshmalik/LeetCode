type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr:  MultiDimensionalArray, n: number):  MultiDimensionalArray {
    const res: MultiDimensionalArray = [];
    const rec = (a: MultiDimensionalArray, k: number) => {
        for(let i in a){
            if(typeof a[i] == "number" || k <= 0){
                res.push(a[i])
            }else{
                rec(a[i] as MultiDimensionalArray, k-1)
            }
        }
    }
    rec(arr, n)
    return res;
};