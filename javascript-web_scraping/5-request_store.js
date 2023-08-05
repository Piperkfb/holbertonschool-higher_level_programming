#!/usr/bin/node

const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');
const request = require('request');

request.get(url, function (err, data, body) {
  if (err) throw err;
  fs.writeFile(path, body, 'utf8', function (err2) {
    if (err2) throw err2;
  });
});
