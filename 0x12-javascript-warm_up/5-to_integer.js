#!/usr/bin/node
if (isNaN(Math.floor(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.floor(process.argv[2]));
}
