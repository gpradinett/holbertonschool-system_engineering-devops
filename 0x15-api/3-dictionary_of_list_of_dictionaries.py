#!/usr/bin/python3
"""
 exports json file with information about all employee progress
"""
from collections import OrderedDict
import json
from requests import get


if __name__ == '__main__':
    task = OrderedDict()
    tasks_list = []
    user_dict = {}
    user_count = 0
    root = 'https://jsonplaceholder.typicode.com'
    user_id = 1
    for i in get(root + '/todos').json():
        if i.get('userId') != user_id:
            tasks_list = []
            user_id = i.get('userId')
        user = get(root + '/users/{}'.format(i.get('userId'))).json()
        task['username'] = user.get('username')
        task["task"] = i.get('title')
        task['completed'] = i.get('completed')
        tasks_list.append(task)
        task = OrderedDict()
        user_dict[i.get('userId')] = tasks_list
    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_dict, f)
