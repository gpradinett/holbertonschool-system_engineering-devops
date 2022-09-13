#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.
Requirements:
- Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_
COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
API que usamos: https://jsonplaceholder.typicode.com/
Info write: https://www.w3schools.com/python/python_file_write.asp
Info json.dumpes = https://www.geeksforgeeks.org/json-dumps-in-python/
"""
from collections import OrderedDict
import json
from requests import get
from sys import argv


if __name__ == '__main__':
    task = OrderedDict()
    tasks_list = []
    user_dict = {}
    root = 'https://jsonplaceholder.typicode.com'
    user = get(root + '/users/{}'.format(argv[1])).json()
    for i in get(root + '/todos').json():
        if i.get('userId') == int(argv[1]):
            task["task"] = i.get('title')
            task['completed'] = i.get('completed')
            task['username'] = user.get('username')
            tasks_list.append(task)
            task = OrderedDict()
    user_dict[argv[1]] = tasks_list
    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(user_dict, f)
