#!/usr/bin/node
const { argv, stdout } = require('node:process');
const size = Number(argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      stdout.write('X');
    }
    console.log();
  }
}
