#!/usr/bin/python3
"""This is the task_02_request
Module
"""
import requests
import json
import csv
url = 'https://jsonplaceholder.typicode.com/posts'
r = requests.get(url)
urlSuccess = True if r.status_code == 200 else False


def fetch_and_print_posts():
    """A func that fetches post from
    JSONPlaceholder
    """
    try:
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to get data: {e}")
        return None
    finally:
        print(f"Status Code: {r.status_code}")
        json_data = r.json()
        for post in json_data:
            print(post["title"])


def fetch_and_save_posts():
    """A func that fetches all post from
    JSONPlaceholder
    """
    try:
        json_data = r.json()
    except ValueError:
        print("Failed to get data")
        return
    finally:
        csvF = "posts.csv"
        filtered_data = [{key: post[key]
                         for key in ('id',
                         'title', 'body')}
                         for post in json_data]
        headers = ['id', 'title', 'body']

    with open(csvF, 'w', newline="") as F:
        csv_write = csv.DictWriter(F, fieldnames=headers)
        csv_write.writeheader()
        csv_write.writerows(filtered_data)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
