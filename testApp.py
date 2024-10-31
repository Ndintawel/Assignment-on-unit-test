# test_app.py
import unittest

#import the instance of the object app from the class app
from app import app

#Defines a new class called testapp
class TestApp(unittest.TestCase):
    def setUp(self):
        #set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        #send a GET response to the '/' route
        response = self.app.get('/')

        #check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        #check that the response JSON match the expected message
        self.assertEqual(response.json, {"message": "Hello level 400 FET, Quality Assurance!"})


if __name__ == '__main__':
    unittest.main()