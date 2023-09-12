#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const file1 = fs.readFileSync(args[2], 'utf-8');
const file2 = fs.readFileSync(args[3], 'utf-8');
fs.writeFileSync(args[4], file1 + file2);
