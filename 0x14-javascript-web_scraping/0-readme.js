#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', function  (err, data) {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }

    console.log('File content:', data);
});
