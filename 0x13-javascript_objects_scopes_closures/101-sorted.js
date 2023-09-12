#!/usr/bin/node
const dict = require('./101-data.js').dict;
const output = {};
for (const key in dict) {
  if (output[dict[key]]) {
    output[dict[key]].push(key);
  } else {
    output[dict[key]] = [key];
  }
}
console.log(output);
