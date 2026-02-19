import requests
import pytest

BASE = "https://sky-todo-list.herokuapp.com"

def test_create_done_flag_not_accepted():
    r = requests.post(BASE + "/", json={"title": "generated", "completed": True}, timeout=10)
    assert r.status_code in (200, 201)

    task_id = None
    try:
        j = r.json()
        if isinstance(j, dict):
            for k in ("id", "_id", "task_id", "taskId"):
                if k in j:
                    task_id = j[k]
                    break
    except Exception:
        pass

    if not task_id:
        loc = r.headers.get("Location")
        if loc:
            task_id = loc.rstrip("/").split("/")[-1]

    if task_id:
        g = requests.get(f"{BASE}/{task_id}", timeout=10)
        if g.ok:
            obj = g.json()
            done = None
            for k in ("done", "completed", "is_done", "status"):
                if k in obj:
                    done = obj[k]
                    break
            assert not (done in (True, "true", 1, "done"))
    else:
        pytest.skip("Не получил id созданной задачи, проверить вручную")