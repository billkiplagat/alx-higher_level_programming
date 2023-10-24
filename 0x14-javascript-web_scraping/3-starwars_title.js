#!/usr/bin/node
const request = require('request');
const movie_id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/'
request(url + movie_id, function (error, body) {
    if (error){
        console.log(error)
    }else{
        console.log(JSON.parse(body).title)
    }
});
