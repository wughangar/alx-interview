#!/usr/bin/node

const request = require('request');
const providedFilmId = process.argv[2];
const filmApiUrl = `https://swapi-api.alx-tools.com/api/films/${providedFilmId}`;
let characterApiUrl;

request(filmApiUrl, async (filmError, filmResponse, filmBody) => {
  if (filmError) {
    console.log(filmError);
    return;
  }

  const characters = JSON.parse(filmBody).characters;

  for (characterApiUrl of characters) {
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

