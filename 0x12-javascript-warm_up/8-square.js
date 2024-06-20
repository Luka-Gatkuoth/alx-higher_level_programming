#!/usr/bin/node
/* Script that print string of character as the size quare of input argument */

const args = process.argv[2];

if (parseInt(args) === undefined || isNaN(parseInt(args))) {
  console.log('Missing size');
} else if (parseInt(args) > 0) {
  function printSquare (char, args) {
    for (let i = 0; i < args; i++) {
      let row = '';
      for (let j = 0; j < args; j++) {
        row += char;
      }
      console.log(row);
    }
  }
  printSquare('X', parseInt(args));
}
