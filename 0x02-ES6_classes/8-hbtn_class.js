export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  toString() {
    return this.location;
  }

  valueOf() {
    return this.size;
  }

  get size() {
    return this._size;
  }

  set size(value) {
    this._size = value;
  }

  get location() {
    return this._location;
  }

  set location(value) {
    this._location = value;
  }
}
