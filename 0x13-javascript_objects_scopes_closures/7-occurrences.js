#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter(El => El == searchElement).length;
};
