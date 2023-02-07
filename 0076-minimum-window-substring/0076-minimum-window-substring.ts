function minWindow(A: string, B: string): string {
    if(B.length > A.length) return "";
    let ans = "";
    const bMap = B.split("").reduce((acc, curr) => ({ ...acc, [curr]: (acc[curr] || 0) + 1 }), {})
    let start = 0, end = 0;
    while (end < A.length) {
        const endChar = A[end];
        if (bMap[endChar] !== undefined) {
            bMap[endChar] -= 1
        }
        end += 1;
        if (Object.values(bMap).reduce((acc, curr) => (curr > 0 || !acc) ? false : true, true)) {
            while (Object.values(bMap).reduce((acc, curr) => (curr > 0 || !acc) ? false : true, true)) {
                const startChar = A[start];
                if (bMap[startChar] !== undefined) {
                    bMap[startChar] += 1;
                }
                start += 1;
            }
            ans = (ans.length > end - start + 1 || ans === "") ? A.slice(start - 1, end) : ans;
        }
    }
    return ans;
};