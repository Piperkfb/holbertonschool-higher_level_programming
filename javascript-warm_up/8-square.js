#!/usr/bin/node

const arg = process.argv[2];
let row = 0;
let coll;
const conv = Number(arg);

if (isNaN(conv)) {
  console.log('Missing size');
} else if (Number.isInteger(conv)) {
  while (row < conv) {
    let rowString = '';
    coll = 0;
    while (coll < conv) {
      rowString += 'X';
      coll++;
    }
    console.log(rowString);
    row++;
  }
}
