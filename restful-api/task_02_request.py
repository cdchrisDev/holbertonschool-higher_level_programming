#!/usr/bin/python3
"""This is the task_02_request
Module
"""
import requests, json


url = 'https://jsonplaceholder.typicode.com/posts'
r = requests.get(url)
urlSuccess = True if r.status_code == 200 else False

def fetch_and_print_posts():
    """A func that fetches post from
    JSONPlaceholder
    """
    print(f"Status Code: {r.status_code}")
    try:
        r.raise_for_status()
    except request.RequestException as e:
        print(f"Failed to get data: {e}")
        return None
    finally:
        print(f"Status Code: {r.status_code}")
        json_data = r.json()
        for post in json_data:
            print(post["title"])
    
"""         
def fetch_and_save_posts():
    A func that fetches all post from
    JSONPlaceholder
    """
     
if __name__ == "__main__":
    fetch_and_print_posts()
    #fetch_and_save_posts()