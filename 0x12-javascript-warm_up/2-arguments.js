#!/usr/bin/node
const { argv } = require('node:process');
let noArgs = argv.length;
console.log(noArgs === 2 ? 'No argument' : noArgs == 3 ? 'Argument found' : 'Arguments found');
