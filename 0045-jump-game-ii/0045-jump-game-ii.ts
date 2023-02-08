function jump(nums: number[]): number {
    let len = nums.length - 1, curr = -1, next = 0, ans = 0
    for (let i = 0; next < len; i++) {
        if (i > curr) ans++, curr = next
        next = Math.max(next, nums[i] + i)
    }
    return ans
};