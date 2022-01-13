// 1-calcul

const calculateNumber = (type, a, b) => {
  // apply `type` math function to `a` and `b`
  const typeFuncs = {
    SUM: (a, b) => Math.round(a) + Math.round(b),
    SUBTRACT: (a, b) => Math.round(a) - Math.round(b),
    DIVIDE: (a, b) =>
      Math.round(b) === 0 ? 'Error' : Math.round(a) / Math.round(b),
  };

  return typeFuncs[type](a, b);
};

module.exports = calculateNumber;
