// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('Test Module 0-calcul', () => {
  it('rounds and sums two numbers', () => {
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.0, 3.0), 4);
    assert.equal(calculateNumber(1000, 0.1), 1000);
    assert.equal(calculateNumber(1000, 0.5), 1001);
  });
});
