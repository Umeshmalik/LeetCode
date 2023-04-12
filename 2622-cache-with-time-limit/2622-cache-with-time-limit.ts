class TimeLimitedCache {
    store: object;
    constructor() {
        this.store = {};
    }

    set(key: number, value: number, duration: number): boolean {
        let isExist = false;
        if(this.store[key]) isExist = true;
        this.store[key] = {
            value: value,
            duration: Date.now() + duration
        }
        return isExist;
    }

    get(key: number): number {
        if(!this.store[key] || this.store[key].duration < Date.now()) return -1;
        return this.store[key].value;
    }

	count(): number {
        return Object.keys(this.store).reduce((acc, curr) => acc + (this.store[curr].duration > Date.now() ? 1 : 0),0);
    }
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */