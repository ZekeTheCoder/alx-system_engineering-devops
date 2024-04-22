#!/usr/bin/python3
"""
A Python script that uses a given REST API, for a given employee ID,
returns information about his/her TODO list progress
and exports the data in JSON format.
"""

import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users"
    url = user_url + "/" + employee_id

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    employee_dict = {employee_id: []}
    for task in tasks:
        employee_dict[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    with open('{}.json'.format(employee_id), 'w') as file:
        json.dump(employee_dict, file)
