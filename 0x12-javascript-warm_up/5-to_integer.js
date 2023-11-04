#!/usr/bin/node
let convert = Number(process.argv[2]);
if (isNaN(convert)) {
  console.log('Not a number');
}
else {
  console.log('My number: ' + convert);
}