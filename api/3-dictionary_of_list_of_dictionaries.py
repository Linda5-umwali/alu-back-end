#!/usr/bin/python3
"""
Script that fetches all employees' TODO lists and exports them to JSON.
"""

import json
import requests


def fetch_all_tasks_and_export():
    """
    Fetch all users and their tasks, and export to todo_all_employees.json
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_resp = requests.get(users_url)
    users_resp.raise_for_status()
    users = users_resp.json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        )
        todos_resp = requests.get(todos_url)
        todos_resp.raise_for_status()
        todos = todos_resp.json()

        task_list = [{
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        } for task in todos]

        all_tasks[str(user_id)] = task_list

    with open("todo_all_employees.json", "w", encoding='utf-8') as json_file:
        json.dump(all_tasks, json_file)
        # no indent to match required format exactly


if __name__ == "__main__":
    fetch_all_tasks_and_export()
