#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;
let people = [];
const names = [];

const requestCharacters = async () => {
  await new Promise(resolve => {
    request(filmEndPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error(`Error: ${err} | StatusCode: ${res.statusCode}`);
      } else {
        const jsonBody = JSON.parse(body);
        people = jsonBody.characters;
        resolve();
      }
    });
  });
};

const requestNames = async () => {
  if (people.length > 0) {
    for (const p of people) {
      await new Promise(resolve => {
        request(p, (err, res, body) => {
          if (err || res.statusCode !== 200) {
            console.error(`Error: ${err} | StatusCode: ${res.statusCode}`);
          } else {
            const jsonBody = JSON.parse(body);
            names.push(jsonBody.name);
            resolve();
          }
        });
      });
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const [index, n] of names.entries()) {
    process.stdout.write(n);
    if (index !== names.length - 1) {
      process.stdout.write('\n');
    }
  }
};

getCharNames();
