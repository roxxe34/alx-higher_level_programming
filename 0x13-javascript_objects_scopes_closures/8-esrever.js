#!/usr/bin/node
exports.esrever = function (list){
  let new_l = [];
  for (let i = list.length - 1; i >= 0 ; i--){
    new_l.push(list[i]);
  }
  return new_l
}