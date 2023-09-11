#!/usr/bin/node
const arg1 = process.argv.slice(2);
const intVal = parseInt(arg1);
if (!isNaN(intVal)){
    for (let i = 0; i < intVal; i++){
        console.log("C is fun");
    }
}
else {
    console.log("Missing number of occurrences")
}
