// 2-calcul.test.js
const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('Test Module 2-calcul_chai', () => {
  it('apply `type` math function to `a` and `b`', () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
});
