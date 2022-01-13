// 3-payment.test.js
const sendPaymentRequestToApi = require('./3-payment');
const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils');

describe('Test Module 3-payment', () => {
  it('SUM totalAmount + totalShipping with sendPaymentRequestToApi', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;
    spy.restore();
  });
});
