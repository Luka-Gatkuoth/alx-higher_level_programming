#!/usr/bin/node

/* Script that find the second biggest number from list of arguments */

const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let second = parseInt(args[2]);
  let biggest = parseInt(args[3]);
  for (let i = 2; i < args.length; i++) {
    const current = parseInt(args[i]);
    if (current > biggest) {
      second = biggest;
      biggest = current;
    } else if ((current > second) && (current < biggest)) {
      second = current;
    }
  }
  console.log(second);
}
