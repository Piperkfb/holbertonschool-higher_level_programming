#!/usr/bin/node

const url = process.argv[2];
const request = require('request')

request.get(url, function(err, status) {
    if (err) {
        console.log('code:', status.statusCode);
    } else {
        console.log('code:', status.statusCode);
    }
})