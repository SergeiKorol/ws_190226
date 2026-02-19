import requests

def test_edit():
    """это тест про тест"""
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200
    assert response.json()['title']=="generated-1"
    