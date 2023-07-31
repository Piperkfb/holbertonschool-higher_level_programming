#!/usr/bin/node

function factor (a) {
  if (a === 0 || a === 1) { return 1; }
  return a * factor (a - 1);
  }

const arg = process.argv[2];
const num = Number(arg);

if (isNaN(num)) {
  console.log(1);
} else if (Number.isInteger(num)) {
  const result = factor(num);
  console.log(result);
}
