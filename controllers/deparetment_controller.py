import sqlite3

class DepartmentMethods:
    def __init__(self, db_path="scolarite.db"):
        self.db_path = db_path

    def connect(self):
        """Establish a connection to the SQLite database."""
        return sqlite3.connect(self.db_path)

    def add_department(self, name):
        """Add a new department to the Department table."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Department (Department_name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    def delete_department(self, department_id):
        """Delete a department by its ID."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Department WHERE Id = ?", (department_id,))
        conn.commit()
        conn.close()

    def get_all_departments(self):
        """Retrieve all departments from the Department table."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Department")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def update_department(self, department_id, new_name):
        """Update a department's name by its ID."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE Department SET Department_name = ? WHERE Id = ?", (new_name, department_id))
        conn.commit()
        conn.close()
