# testapp.py

from app import app  

def test_home():
    
    with app.test_client() as client:
        response = client.get('/')  

        # Check that the response status code is 200 (OK)
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

        # Check that the response data matches the expected JSON structure
        expected_response = {"message": "Hello level 400 FET, Quality Assurance!"}
        assert response.get_json() == expected_response, \
            f"Expected JSON response {expected_response} but got {response.get_json()}"