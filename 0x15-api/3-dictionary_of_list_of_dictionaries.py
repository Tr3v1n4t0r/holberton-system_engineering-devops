#!/usr/bin/python3
"""
For all employees, export to JSON information about TODO list progress
"""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    all_id = set()
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = req.json()
    for user in data:
        all_id.add(user.get('userId'))

    export = {}
    for user in all_id:
        req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(user))
        username = req.json().get('username')

        req = requests.get('https://jsonplaceholder.typicode.com/' +
                           'todos?userId={}'.format(user))
        data = req.json()

        export['{}'.format(user)] = []
        for task in data:
            export['{}'.format(user)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            })

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump({int(x): export[x] for x in export.keys()},
                  outfile, sort_keys=True)
