import requests

def add_task():
    body = {"title":"generated","completed":False}
    response = requests.post("https://sky-todo-list.herokuapp.com/", json=body)
    id = response.json()["id"]

    response = requests.delete(f'https://sky-todo-list.herokuapp.com/{id}')
    response = requests.get(f"https://sky-todo-list.herokuapp.com/{id}")
    assert response.status_code == 404
    
