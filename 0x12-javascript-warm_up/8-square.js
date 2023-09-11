#!/usr/bin/node
const arg1 = process.argv.slice(2);
const intVal = parseInt(arg1);
if (!isNaN(intVal)) {
  for (let i = 0; i < intVal; i++) {
    let row = '';
    for (let j = 0; j < intVal; j++) {
      row += 'x';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
