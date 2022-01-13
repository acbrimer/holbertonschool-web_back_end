// 4-payment
const Utils = require('./utils');

const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
  // SUM totalAmount + totalShipping using Utils.calculateNumber
  // log 'The total is: <result of the sum>'
  console.log(
    `The total is: ${Utils.calculateNumber('SUM', totalAmount, totalShipping)}`
  );
};

module.exports = sendPaymentRequestToApi;
