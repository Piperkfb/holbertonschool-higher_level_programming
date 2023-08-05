#!/usr/bin/node

const movID = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + movID;

request.get(url, function(err, data, body) {
    if (err) {
        throw err;
    } else {
      const jsonData = JSON.parse(body).title
      console.log(jsonData);
    }
});