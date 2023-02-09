#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const index = 0;
    const data = JSON.parse(body).characters;

    printCharacters(data, index);
  }
});

const printCharacters = function (url, index) {
  request(url[index], (err, response, body) => {
    if (!err && response.statusCode === 200) {
      const charData = JSON.parse(body);
      console.log(charData.name);
    }

    if (++index < url.length) {
      printCharacters(url, index++);
    }
  });
};
