export default class Currency {
  constructor(code, name) {
    this._name = name;
    this._code = code;
  }

  get _name() {
    return this._name;
  }

  set _name(newName) {
    this._name = newName;
  }

  get _code() {
    return this._code;
  }

  set _code(newCode) {
    this._code = newCode;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
