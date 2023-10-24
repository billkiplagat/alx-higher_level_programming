#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = 18;
request(url, function (error, body) {
    if (error) {
      console.log(error);
    } else {
        try {
            const filmsData = JSON.parse(body);
        
            // Filter the films where Wedge Antilles is present
            const moviesWithWedgeAntilles = filmsData.results.filter((film) =>
              film.characters.includes(characterId)
            );
        
            console.log(moviesWithWedgeAntilles.length);
          } catch (err) {
            console.error('Error parsing JSON:', err);
          }

    }
  });
