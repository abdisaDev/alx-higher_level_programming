#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  for (const element of list) {
    revList.unshift(element);
  }
  return revList;
};
