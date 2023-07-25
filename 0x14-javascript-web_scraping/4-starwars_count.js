#!/usr/bin/node
/*
 * that script prints the number of movies where the character
 * “Wedge Antilles” is present
 */

const request = require('request');
const URL = process.argv[2];

request.get(URL, function (err, req, res) {
  if (err) console.error(err);
  const films = JSON.parse(res).results;
  const moviesWithWedge = films.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18'));
  console.log(moviesWithWedge.length);
});
