#!/usr/bin/node
const data = require('100-data.js');

const newData = data.map((value, index) => {
  return value * index;
});

console.log(newData);
