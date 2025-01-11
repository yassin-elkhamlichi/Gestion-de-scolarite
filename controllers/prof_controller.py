import sqlite3

class ProfMethods:
    def __init__(self, db_path="scolarite.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def get_department_id_by_name(self, name):
        """Fetch department ID based on department name."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT ID FROM Department WHERE  Department_name = ?", (name,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def add_prof(self, name, prenom, email, date_nais=None, tele=None, adresse=None, department_name=None):
        department_id = self.get_department_id_by_name(department_name)
        if not department_id:
            raise ValueError("Invalid department name")

        conn = self.connect()
        cursor = conn.cursor()
        query = """
            INSERT INTO Prof (Nom, Prenom, Email, DateNais, Tele, Adresse, Department_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (name, prenom, email, date_nais, tele, adresse, department_id))
        conn.commit()
        conn.close()

    def delete_prof(self, prof_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Prof WHERE ID = ?", (prof_id,))
        conn.commit()
        conn.close()

    def get_all_profs(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Prof")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_department_name_by_id(self, department_id):
        """Fetch department name based on department ID."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Department_name FROM Department WHERE ID = ?", (department_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def update_prof(self, prof_id, name, prenom, email, date_nais=None, tele=None, adresse=None, department_name=None):
        department_id = self.get_department_id_by_name(department_name)
        if not department_id:
            raise ValueError("Invalid department name")

        conn = self.connect()
        cursor = conn.cursor()
        query = """
            UPDATE Prof 
            SET Nom = ?, Prenom = ?, Email = ?, DateNais = ?, Tele = ?, Adresse = ?, Department_id = ?
            WHERE ID = ?
        """
        cursor.execute(query, (name, prenom, email, date_nais, tele, adresse, department_id, prof_id))
        conn.commit()
        conn.close()
