#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    console.log(err);
  }
});
