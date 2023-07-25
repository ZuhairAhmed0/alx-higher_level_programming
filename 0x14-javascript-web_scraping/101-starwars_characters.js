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
  const characters = JSON.parse(res).characters;
  characters.forEach(character => {
    request.get(character, function (err, req, res) {
      if (!err) console.log(JSON.parse(res).name);
    });
  });
});
