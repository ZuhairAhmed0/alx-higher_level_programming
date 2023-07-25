#!/usr/bin/node
/*
 * that script prints the number of movies where the character
 * “Wedge Antilles” is present
 */

const fs = require('fs');
const request = require('request');
const URL = process.argv[2];
const filePath = process.argv[3];

request.get(URL, function (err, req, res) {
  if (err) console.error(err);
  fs.writeFile(filePath, res, 'utf-8', function (err, data) {
    if (err) console.error(err);
  });
});
