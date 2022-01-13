// 6-payment_token

const getPaymentTokenFromAPI = async (success) => {
  if (success) {
    return Promise.resolve({ data: 'Successful response from the API' });
  }
};
