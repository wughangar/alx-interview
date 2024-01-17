#!/usr/bin/node

const request = require('request');

function getCharacters(movieId) {
	const url = `https://swapi-api.alx-tools.com/films/${movieId}/`;
	request(url, { json: true }, (error, response, body) => {
		if (error) {
			console.error('Error fetching movie data:', error);
			return;
		}
	if (response.statusCode !== 200) {
		console.error(`Unexpected status code: ${response.statusCode}`);
		return;
	}

	const characters = body.characters;
	characters.forEach(characterURL => {
		request(characterURL, { json: true }, (charError, charResponse, charBody) => {
		if (charError) {
			console.error('Error fetching character data:', charError)
			return;
        }
		if (charResponse.statusCode !== 200) {
			console.error(`Unexpected status code for character: ${charResponse.statusCode}`);
			return;
		}
		console.log('Character:', charBosy.name);
		});
	});
	});
}

const movieId = process.argv[2];
if (!movieId) {
	console.error('Please provide a Movie ID as a command-line argument.');
} else {
	getCharacters(movieId);
}
