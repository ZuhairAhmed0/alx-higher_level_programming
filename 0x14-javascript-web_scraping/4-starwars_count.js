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
  console.log(films.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0));
});
