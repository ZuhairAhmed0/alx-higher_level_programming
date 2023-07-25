#!/usr/bin/node
/*
 * that script reads and prints the content of a file.
 */

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) console.error(err);
  console.log(data);
});
