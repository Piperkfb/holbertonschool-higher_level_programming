#!/usr/bin/node

const argument = process.argv[2];
let convert;

if (argument === undefined) {
  console.log('Not a number');
} else {
  convert = Number(argument);

  if (isNaN(convert)) {
    console.log('Not a number');
  } else if (Number.isInteger(convert)) {
    console.log('My number:', convert);
  } else {
    console.log('Not a number');
  }
}