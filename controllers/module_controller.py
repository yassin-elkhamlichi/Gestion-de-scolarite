import sqlite3

class ModuleMethods:
    def __init__(self, db_path="scolarite.db"):
        self.db_path = db_path

    def connect(self):
        """Establish a connection to the SQLite database."""
        return sqlite3.connect(self.db_path)

    def add_module(self, name):
        """Add a new module to the Module table."""
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Module (Module_name) VALUES (?)", (name,))
            conn.commit()
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Error adding module: {e}")
        finally:
            conn.close()

    def delete_module(self, module_id):
        """Delete a module by its ID."""
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Module WHERE id = ?", (module_id,))
            conn.commit()
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Error deleting module: {e}")
        finally:
            conn.close()

    def get_all_modules(self):
        """Retrieve all modules from the Module table."""
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Module")
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Error fetching modules: {e}")
        finally:
            conn.close()

    def update_module(self, module_id, new_name):
        """Update a module's name by its ID."""
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("UPDATE Module SET Module_name = ? WHERE id = ?", (new_name, module_id))
            conn.commit()
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Error updating module: {e}")
        finally:
            conn.close()