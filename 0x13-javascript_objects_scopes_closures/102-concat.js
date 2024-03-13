#!/usr/bin/node
const files = require('fs');

const firstFileContent = files.readFileSync(process.argv[2]).toString();
const secondFileContent = files.readFileSync(process.argv[3]).toString();
files.writeFileSync(process.argv[4], concatenatedContent);
