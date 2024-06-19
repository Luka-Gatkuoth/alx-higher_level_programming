#!/usr/bin/node
/* JavaScript that convert the input argument into an integer */

const args = process.argv[2];
if (args === undefined || isNaN(parseInt(args))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${args}`);
}
