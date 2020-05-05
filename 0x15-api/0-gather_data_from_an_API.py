#!/usr/bin/python3
"""
For a given employee ID, return information about TODO list progress
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(argv[1]))
    name = req.json().get('name')

    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    data = req.json()
    done = total = 0
    for task in data:
        total += 1
        if task.get('completed'):
            done += 1

    print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    for task in data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
