#!/usr/bin/node

const arg = process.argv[2];
const str = process.argv[3];
const fs = require('fs');

fs.writeFile(arg, str, 'utf8', function (err) {
  if (err) throw err;
});
