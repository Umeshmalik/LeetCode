declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function(fn) {
    let ans = {};
    for(let i=0; i<this.length; i++){
        const n = fn(this[i])
        if(!ans[n]) ans[n] = []
        ans[n].push(this[i])
    }
    return ans
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */