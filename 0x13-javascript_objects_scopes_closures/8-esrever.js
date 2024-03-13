#!/usr/bin/node
exports.esrever = function (list) {
  let lengths = list.length - 1;
  let m = 0;
  while ((lengths - m) > 0) {
    const axis = list[lengths];
    list[lengths] = list[m];
    list[m] = axis;
    m++;
    lengths--;
  }
  return list;
};
