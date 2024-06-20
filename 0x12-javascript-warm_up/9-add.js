#!/usr/bin/node

/* Script that print the addition of two integer */

const num1 = process.argv[2];
const num2 = process.argv[3];
const a = parseInt(num1);
const b = parseInt(num2);

function add (a, b) {
  console.log(a + b);
}
add(a, b);
