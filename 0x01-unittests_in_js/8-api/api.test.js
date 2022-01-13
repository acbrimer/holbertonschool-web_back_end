// 8-api/api.test
const expect = require('chai').expect;
const request = require('request');

describe('Test Module for 8-api', () => {
  it('Test index page', (done) => {
    request('http://localhost:7865/', (err, res, body) => {
      // Correct status code?
      expect(res).to.be.not.null;
      expect(res.statusCode).to.equal(200);
      // Correct result?
      expect(err).to.be.null;
      expect(body).to.be.not.null;
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
