#!/usr/bin/node

const phrase = 'C is fun';
const arg = process.argv[2];
let i;
const x = Number(arg);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (Number.isInteger(x)) {
  for (i = 1; i <= x; i++) {
    console.log(phrase);
  }
}
