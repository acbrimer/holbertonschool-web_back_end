// 6-payment_token.test
const getPaymentTokenFromAPI = require('./6-payment_token');
const expect = require('chai').expect;

describe('Test Module 6-payment_token', () => {
  it('test getPaymentTokenFromAPI', () => {
    getPaymentTokenFromAPI(true).then((res) => {
      expect(res.data).to.equal('Successful response from the API');
      done();
    });
  });
});
