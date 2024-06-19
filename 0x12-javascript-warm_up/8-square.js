#!/usr/bin/node
const { argv, stdout } = require('node:process');
for (let i = 0; i < argv[2]; i++) {
  for (let j = 0; j < argv[2]; j++) {
    stdout.write('X');
  }
  console.log();
}
