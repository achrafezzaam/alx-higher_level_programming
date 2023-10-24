#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let occurence = 0;
    for (const movie in movies) {
      const characters = movies[movie].characters;
      for (const character in characters) {
        if (characters[character].includes('18')) {
          occurence++;
        }
      }
    }
    console.log(occurence);
  }
});
