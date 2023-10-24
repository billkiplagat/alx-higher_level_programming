#!/usr/bin/node
const fs = require('fs');

const file_path = process.argv[2]
const content = process.argv[3];
fs.writeFile(file_path, content, 'utf-8', function (err) {
  if (err) {
    console.error(err);
    return;
  }
});
