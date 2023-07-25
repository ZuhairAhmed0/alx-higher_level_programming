#!/usr/bin/node
/*
 * that script prints the number of movies where the character
 * “Wedge Antilles” is present
 */

const request = require('request');
const URL = process.argv[2];

request.get(URL, function (err, req, res) {
  if (err) console.error(err);
	request.get('https://swapi-api.alx-tools.com/api/people/18', function (err, req, res) {
		if (err) console.error(err);
		const films = JSON.parse(res).films;
		console.log(films.length);
	});
});
