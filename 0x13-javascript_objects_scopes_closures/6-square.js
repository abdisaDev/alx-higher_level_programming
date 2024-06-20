#!/usr/bin/node

const SquareR = require('./5-square');

class Square extends SquareR {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
