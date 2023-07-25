#!/usr/bin/node
/*
 * that script computes the number of tasks completed by user id.
 */

const request = require('request');
const URL = process.argv[2];

request.get(URL, function (err, req, res) {
  if (err) console.error(err);
  const todos = JSON.parse(res);
  const completedTasksByUser = {};
  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });
  console.log(completedTasksByUser);
});
