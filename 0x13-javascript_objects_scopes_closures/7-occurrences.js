#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const size = list.filter(El => El === searchElement).length;

  return size;
};
