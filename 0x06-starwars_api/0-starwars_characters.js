#!/usr/bin/node

const request = require('request');
const providedFilmId = process.argv[2];
const filmApiUrl = `https://swapi-api.hbtn.io/api/films/${providedFilmId}`;

request(filmApiUrl, async (filmError, filmResponse, filmBody) => {
  if (filmError) {
    console.log(filmError);
  }
  for (const characterApiUrl of JSON.parse(filmBody).characters) {
    await new Promise((resolve, reject) => {
      request(characterApiUrl, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          reject(characterError);
        }
        console.log(JSON.parse(characterBody).name);
        resolve();
      });
    });
  }
});
