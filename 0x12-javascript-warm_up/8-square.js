#!/usr/bin/node
const arg1 = process.argv.slice(2)[0];
const intVal = parseInt(arg1);
if (isNaN(intVal)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < intVal; i++) {
    console.log('X'.repeat(intVal));
  }
}
