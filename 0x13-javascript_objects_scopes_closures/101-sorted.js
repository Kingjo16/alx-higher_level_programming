#!/usr/bin/node

const dictionary = require('./101-data').dict;

const entries = Object.entries(dictionary);
const values = Object.values(dictionary);
const uniqueValues = [...new Set(values)];
const newDictionary = {};

for (const value of uniqueValues) {
  const keyList = [];
  for (const entry of entries) {
    if (entry[1] === value) {
      keyList.unshift(entry[0]);
    }
  }
  newDictionary[value] = keyList;
}

console.log(newDictionary);
