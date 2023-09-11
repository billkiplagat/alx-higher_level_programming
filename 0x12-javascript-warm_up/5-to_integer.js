#!/usr/bin/node
const arg1 = process.argv.slice(2);
const intVal = parseInt(arg1);
/* isNaN() is Not-a-Number */ 
if (!isNaN(intVal))
{
    console.log(`My number: ${intVal}`);
} else {
    console.log("Not a number");
}
