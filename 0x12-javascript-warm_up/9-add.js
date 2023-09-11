#!/usr/bin/node
if (process.argv.length !== 4) {
  console.log('NaN');
  process.exit(1);
}
const num1 = parseFloat(process.argv[2]);
const num2 = parseFloat(process.argv[3]);
if (isNaN(num1) || isNaN(num2)) {
  console.log('Invalid input. Both arguments must be numbers.');
  process.exit(1);
}
function add (a, b) {
  return a + b;
}
const result = add(num1, num2);
console.log(result);
