// 4-payment.test.js
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
  it('Check sendPaymentRequestToApi is logging to console', () => {
    const stub_calculateNumber = sinon
      .stub(Utils, 'calculateNumber')
      .returns(10);
    const spy_console = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);
    stub_calculateNumber.calledWith(100, 20);
    spy_console.calledWith('The total is: 10');
    stub_calculateNumber.returns(10);
    stub_calculateNumber.restore();
    spy_console.restore();
  });
});
