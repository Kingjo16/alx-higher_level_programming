#!/usr/bin/node

const req = require('request');

req.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const taskscom = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!taskscom[todo.userId]) {
        taskscom[todo.userId] = 1;
      } else {
        taskscom[todo.userId] += 1;
      }
    }
  });
  console.log(taskscom);
});
