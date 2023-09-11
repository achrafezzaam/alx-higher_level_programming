#!/usr/bin/node
const args = process.argv;
const intArg = parseInt(args[2]);

if (intArg) {
  for (let i = 0; i < intArg; i++) {
    console.log('#'.repeat(intArg));
  }
} else {
  console.log('Missing number of occurrences');
}
