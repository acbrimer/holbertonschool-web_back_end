// log initial message
console.log('Welcome to Holberton School, what is your name?');
// read from stdin
process.stdin.on('readable', () => {
  const name = process.stdin.read();
  if (name !== null) {
    process.stdout.write(`Your name is: ${name}`);
    // log close message
    console.log('This important software is now closing');
  }
});
