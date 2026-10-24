!/usr/bin/node
/*
    Print a square of a given size with '#'
*/

if (process.argv.length <= 2) {
    console.log("Missing size");
    console.log("Usage: ./1-print_square.js <size>");
    process.exit(1);
}

const size = parseInt(process.argv[2], 10);

for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
        row += '#';
    }
    console.log(row);
}
