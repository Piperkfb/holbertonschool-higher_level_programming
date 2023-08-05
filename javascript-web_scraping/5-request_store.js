#!/usr/bin/node

const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');
const request = require('request');

request.get(url, 'utf8', function(err, data, body) {
    if (err) throw err;
    const Jason = JSON.parse(body);
    fs.writeFile(path, Jason, function(err2) {
        if (err2) throw err2;
    });
});