#!/usr/bin/node

const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');
const request = require('request');

request.get(url, function(err, data) {
    if (err) throw err;
    fs.writeFile(path, data, 'utf8', function(err2) {
        if (err2) throw err2;
    });
});