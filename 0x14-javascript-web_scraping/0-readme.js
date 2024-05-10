#!/usr/bin/node
// Read from file

const fs_l = require('fs');
fs_l.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
