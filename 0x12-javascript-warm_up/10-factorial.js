#!/usr/bin/node
/* Script that print the factorial of the input argument using reursion */

const number = process.argv[2];
const n = parseInt(number);

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(n));
