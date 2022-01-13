// 6-payment_token

const getPaymentTokenFromAPI = async (success) => {
  if (success) {
    return new Promise((resolve) =>
      resolve({ data: 'Successful response from the API' })
    );
  }
};
