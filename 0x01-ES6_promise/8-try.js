export default function divideFunction(numerator, denominator) {
  try {
    return numerator / denominator;
  } catch (err) {
    return 'cannot divide by 0';
  }
}
