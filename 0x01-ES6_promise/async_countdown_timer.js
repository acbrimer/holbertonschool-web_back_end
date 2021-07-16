function countdown(start = 10) {
  // returns promise that counts down from start and return message
  return new Promise((resolve) => {
    let counter = start;
    // JS builtin for "do a thing every n milliseconds"
    // setInterval(<callback function>, <milliseconds>)
    const timer = setInterval(() => {
      // inside of function that gets called every n milliseconds
      console.log(counter);
      counter -= 1;
      // if counter is 0, call clearInterval to break out of setInterval loop
      if (counter === 0) {
        clearInterval(timer);
        // resolve promise to return data after countdown finishes
        resolve('Blast off!');
      }
      // call function in first arg of setInterval every 1000ms (1s)
    }, 1000);
  });
}

async function runCountdownAsync() {
  // in async context, we can wait for a promise to resolve before moving on
  const countdownResult = await countdown(10);
  // don't log countdownResult until countdown() has called resolve
  console.log(`Countdown returned: ${countdownResult}`);
}

// calling async function from synchronous context returns a Promise
const runCountdownPromise = runCountdownAsync();
// keep doing other stuff while runCountdownPromise does it's thing
console.log('Called runCountdownAsync()');
// runCountdownPromise logs Promise { <pending> } b/c it's still running
console.log(runCountdownPromise);
// hit the end of the script before Promise resolves
// async context still exists until Promise resolves
console.log('Hello from the last line of this script!');
