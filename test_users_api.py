import requests
import json
import faker

faker = faker.Faker()

base_url = "https://reqres.in"


def test_get_test():
    url = base_url + "/api/users"
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    # print("GET ENDPOINT response is: ", json_str)


def test_create_user():
    random_email = faker.email()
    url = base_url + "/api/users"
    headers = {"Content-Type": "application/json"}
    request_body = {
        "name": random_email,
        "job": "QA"
    }
    response = requests.post(url, json=request_body, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("POST ENDPOINT response is: ", json_str)
    assert "name" in json_data
    assert json_data["job"] == "QA"
    user_id = json_data["id"]
    return user_id

def test_delete_user(id):
    url = base_url + f"/api/users/{id}"
    response = requests.delete(url)
    assert response.status_code == 204
    print(f" user with id {id} deleted")


# call tests
user_id = test_create_user()
test_delete_user(user_id)
test_get_test()
