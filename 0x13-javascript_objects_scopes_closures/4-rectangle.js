#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const save = this.height;
    this.height = this.width;
    this.width = save;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};