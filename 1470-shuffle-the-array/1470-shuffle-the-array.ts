function shuffle(nums: number[], n: number): number[] {
    return nums.slice(0, n).map((num, i) => [num, nums[i+n]]).reduce((acc, curr)=> [...acc, ...curr], []);
};