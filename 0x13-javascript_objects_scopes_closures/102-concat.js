#!/usr/bin/node

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const dest = process.argv[4];

const data1 = fs.readFileSync(file1);
const data2 = fs.readFileSync(file2);
const combinedData = data1 + data2;

fs.writeFileSync(dest, combinedData);
