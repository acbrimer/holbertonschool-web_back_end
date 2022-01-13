// 5-payment.test.js
const sendPaymentRequestToApi = require('./3-payment');
const sinon = require('sinon');
const expect = require('chai').expect;
const Utils = require('./utils');

describe('Test Module 3-payment', () => {
  let spy_console;

  beforeEach(() => {
    spy_console = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spy_console.restore();
  });

  it('SUM totalAmount + totalShipping with sendPaymentRequestToApi', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;
    spy.restore();
  });
  it('Check sendPaymentRequestToApi is logging to console', () => {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    sendPaymentRequestToApi(100, 20);
    stub.calledWith(100, 20);
    spy_console.calledWith('The total is: 10');
    stub.returns(10);
    stub.restore();
  });
  it('call sendPaymentRequestToAPI with 100, and 20', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spy_console.calledOnce).to.be.true;
    expect(spy_console.calledWith('The total is: 120')).to.be.true;
  });
  it('call sendPaymentRequestToAPI with 10, and 10', () => {
    sendPaymentRequestToApi(10, 10);
    expect(spy_console.calledOnce).to.be.true;
    expect(spy_console.calledWith('The total is: 20')).to.be.true;
  });
});
