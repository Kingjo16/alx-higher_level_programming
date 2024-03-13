#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileAContent = fs.readFileSync(process.argv[2], 'utf8');
const fileBContent = fs.readFileSync(process.argv[3], 'utf8');
const concatenatedContent = fileAContent + fileBContent;
fs.writeFileSync(process.argv[4], concatenatedContent);
