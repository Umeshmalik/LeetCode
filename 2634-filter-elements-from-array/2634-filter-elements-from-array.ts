function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    return arr.filter((ar, i) => fn(ar, i))
};