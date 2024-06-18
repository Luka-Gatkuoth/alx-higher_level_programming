#!/usr/bin/node
/* Script that take argument from user and print it */
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No argument');
  process.exit(1);
}
const userInput = args[0];
console.log(userInput);
