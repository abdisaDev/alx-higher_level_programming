#!/usr/bin/node
const { argv } = require('node:process');

const lists = argv.splice(2);

if (lists.length <= 1) {
  console.log(0);
} else {
  const maxDigit = Math.max(...lists);
  lists[lists.indexOf(String(maxDigit))] = Number.NEGATIVE_INFINITY;
  console.log(Math.max(...lists));
}
