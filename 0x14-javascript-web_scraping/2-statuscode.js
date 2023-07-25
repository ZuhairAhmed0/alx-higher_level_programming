#!/usr/bin/node
/*
 * that script that display the status code of a GET request.
 */

const request = require('request');
const URL = process.argv[2];

request.get(URL, function (err, response, body) {
  if (err) console.error(err);
  console.log(`code: ${response.statusCode}`);
});
