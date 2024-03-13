#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let m = 0; m < this.height; m++) {
      let size = '';
      for (let k = 0; k < this.width; k++) {
        size += 'X';
      }
      console.log(size);
    }
  }

  rotate () {
    const axsis = this.width;
    this.width = this.height;
    this.height = axsis;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
