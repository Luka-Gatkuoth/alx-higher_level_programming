#!/usr/bin/node
/*
 * Script that print first argument pass to it
 * */

const args = process.argv;
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
