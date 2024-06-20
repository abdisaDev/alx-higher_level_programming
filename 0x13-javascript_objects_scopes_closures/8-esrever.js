#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const revList = [];
  for (const element of list) {
    revList.unshift(element);
  }
  return revList;
};
