#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get(url, function(err, data, body) {
    if (err) throw err;
    Jason = JSON.parse(body).results;
    let movNum = 0;

    for (const movie in Jason)
    const charList = Jason[movie].characters
    for (const char in charList) {
        if (charList[char].includes('/18/')) {
            movNum++;
        }
    }
    console.log(movNum);
})