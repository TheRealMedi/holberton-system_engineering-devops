#!/usr/bin/python3
"""Returns information about a employee with a given ID"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/'
    todos_url = 'https://jsonplaceholder.typicode.com/todos/'

    users = requests.get('{}{}'.format(url, employee_id)).json()
    todos = requests.get('{}{}'.format(todos_url, employee_id))

    user = users.json().get('username')
    json_repr = todos.json()


    with open('{}.csv'.format(employee_id), 'w') as csv_data:
        csv_writer = csv.writer(
            csv_data,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL
            )

        for task in json_repr:
            if task.get('userId') == employee_id:
                csv_writer.writerow(
                    [
                        task.get('userId'),
                        user,
                        task.get('completed'),
                        task.get('title')])
        csv_data.close()
