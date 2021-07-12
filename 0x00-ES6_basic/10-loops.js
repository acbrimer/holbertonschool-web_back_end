export default function appendToEachArrayValue(array, appendString) {
  if (array && array.length > 0) {
    for (const idx of array) {
      const value = array[idx];
      // eslint-disable-next-line no-param-reassign
      array[idx] = appendString + value;
    }
  }
  return array;
}
