#!/usr/bin/node
/*
 * that script prints the title of a Star Wars movie
 * where the episode number matches a given integer..
 */

const request = require('request');
const ID = process.argv[2];
const URL = 'https://swapi-api.alx-tools.com/api/films';

request.get(`${URL}/${ID}`, function (err, req, res) {
  if (err) console.error(err);
const movie = JSON.parse(res);
  console.log(movie.title);
});
