import requests

base_url = 'http://5.101.50.27:8000'

def get_company_list(params_to_add = None):
    resp = requests.get(base_url + '/company/list', params=params_to_add)  # Список всех компаний
    return resp.json()

def get_token(user = 'harrypotter', password = 'expelliarmus'):
    creds = {
        'username': user,
        'password': password
        }
    resp = requests.post(base_url+'/auth/login', json=creds)
    return resp.json()["user_token"]

def create_company(name, description=""):
    company = {
            "name": name,
            "description": description
        }
    resp = requests.post(base_url+'/company/create', json=company)
    return resp.json()

def get_company(id):
    resp = requests.get(base_url + '/company/'+str(id))
    return resp.json()

def edit_company(new_id, new_name, new_descr):
    # Получаем токен
    client_token = get_token()

    # Формируем URL с параметром client_token
    url_with_token = f"{base_url}/company/update/{new_id}?client_token={client_token}"

    # Вызываем словарь и кладем в него описание компании
    company = {
        "name": new_name,  # Новое имя компании
        "description": new_descr  # Новое описание компании
    }

    # Метод отправляет запрос по URL, передает заголовки и тело
    resp = requests.patch(url_with_token, json=company)

    # Результат вернется в JSON, мы его прокинем в тест
    return resp.json()

def delete_company(id):
    client_token = get_token()

    # Формируем URL с параметром client_token
    url_with_token = f"{base_url}/company/{id}?client_token={client_token}"

    # Метод отправляет DELETE-запрос
    resp = requests.delete(url_with_token)

    # Возвращаем JSON-ответ
    return resp.json()

def set_active_state(id, is_active):
    client_token = get_token()

    url_with_token = f"{base_url}/company/status_update/{id}?client_token={client_token}"
    resp = requests.patch(url_with_token, json={"is_active": is_active})
    return resp.json()

def test_get_companies():
    #1. Список всех компаний
    body = get_company_list()
    assert len(body) > 0

def test_get_active_companies():
    #1. Список всех компаний
    full_list = get_company_list()

    #2. Список активных компаний
    filtered_list = get_company_list(params_to_add={'active': 'true'})

    #3. Проверяем что списки не равны
    assert len(full_list) > len(filtered_list)

def test_add_new():
    #1. Получение колисчества компаний
    body = get_company_list()
    len_before = len(body)

    #2. создать новую компанию
    name = "Autotest-Pacharm"
    descr = "Descr"
    result = create_company(name, descr)
    new_id = result["id"]

    #3. количество компаний после создания
    body = get_company_list()
    len_after = len(body)

    #4. проверить что увеличилось на +1
    assert len_after - len_before == 1
    #5. проверить название и описание последней компании в списке соответствует ответу из шага 2
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == new_id

def test_get_one_company():
    name = "Autocreate Company"
    descr = "Privet"
    result = create_company(name, descr)
    new_id = result["id"]

    new_company = get_company(new_id)
    assert new_company["id"] == new_id
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] == True

def test_edit():
    name = "Edit Company"
    descr = "New info"
    result = create_company(name, descr)
    new_id = result["id"]

    new_name = "Updated"
    new_descr = "_upd_"
    edited = edit_company(new_id, new_name, new_descr)

    assert edited["name"] == new_name
    assert edited["description"] == new_descr

def test_delete():
    name = "Company to be deleted"
    descr = "Delete me"
    result = create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = get_company(new_id)
    # Проверим название, описание и статус компании:
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

    # Получаем список компаний и сохраняем его длину
    body = get_company_list()
    len_before = len(body)

    # Удаляем компанию
    delete_company(new_id)

    # Проверяем, что список компаний меньше на 1
    body = get_company_list()
    len_after = len(body)
    assert len_before - len_after == 1

    # Проверяем, что удаленная компания не находится по id
    deleted = get_company(new_id)
    assert deleted['detail'] == 'Компания не найдена'

def test_deactivate():
    # Создаем компанию
    name = "Company to be deactivated"
    result = create_company(name)
    new_id = result["id"]
    # Деактивируем компанию
    body = set_active_state(new_id, False)

    # Проверяем, что у компании статус «неактивная»
    assert body["is_active"] is False

def test_deactivate_and_activate_back():
    #Создаем компанию:
    name = "Company to be deactivated"
    result = create_company(name)
    new_id = result["id"]

    # Деактивируем компанию с помощью параметра False
    body_d = set_active_state(new_id, False)
    # Проверяем, что компания не активная
    assert body_d["is_active"] is False

    # Активируем компанию с помощью параметра True
    body_a = set_active_state(new_id, True)
    # Проверяем, что компания активная
    assert body_a["is_active"] is True