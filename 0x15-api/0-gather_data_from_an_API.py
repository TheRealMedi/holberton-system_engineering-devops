#!/usr/bin/python3
"""Returns information about a employee with a given ID"""
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/'
    todos_url = 'https://jsonplaceholder.typicode.com/todos/'

    users = requests.get('{}{}'.format(url, employee_id)).json()
    todos = requests.get('{}{}'.format(todos_url, employee_id)).json()
    done = [task.get('title') for task in todos
                 if task.get('completed') is True]

    
    print('Employee {} is done with tasks({}/{}):'
          .format(users['name'], len(done), len(todos)))
    for title in done:
        print('\t {}'.format(title))
