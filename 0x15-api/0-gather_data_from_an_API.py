#!/usr/bin/python3
"""
A Python script that uses a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users"
    url = users_url + "/" + employee_id

    response = requests.get(url)
    EMPLOYEE_NAME = response.json().get('name')

    todos_url = url + "/todos"
    response = requests.get(todos_url)
    tasks = response.json()
    TOTAL_NUMBER_OF_TASKS = len(tasks)

    NUMBER_OF_DONE_TASKS = 0
    tasks_list = []

    for task in tasks:
        if task.get('completed'):
            tasks_list.append(task)
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in tasks_list:
        print("\t {}".format(task.get('title')))
