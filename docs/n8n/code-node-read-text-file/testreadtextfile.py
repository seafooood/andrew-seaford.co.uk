# python -m unittest TestReadTextFile.py

import unittest
import base64
from ReadTextFile import process_items

class TestReadTextFile(unittest.TestCase):
    """
    This test suite validates the functionality of the `process_items` function,
    which simulates an n8n code node that reads and processes file content.
    """

    def test_process_items_with_valid_file(self):
        """
        Tests the function with a typical n8n input containing a Base64-encoded
        text file and checks if the output is correctly split into lines.
        """
        # --- 1. Define the input data simulating an n8n node output ---
        # The content of the file to be processed.
        original_content = (
            "#!/bin/sh\n"
            "if [ -d /opt/custom-certificates ]; then\n"
            "  echo \"Trusting custom certificates from /opt/custom-certificates.\"\n"
            "fi\n"
        )
        # Encode the content to Base64 to mimic the n8n binary data format.
        base64_encoded_content = base64.b64encode(original_content.encode('utf-8')).decode('utf-8')

        # The input list, structured exactly as it would be from a "Read/Write Files" node.
        input_items = [
            {
                "binary": {
                    "data": {
                        "fileExtension": "sh",
                        "mimeType": "application/x-sh",
                        "fileName": "test_file.sh",
                        "fileSize": len(base64_encoded_content),
                        "data": base64_encoded_content
                    }
                }
            }
        ]

        # --- 2. Define the expected output ---
        # A list of dictionaries, one for each line of the original content.
        expected_output = [
            {'json': {'line': '#!/bin/sh'}},
            {'json': {'line': 'if [ -d /opt/custom-certificates ]; then'}},
            {'json': {'line': '  echo "Trusting custom certificates from /opt/custom-certificates."'}},
            {'json': {'line': 'fi'}},
            {'json': {'line': ''}}  # The final newline character creates an empty string line.
        ]

        # --- 3. Execute the function and compare the results ---
        actual_output = process_items(input_items)
        self.assertEqual(actual_output, expected_output)

    def test_process_items_with_missing_binary_data(self):
        """
        Tests the function's error handling when the binary property is missing.
        """
        input_items = [{'some_other_key': 'value'}]
        expected_output = [{'json': {'error': 'File content not found in expected binary property structure.'}}]
        actual_output = process_items(input_items)
        self.assertEqual(actual_output, expected_output)

    def test_process_items_with_invalid_base64_string(self):
        """
        Tests the function's error handling for non-decodable Base64 content.
        """
        input_items = [
            {
                "binary": {
                    "data": {
                        "data": "This is not a valid base64 string!"
                    }
                }
            }
        ]
        # The expected output should indicate a decoding error.
        expected_output = [{'json': {'error': "Decoding error: Incorrect padding"}}]
        actual_output = process_items(input_items)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
