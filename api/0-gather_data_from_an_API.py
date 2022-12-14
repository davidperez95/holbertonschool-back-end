#!/usr/bin/python3
"""
This python script returns information about his/her to do list progress.
using https://jsonplaceholder.typicode.com/ as a REST API
    parameters: employee ID (int)
"""

import requests
from sys import argv


if __name__ == '__main__':

    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(api_url, employee_id)
    tasks_url = '{}/todos'.format(user_url)
    
    name_response = requests.get(user_url).json()

    employee_name = name_response.get('name')

    task_response = requests.get(tasks_url).json()

    total_tasks = len(task_response)

    non_competed = sum([elem['completed'] is False for elem in task_response])

    task_completed = total_tasks - non_competed

    output = 'Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                            task_completed,
                                                            total_tasks)
    print(output)

    for task in task_response:
        if task.get('completed') is True:
            print('\t', task.get('title'))

