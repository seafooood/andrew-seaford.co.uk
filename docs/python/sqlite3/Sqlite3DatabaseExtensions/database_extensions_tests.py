import unittest
import tempfile
import sqlite3
import os
from database_extensions import database_extensions

class database_extensions_tests(unittest.TestCase):
    def setUp(self):
        """Set up for unit tests, function is executed before tests begin"""

        # Create a temporary file to use as a test database
        self.db_fd, self.db_path = tempfile.mkstemp()

        # Initialize the database with the test schema and data
        self.init_db()

    def tearDown(self):
        """Tear down for unit tests, function is executed after tests have been executed"""

        # Close and remove the temporary database
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def init_db(self):
        """Initialize the database with the test schema and data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE Settings (Sname TEXT, Svalue TEXT)')
        cursor.execute('INSERT INTO Settings (Sname, Svalue) VALUES (?, ?)', ('Setting1', 'Value1'))
        cursor.execute('INSERT INTO Settings (Sname, Svalue) VALUES (?, ?)', ('Setting2', 'Value2'))
        conn.commit()
        conn.close()

    def test_fetchAll(self):
        """Test confirms that FetchAll will return a list of all the system settings"""

        # Arrange 
        expected_result = [
            ('Setting1', 'Value1'),
            ('Setting2', 'Value2')
        ]
        systemUnderTest = database_extensions(self.db_path)

        # Act
        actual_result = systemUnderTest.fetchAll('SELECT Sname, Svalue FROM `Settings` ORDER BY Sname ASC')

        # Assert      
        self.assertEqual(actual_result, expected_result) 
    
    def test_fetchSingleValue(self):
        """Test confirms that fetchSingleValue will return a single system setting value"""

        # Arrange 
        expected_result = 'Value1'
        systemUnderTest = database_extensions(self.db_path)

        # Act
        actual_result = systemUnderTest.fetchSingleValue("SELECT Svalue FROM `Settings` where Sname='Setting1'")

        # Assert      
        self.assertEqual(actual_result, expected_result) 
    
    def test_fetchSingleValue_no_record_found(self):
        """Test confirms that fetchSingleValue raise exception when the value is not found"""

        # Arrange 
        systemUnderTest = database_extensions(self.db_path)

        # Act and Assert
        with self.assertRaises(Exception) as context:
            systemUnderTest.fetchSingleValue("SELECT Svalue FROM `Settings` where Sname='bad'")        
        self.assertEqual(str(context.exception), "No record found") # Assert that the exception message is "No record found"
    
    def test_fetchSingleValue_too_many_records_found(self):
        """Test confirms that fetchSingleValue raise exception when too many records are found"""

        # Arrange 
        systemUnderTest = database_extensions(self.db_path)

        # Act and Assert
        with self.assertRaises(Exception) as context:
            systemUnderTest.fetchSingleValue("SELECT Svalue FROM `Settings`")        
        self.assertEqual(str(context.exception), "More than one record found") # Assert that the exception message is "More than one record found"
    
    def test_execute(self):
        """Text confirms that execute can insert a record"""

        # Arrange 
        sname = 'Setting5'
        svalue = 'Value5'
        expected_result = [
            ('Setting1', 'Value1'),
            ('Setting2', 'Value2'),
            (sname, svalue)
        ]
        systemUnderTest = database_extensions(self.db_path)

        # Act
        systemUnderTest.execute(f"INSERT INTO `Settings` (Sname, Svalue) VALUES ('{sname}', '{svalue}')")

        # Assert
        actual_result = systemUnderTest.fetchAll('SELECT Sname, Svalue FROM `Settings` ORDER BY Sname ASC')
        self.assertEqual(actual_result, expected_result) 

if __name__ == '__main__':
    unittest.main()