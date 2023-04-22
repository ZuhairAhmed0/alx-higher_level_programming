#!/usr/bin/node

exports.esrever = function (list) {
  const reslist = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reslist.push(list[i]);
  }

  return reslist;
};
