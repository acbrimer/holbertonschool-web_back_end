// 1-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('Test Module 1-calcul', () => {
  it('apply `type` math function to `a` and `b`', () => {
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
