#!/usr/bin/node

const size = process.argv[2];
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let x = '';
    for (let j = 0; j < size; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
