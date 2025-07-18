import requests
import unittest

BASE_URL= "http://localhost:5000"


class MyTest(unittest.TestCase):

    def test_requests(self):

## Post request test
        user = {
        "email": "trst@test.com",
        "name": "Kat",
        "address": "This is the data we created.",
        "test": "500 server err"
}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(BASE_URL  + "/users", json=user, headers=headers)

        self.assertEqual(response.status_code, 200, "Unexpected status code")
        print(response.status_code, response.text)

## 500 server error
        user = {
                "email": "500@test.com",
                # "name": "Kat",
                "address": "This is the data we created.",
                "test": "500 server err"
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(BASE_URL  + "/users", json=user, headers=headers)

        self.assertEqual(response.status_code, 500, "Unexpected status code")
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
        update_user = {
        "email": "updated@test.com",
        "name": "Update",
        "address": "This is the updated user",
        "name": "Update_2",
        }

        update_response=requests.put(BASE_URL + "/users/4", json=update_user, headers=headers)
        self.assertEqual(update_response.status_code, 200, "Unexpected status code")
        print(update_user)
        print(update_response.text)

## Delete request test
        delete_response=requests.delete(BASE_URL + "/users/3")
        self.assertEqual(delete_response.status_code, 200, "Unexpected status code")
        print(delete_response.text, delete_response.status_code)

## Get deleted user test 404
        response=requests.get(BASE_URL + "/users/3")
        self.assertEqual(response.status_code, 404, "Incorrect status code")
        print(response.content,  response.status_code)

## 415 Unsupported Media Type error test
        delete_invalid=requests.put(BASE_URL + "/users/1")
        self.assertEqual(delete_invalid.status_code, 415, "Unexpected status code")
        print(delete_invalid.text)

        response=requests.get(BASE_URL + "/users")
        self.assertEqual(response.status_code, 200, "Unexpected status code")
        print(response.text,response.status_code)


if __name__ == "__main__":
    unittest.main()

