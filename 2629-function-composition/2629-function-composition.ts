type F = (x: number) => number;

function compose(functions: F[]): F {
    return (n) => functions.reduceRight((acc, curr) => curr(acc) ,n);
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */