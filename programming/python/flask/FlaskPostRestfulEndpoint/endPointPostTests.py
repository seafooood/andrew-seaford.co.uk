import unittest
import json
from endPointPost import *

class SystemSettingsTestCase(unittest.TestCase):
    def setUp(self):
        """Set up for unit tests, function is executed before tests begin"""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_get_settings(self):
        """Test confirms that GET /Settings will return a list of all the system settings"""

        # Arrange 
        expected_result = [
            {'Name': 'Setting1', 'Value': 'Value1'},
            {'Name': 'Setting2', 'Value': 'Value2'}
        ]

        # Act
        response = self.client.get('/Settings') # Make a GET request to the /Settings endpoint

        # Assert
        self.assertEqual(response.status_code, 200) # Check that the response status code is 200 OK
        actual_result = json.loads(response.data) # Parse the JSON response        
        self.assertEqual(actual_result, expected_result) # Check that the response contains the expected data
    
    def test_post_setting(self):
        """Test confirms that POST /Setting will add a new setting"""
        
        # Arrange 
        expected_result = [
            {'Name': 'Setting1', 'Value': 'Value1'},
            {'Name': 'Setting2', 'Value': 'Value2'},
            {'Name': 'Setting3', 'Value': 'Value3'}
        ]

        # Act
        response = self.client.post('/Setting', json={"Name":"Setting3", "Value":"Value3"}) # Make a POST request to the /Setting endpoint

        # Assert
        print("post response", response)
        self.assertEqual(response.status_code, 201) # Check that the response status code is 201 CREATED
        response = self.client.get('/Settings') # Make a GET request to the /Settings endpoint to get all settings which should include the new setting
        actual_result = json.loads(response.data) # Parse the JSON response        
        self.assertEqual(actual_result, expected_result) # Check that the response contains the old settings and the new setting
    
    def test_post_setting_no_post_data(self):
        """Test confirms that POST /Setting will return 415 when post request does not contain the json data"""
        
        # Arrange 

        # Act
        response = self.client.post('/Setting') # Make a POST request to the /Setting endpoint without json data

        # Assert
        self.assertEqual(response.status_code, 400) # Check that the response status code is 415
        self.assertEqual(response.status, '400 BAD REQUEST') # Check the response status message   

    def test_post_setting_bad_post_data(self):
        """Test confirms that POST /Setting will return 415 when post request contain bad json data"""
        
        # Arrange 
        badJsonData = {'Bad':'bob1'} # Json data should include Name and Value
        expected_message = f'Input payload validation failed'

        # Act
        response = self.client.post('/Setting', json=badJsonData) # Make a POST request to the /Setting endpoint with bad json data

        # Assert
        self.assertEqual(response.status_code, 400) # Check that the response status code is 400
        self.assertEqual(response.status, '400 BAD REQUEST') # Check the response status message        
        response_json = response.get_json() # Extract the JSON data from the response    
        self.assertIn('message', response_json) # Ensure the 'message' key is in the response
        self.assertEqual(response_json['message'], expected_message) # Check that the response message contains the expected message
    
    def test_post_setting_exists_post_data(self):
        """Test confirms that POST /Setting will return 400 when setting already exists"""
        
        # Arrange 
        badJsonData = {"Name":"Setting1", "Value":"Value10"} # Json data contains an already exisiting setting name
        expected_message = f'Setting Setting1 already exists'

        # Act
        response = self.client.post('/Setting', json=badJsonData) # Make a POST request to the /Setting endpoint with json data

        # Assert
        self.assertEqual(response.status_code, 400) # Check that the response status code is 400
        self.assertEqual(response.status, '400 BAD REQUEST') # Check the response status message        
        response_json = response.get_json() # Extract the JSON data from the response    
        self.assertIn('message', response_json) # Ensure the 'message' key is in the response
        self.assertEqual(response_json['message'], expected_message) # Check that the response message contains the expected message
    

if __name__ == '__main__':
    unittest.main()