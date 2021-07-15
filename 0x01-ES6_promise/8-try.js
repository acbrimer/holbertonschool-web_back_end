export default function divideFunction(numerator, denominator) {
  try {
    return denominator / numerator;
  } catch (err) {
    return 'cannot divide by 0';
  }
}
