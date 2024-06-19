#!/usr/bin/node
const { argv } = require('node:process');

console.log(`My number: ${!isNaN(Number(argv[2])) ? argv[2] : 'Not a number'}`);
