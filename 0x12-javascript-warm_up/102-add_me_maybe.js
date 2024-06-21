#!/usr/bin/node
/* Function that icreement and call the function */

exports.addMeMaybe = function (number, thFunction) {
  number++;
  thFunction(number);
};
