#!/usr/bin/node
/* node is always the first argument */
if (process.argv[2] !== undefined) {
  if (process.argv[3] !== undefined) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
} else {
  console.log('No argument');
}
