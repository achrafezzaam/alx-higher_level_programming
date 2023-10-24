#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const tasks = JSON.parse(body);
    const finished = {};
    for (const elem in tasks) {
      const task = tasks[elem];
      if (task.completed === true) {
        if (finished[task.userId] === undefined) {
          finished[task.userId] = 1;
        } else {
          finished[task.userId]++;
        }
      }
    }
    console.log(finished);
  }
});
