#!/usr/bin/node

function factor(a) {
    if (a === 0 || a === 1)
    return 1;
    for (let i = a - 1; i >= 1; i--) {
        a *= i;
    }
    return a;
}

const arg = process.argv[2];
const num = Number(arg);

if (isNaN(num)) {
    console.log(1);
} else if (Number.isInteger(num)) {
    const result = factor(num);
    console.log(result)
}