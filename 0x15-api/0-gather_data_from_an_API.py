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
"""

from requests import get
from sys import argv


if __name__ == '__main__':

    done = 0
    tasks = []
    root = 'https://jsonplaceholder.typicode.com'
    name = get(root + '/users/{}'.format(argv[1])).json().get('name')
    for i in get(root + '/todos').json():
        if i.get('userId') == int(argv[1]):
            tasks.append(i)
            if i.get('completed') is True:
                done += 1
    print("Employee {} is done with tasks({}/{}):".
          format(name, done, len(tasks)))
    for i in tasks:
        if i.get('completed') is True:
            print("\t {}".format(i.get('title')))
