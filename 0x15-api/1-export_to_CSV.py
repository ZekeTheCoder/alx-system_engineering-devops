#!/usr/bin/python3
"""
A Python script that uses a given REST API, for a given employee ID,
returns information about his/her TODO list progress
and exports the data in CSV format.
"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users"
    url = users_url + "/" + employee_id

    response = requests.get(url)
    username = response.json().get('username')

    todos_url = url + "/todos"
    response = requests.get(todos_url)
    tasks = response.json()

    with open('{}.csv'.format(employee_id), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(employee_id, username, task.get('completed'),
                            task.get('title')))
