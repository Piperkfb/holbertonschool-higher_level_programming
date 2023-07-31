#!/usr/bin/node

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
let result;

function add (a, b) {
  const sum = (a + b);
  return (sum);
}

if (num1 === undefined || num2 === undefined || isNaN(num1, num2)) {
  console.log('NaN');
} else {
  result = add(num1, num2);
  console.log(result);
}
