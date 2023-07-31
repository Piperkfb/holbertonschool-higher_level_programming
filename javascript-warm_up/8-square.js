#!/usr/bin/node

const arg = process.argv[2];
let row = 0;
let coll;

conv = Number(arg);
if (isNaN(conv)) {
  console.log('Missing size');
} else if (Number.isInteger(conv)) {
    while (row < conv) {
        let rowString = '';
        column = 0;
        while (column < conv) {
          rowString += 'X';
          column++;
        }
        console.log(rowString);
        row++;
      }
    }