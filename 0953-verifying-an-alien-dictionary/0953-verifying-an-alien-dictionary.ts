function isAlienSorted(words: string[], order: string): boolean {
    const mp = order.split("").reduce((acc, curr, idx) => ({ ...acc, [curr]: idx }), {});
    for (let i = 1; i < words.length; i++) {
        if (words[i].length < words[i - 1].length && words[i - 1].slice(0, words[i].length) == words[i]) return false
        for (let j = 0; j < Math.min(words[i].length, words[i - 1].length); j++) {
            const char1 = words[i][j], char2 = words[i - 1][j];
            if (mp[char1] < mp[char2]) return false
            else if(char1 === char2) continue;
            else break
        }
    }
    return true
};