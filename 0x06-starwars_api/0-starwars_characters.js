#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const data = JSON.parse(body);
    data.characters.forEach(function (character) {
      request(character, function (err, response, body) {
        if (!err && response.statusCode === 200) {
          const charData = JSON.parse(body);
          console.log(charData.name);
        }
      });
    });
  }
});
