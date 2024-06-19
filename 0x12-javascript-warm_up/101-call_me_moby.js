#!/usr/bin/node
const callMeMoby = function (times, callBack) {
  for (let i = 0; i < times; i++) {
    callBack();
  }
};

exports.callMeMoby = callMeMoby;
