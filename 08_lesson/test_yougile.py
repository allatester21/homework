import requests


base_url = 'https://yougile.com'
token = ''


def get_pojects_list():
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + token
    }
    resp = requests.get(base_url + '/api-v2/projects', headers=headers)  # Список всех компаний
    return resp.json()


def create_projects(title):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + token
    }

    project = {"title": title}

    resp = requests.post(base_url + '/api-v2/projects', headers=headers, json=project)
    return resp.json()


def edit_project(new_id, title):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + token
    }

    project = {"title": title}

    requests.put(base_url + '/api-v2/projects/' + new_id, headers=headers, json=project)
    result = requests.get(base_url + '/api-v2/projects/' + new_id, headers=headers)
    return result.json()


def get_project_id(new_id):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + token
    }

    result = requests.get(base_url + '/api-v2/projects/' + new_id, headers=headers)
    return result.json()


def test_get_companies_positive():
    # Список всех компаний
    body = get_pojects_list()
    assert len(body) > 0


def test_create_project_positive():
    body = get_pojects_list()
    len_before = body["paging"]["count"]

    # создать проект
    title = "Project QA"
    result = create_projects(title)
    new_id = result["id"]

    body = get_pojects_list()
    len_after = body["paging"]["count"]

    assert len_after - len_before == 1
    assert body['content'][-1]["id"] == new_id


def test_edit_project_positive():
    title = "QA Project"    # создаем проект
    result = create_projects(title)
    new_id = result["id"]

    new_title = "Служба поддержки QA"    # меняем название проекта
    edited = edit_project(new_id, new_title)

    assert edited['title'] == new_title   # проверяем что название изменилось


def test_poject_id_positive():
    title = "Автоматизация тестирования"    # создаем проект
    result = create_projects(title)
    new_id = result["id"]

    project = get_project_id(new_id)

    assert project["id"] == new_id
    assert project["title"] == title


def test_get_companies_negative():
    # Список всех компаний
    body = get_pojects_list()
    assert not len(body) == 1


def test_create_project_negative():
    body = get_pojects_list()
    len_before = body["paging"]["count"]

    # создать проект
    title = "Project QA"
    result = create_projects(title)
    new_id = result["id"]

    body = get_pojects_list()
    len_after = body["paging"]["count"]

    assert not len_after - len_before == 0
    assert body['content'][-1]["id"] == new_id


def test_edit_project_negative():
    title = "QA Project"    # создаем проект
    result = create_projects(title)
    new_id = result["id"]

    new_title = "Служба поддержки QA"    # меняем название проекта
    edited = edit_project(new_id, new_title)

    assert not edited['title'] == title   # проверяем что название изменилось


def test_poject_id_negative():
    title = "Автоматизация тестирования"    # создаем проект
    result = create_projects(title)
    new_id = result["id"]

    project = get_project_id(new_id)

    assert not len(project) == 0
    assert project["title"] == title
