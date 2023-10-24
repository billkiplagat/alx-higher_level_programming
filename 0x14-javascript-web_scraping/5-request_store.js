#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const content_file = process.argv[3];

request(url, function (error, body){
    if (error) {
        console.log(error);
    }else{
        fs.writeFile(content_file, body, 'utf-8', function (err) {
            if (err) {
              console.error(err);
              return;
            }
          });
    }
})

