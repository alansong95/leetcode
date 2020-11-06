/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
  return [...S].filter(item => {
      if (J.includes(item)) {
          return 1
      } 
  }).length
};

// one line solution
var numJewelsInStones = function(J, S) {
  return [...S].filter(item => J.includes(item)).length
};