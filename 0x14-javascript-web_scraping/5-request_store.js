#!/usr/bin/node

const req = require('request');
const files = require('fs');

req.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    files.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
