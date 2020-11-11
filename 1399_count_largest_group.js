/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function(n) {
    x = Array.from({length: n}, (_, i) => i + 1).map(item => {
        sod = 0;
        while (item > 0) {
            sod += item % 10;
            item = Math.floor(item / 10);
        }
        // console.log(item)
        return sod;
    })
        .reduce((acc, value) => {
        if (!acc[value]) {
            acc[value] = 0;
        }
        acc[value] += 1;
        return acc;   
    }, []).reduce((acc, value) => {
        if (!acc[value]) {
            acc[value] = 0
        }
        acc[value] += 1;
        return acc;
    }, {});
    indx = Object.keys(x).reduce((a, b) => +a > +b ? a : b, -1)
    return x[indx]
};