#!/usr/bin/python3
"""
A Python script that, using a given REST API, records all tasks
from all employees and exports the data in JSON format.
"""

import json
import requests


if __name__ == '__main__':
    users_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(users_url)
    users = response.json()

    employees_data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_url = '{}/{}'.format(users_url, user_id)

        todo_url = user_url + '/todos/'
        response = requests.get(todo_url)
        tasks = response.json()

        employees_data[user_id] = []

        for task in tasks:
            employees_data[user_id].append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(employees_data, file)
