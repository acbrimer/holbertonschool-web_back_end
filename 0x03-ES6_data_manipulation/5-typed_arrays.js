export default function createInt8TypedArray(length, position, value) {
  const buff = new ArrayBuffer(length);
  buff[position] = value;
  return new DataView(buff);
}
