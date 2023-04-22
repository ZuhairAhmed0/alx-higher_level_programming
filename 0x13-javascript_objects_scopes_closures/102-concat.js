#!/usr/bin/node

const fs = require('f');

const file1 = process.argv[2];
const file2 = process.argv[3];
const dest = process.argv[4];

const data1 = fs.readFileSync(file1, 'utf8');
const data2 = fs.readFileSync(file2, 'utf8');
const combinedData = data1 + data2;

fs.writeFileSync(dest, combinedData, 'utf8');
console.log(`Successfully concatenated ${file1} and ${file2} into ${dest}.`);
