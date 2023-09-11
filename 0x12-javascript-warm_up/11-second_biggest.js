#!/usr/bin/node
if (process.argv.length > 3) {
  const save = process.argv.map(Number).slice(2, process.argv.length).sort();
  console.log(save[save.length - 2]);
} else {
  console.log(0);
}
