import unittest
import json
from endPointGet import *

class SystemSettingsTestCase(unittest.TestCase):
    def setUp(self):
        """Set up for unit tests, function is executed before tests begin"""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_get_setting(self):
        """Test confirms that GET /Setting/{sname} will return a setting value"""

        # Arrange
        expected_result = 'Value1'

        # Act
        response = self.client.get('/Setting/Setting1') # Make a GET request to the /Setting/{sname} endpoint
        
        # Assert
        self.assertEqual(response.status_code, 200) # Check that the response status code is 200 OK
        actual_result = json.loads(response.data) # Parse the JSON response
        self.assertEqual(actual_result, expected_result) # Check that the response contains the expected data

    def test_get_setting_bad_setting_name(self):
        """Test confirms that GET /Setting/{sname} will return 400 when the setting name does not exisit"""

        # Arrange
        sname = 'Bad_Setting_Name'
        expected_message = f'Invalid setting name. {sname} does not exist'

        # Act
        response = self.client.get(f'/Setting/{sname}') # Make a GET request to the /Settings endpoint
        
        # Assert
        self.assertEqual(response.status_code, 400) # Check that the response status code is 400 BAD
        self.assertEqual(response.status, '400 BAD REQUEST') # Check the response status message        
        response_json = response.get_json() # Extract the JSON data from the response    
        self.assertIn('message', response_json) # Ensure the 'message' key is in the response
        self.assertEqual(response_json['message'], expected_message) # Check that the response message contains the expected message

if __name__ == '__main__':
    unittest.main()