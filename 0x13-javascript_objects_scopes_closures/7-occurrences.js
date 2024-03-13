#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocure = 0;
  for (let m = 0; m < list.length; m++) {
    if (searchElement === list[m]) {
      ocure++;
    }
  }
  return ocure;
};
