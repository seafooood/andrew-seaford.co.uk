import sqlite3

class database_extensions():
    def __init__(self, db):
        self.databaseFileName = db

    def fetchAll(self, sql):
        """Fetch all of the records from the database"""
        conn = sqlite3.connect(self.databaseFileName)
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()  
        conn.close() 
        return records   

    def fetchSingleValue(self, sql):
        """Fetch one single value from the database"""
        records = self.fetchAll(sql)  

        if not records and len(records) == 0: 
            raise Exception("No record found")
                
        if len(records) > 1: 
            raise Exception("More than one record found")

        return records[0][0]   

    def execute(self, sql):
        """Execute an sql command that will not return any records"""
        conn = sqlite3.connect(self.databaseFileName)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()