#!/usr/bin/node
const { readFileSync, writeFileSync } = require('fs');
const { argv } = require('node:process');

const first = readFileSync(argv[2], 'utf8');
const second = readFileSync(argv[3], 'utf8');

writeFileSync(argv[4], first + second);
