// 10-api/api.test
const expect = require('chai').expect;
const request = require('request');

describe('Test Module for 10-api', () => {
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
      expect(body).to.equal(`Payment methods for cart ${testId}`);
      done();
    });
  });
  it('/cart/:id - Correct status code when :id is NOT a number (=> 404)', (done) => {
    request('http://localhost:7865/cart/abc', (err, res, body) => {
      // Correct status code?
      expect(res.statusCode).to.equal(404);
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
  it('/available_payments - Correct object returned', (done) => {
    request('http://localhost:7865/available_payments', (err, res, body) => {
      // Correct status code?
      expect(res.statusCode).to.equal(200);
      // Correct content?
      expect(body).to.be.not.null;
      const obj = JSON.parse(body) || {};
      expect(obj).to.have.keys(['payment_methods']);
      expect(obj.payment_methods).to.have.keys(['credit_cards', 'paypal']);
      done();
    });
  });
  it('POST /login - Correct response with username', (done) => {
    request.post(
      {
        url: 'http://localhost:7865/login',
        json: { userName: 'Betty' },
      },
      (err, res, body) => {
        // Correct status code?
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      }
    );
  });
});
