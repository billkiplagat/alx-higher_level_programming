#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const contentFile = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(contentFile, body, 'utf-8', function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
});
