#!/usr/bin/node

const count = process.argv.length;
switch (count) {
    
    case 2:
    console.log('No argument');
    break;

    case 3:
    console.log('Argument found');
    break;

    default:
    console.log('Arguments found');
}
