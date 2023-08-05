#!/usr/bin/node

const arg = process.argv[2];
const fs = require('fs');

fs.readFile(arg, 'utf8', function(err, data) {
    console.log(err || data);
});