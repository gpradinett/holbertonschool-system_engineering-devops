#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the CSV format.
Requirements:
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
API que usamos: https://jsonplaceholder.typicode.com/
Info CSV: https://www.pythontutorial.net/python-basics/python-write-csv-file/
Info flag para agregar comillas usando el modulo csv:
https://www.adamsmith.haus/python/examples/3278/csv-write-to-a-csv-file-and-
quote-all-fields
"""
import csv
from requests import get
from sys import argv


if __name__ == '__main__':
    tasks = []
    tasks_list = []
    root = 'https://jsonplaceholder.typicode.com'
    user = get(root + '/users/{}'.format(argv[1])).json()
    for i in get(root + '/todos').json():
        if i.get('userId') == int(argv[1]):
            tasks.append(argv[1])
            tasks.append(user.get('username'))
            tasks.append(i.get('completed'))
            tasks.append(i.get('title'))
            tasks_list.append(tasks)
            tasks = []
    with open('{}.csv'.format(argv[1]), 'w') as f:
        f_csv = csv.writer(f, quoting=csv.QUOTE_ALL)
        f_csv.writerows(tasks_list)
