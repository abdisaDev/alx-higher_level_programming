#!/usr/bin/node
const {list} = require('./100-data.js');

const newData = list.map((value, index) => {
  return value * index;
});

console.log(newData);
