#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (previous, current) {
    previous.push(current);
    return previous;
  }, []);
};
