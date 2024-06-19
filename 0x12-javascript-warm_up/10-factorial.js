#!/usr/bin/node
const { argv } = require('node:process');

function factorial (a) {
  const num = Number(a);

  if (isNaN(num) || num === 0) {
    return 1;
  }

  return factorial(num - 1) * num;
}

console.log(factorial(argv[2]));
