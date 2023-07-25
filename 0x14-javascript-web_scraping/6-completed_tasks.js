#!/usr/bin/node
/*
 * that script computes the number of tasks completed by user id.
 */

const request = require('request');
const URL = process.argv[2];

request.get(URL, function (err, req, res) {
  if (err) console.error(err);
  const todos = JSON.parse(res);
  const completed = {};
  todos.forEach((todo) => {
    if (todo.completed && completed[todo.userId] === undefined) {
      completed[todo.userId] = 1;
    } else if (todo.completed) {
      completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});
