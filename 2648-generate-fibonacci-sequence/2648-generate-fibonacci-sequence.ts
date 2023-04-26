function* fibGenerator(): Generator<number, any, number> {
    let a = 0, b = 1;
    yield a
    while(true){
        let k = a + b
        b = a
        a = k
        yield a
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */