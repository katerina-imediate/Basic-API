
import requests
import unittest

BASE_URL= "http://localhost:5000"


class MyTest(unittest.TestCase):

    def test_requests(self):

## Post request test
        user = {
        "id": 15,
        "email": "trst@test.com",
        "name": "Kat",
        "address": "This is the data we created."
}
        BASE_URL= "http://127.0.0.1:5000"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(BASE_URL  + "/users", json=user, headers=headers)

        self.assertEqual(response.status_code, 200, "Unexpected status code")
        print(response.status_code, response.text)

## Get all userstest
        invalid_idresponse = requests.get(BASE_URL  + "/users")
        self.assertEqual(invalid_idresponse.status_code, 200, "Unexpected status code")
        print(invalid_idresponse.json())

## Not allowed 405 test
        invalid_idresponse = requests.patch(BASE_URL  + "/users/1")
        self.assertEqual(invalid_idresponse.status_code, 405, "Unexpected status code")
        print(invalid_idresponse.status_code, invalid_idresponse.text)

## Put request test
        get_id= requests.get(BASE_URL  + "/users/")
        print(get_id.text)

        update_user={
        "email": "updated@test.com",
        "name": "Update",
        "address": "This is the updated user"
}
        update_response=requests.put(BASE_URL + "/users/1", json=update_user, headers=headers)
        self.assertEqual(update_response.status_code, 200, "Unexpected status code")
        print(update_user)
        print(update_response.text)

## Delete request test
        delete_response=requests.delete(BASE_URL + "/users/3")
        self.assertEqual(delete_response.status_code, 200, "Unexpected status code")
        print(delete_response.text)

## Delete invalid user
        delete_invalid=requests.put(BASE_URL + "/users/4")
        self.assertEqual(delete_invalid.status_code, 404, "Unexpected status code")
        print(delete_invalid.text)


if __name__ == "__main__":
    unittest.main()

