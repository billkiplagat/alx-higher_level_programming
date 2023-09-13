#!/usr/bin/node
function computeFactorial (number) {
  if (isNaN(number) || number < 0) {
    return 1;
  }
  if (number === 0) {
    return 1;
  }
  return number * computeFactorial(number - 1);
}

const input = process.argv[2];
const number = parseInt(input, 10);

const factorial = computeFactorial(number);

console.log(`${factorial}`);
