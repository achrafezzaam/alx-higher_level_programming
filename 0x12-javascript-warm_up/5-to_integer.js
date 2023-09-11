#!/usr/bin/node
const args = process.argv;
const intArg = parseInt(args[2]);

if (intArg) {
  console.log('My number: ' + intArg);
} else {
  console.log('Not a number');
}
