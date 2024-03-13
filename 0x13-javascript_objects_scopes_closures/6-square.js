#!/usr/bin/node
const prvsquare = require('./5-square');

class Square extends prvsquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let m = 0; m < this.height; m++) {
      let size = '';
      for (let k = 0; k < this.width; k++) {
        size += c;
      }
      console.log(size);
    }
  }
}

module.exports = Square;
