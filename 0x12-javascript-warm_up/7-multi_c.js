#!/usr/bin/node
const args = process.argv;
let intArg = parseInt(args[2]);

if (intArg) {
  while (intArg > 0) {
    console.log('C is fun');
    intArg--;
  }
} else {
  console.log('Missing number of occurrences');
}
