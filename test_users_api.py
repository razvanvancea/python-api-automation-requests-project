import requests
import json
import faker

faker = faker.Faker()

base_url = "https://reqres.in"


# test cases
def test_get_test():
    url = base_url + "/api/users"
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    # print("GET ENDPOINT response is: ", json_str)


def test_create_user():
    random_first_name = faker.first_name()
    url = base_url + "/api/users"
    headers = {"Content-Type": "application/json"}
    request_body = {
        "name": random_first_name,
        "job": "QA"
    }
    response = requests.post(url, json=request_body, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("POST ENDPOINT response is: ", json_str)
    assert "name" in json_data
    assert json_data["name"] == random_first_name
    assert json_data["job"] == "QA"


def test_delete_user():
    random_first_name = faker.first_name()
    user_id = create_user(random_first_name, "DEV")
    url = base_url + f"/api/users/{user_id}"
    response = requests.delete(url)
    assert response.status_code == 204
    print(f" user with id {user_id} deleted")
    print('the random name is: ' + random_first_name)


# utility functions
def create_user(name, job):
    url = base_url + "/api/users"
    headers = {"Content-Type": "application/json"}
    request_body = {
        "name": name,
        "job": job
    }
    response = requests.post(url, json=request_body, headers=headers)
    json_data = response.json()
    return json_data["id"]


# call tests
test_create_user()
test_delete_user()
test_get_test()
