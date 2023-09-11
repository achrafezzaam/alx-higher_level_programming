#!/usr/bin/node
const args = process.argv;
let i = 2;
let save = 0;

while (args[i] && args.length > 3) {
  if (i === 2 || parseInt(args[i]) > save) {
    save = parseInt(args[i]);
  }
  i++;
}

console.log(save);
