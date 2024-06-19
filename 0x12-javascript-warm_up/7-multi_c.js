#!/usr/bin/node

/* Script that print string of text as muliple of provided positive integer argument */

const args = process.argv[2];

if (args > 0) {
  function iLoveC (text, args) {
    for (let i = 0; i < args; i++) {
      console.log(text);
    }
  }
  iLoveC('C is fun', args);
} else if (args === undefined) {
  console.log('Missing number of occurences');
}
