function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    return arr.map((n, i) => fn(n, i))
};