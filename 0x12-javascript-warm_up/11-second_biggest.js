#!/usr/bin/node
const { argv } = require('node:process');

const lists = argv.splice(2);

if (lists.length <= 1) {
  console.log(0);
} else {
  const max_digit = Math.max(...lists);
  lists[lists.indexOf(max_digit)] = Number.NEGATIVE_INFINITY;
  console.log(Math.max(...lists));
}
