// 9-api/api.test
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
  it('/cart/:id - Correct status code when :id is a number', (done) => {
    const testId = 123;
    request(`http://localhost:7865/cart/${testId}`, (err, res, body) => {
      // Correct status code?
      expect(res).to.be.not.null;
      expect(res.statusCode).to.equal(200);
      // Correct result?
      expect(err).to.be.null;
      expect(body).to.be.not.null;
      expect(body).to.equal(`Payment method for cart ${testId}`);
      done();
    });
  });
  it('/cart/:id - Correct status code when :id is NOT a number (=> 404)', (done) => {
    request('http://localhost:7865/cart/abc', (err, res, body) => {
      // Correct status code?
      expect(res.statusCode).to.equal(404);
      // Correct result?
      expect(err).to.be.not.null;
      expect(body).to.be.null;
      done();
    });
  });
});
