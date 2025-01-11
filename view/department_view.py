from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QTableWidget,
    QTableWidgetItem, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from controllers.deparetment_controller import DepartmentMethods  # Import your DepartmentMethods class


class DepartmentView(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Gestion des Départements")
        self.setGeometry(150, 150, 800, 600)
        self.setStyleSheet("background-color: #f8f9fa;")  # Light background for better visibility

        # Initialize the DepartmentMethods class
        self.department_methods = DepartmentMethods()

        # Central Widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(10)  # Reduced spacing between widgets

        # Fonts
        title_font = QFont("Helvetica", 18, QFont.Bold)
        label_font = QFont("Helvetica", 12)

        # Title
        title_label = QLabel("Gestion des Départements", self)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 10px;")  # Reduced margin
        layout.addWidget(title_label)

        # Ajouter un Département
        add_label = QLabel("Ajouter un Département:", self)
        add_label.setFont(label_font)
        layout.addWidget(add_label)

        self.add_name_input = QLineEdit(self)
        self.add_name_input.setPlaceholderText("Nom du Département")
        self.add_name_input.setStyleSheet("padding: 5px; border: 1px solid #bdc3c7; border-radius: 4px;")
        layout.addWidget(self.add_name_input)

        add_button = QPushButton("Ajouter", self)
        add_button.setStyleSheet("""
            background-color: #28a745; 
            color: #ffffff; 
            padding: 8px 12px; 
            border-radius: 4px;
        """)
        layout.addWidget(add_button)

        # Mettre à Jour un Département
        update_label = QLabel("Mettre à Jour un Département:", self)
        update_label.setFont(label_font)
        layout.addWidget(update_label)

        self.update_id_input = QLineEdit(self)
        self.update_id_input.setPlaceholderText("ID du Département")
        self.update_id_input.setStyleSheet("padding: 5px; border: 1px solid #bdc3c7; border-radius: 4px;")
        layout.addWidget(self.update_id_input)

        self.update_name_input = QLineEdit(self)
        self.update_name_input.setPlaceholderText("Nouveau Nom")
        self.update_name_input.setStyleSheet("padding: 5px; border: 1px solid #bdc3c7; border-radius: 4px;")
        layout.addWidget(self.update_name_input)

        update_button = QPushButton("Mettre à Jour", self)
        update_button.setStyleSheet("""
            background-color: #007bff; 
            color: #ffffff; 
            padding: 8px 12px; 
            border-radius: 4px;
        """)
        layout.addWidget(update_button)

        # Supprimer un Département
        delete_label = QLabel("Supprimer un Département:", self)
        delete_label.setFont(label_font)
        layout.addWidget(delete_label)

        self.delete_id_input = QLineEdit(self)
        self.delete_id_input.setPlaceholderText("ID du Département")
        self.delete_id_input.setStyleSheet("padding: 5px; border: 1px solid #bdc3c7; border-radius: 4px;")
        layout.addWidget(self.delete_id_input)

        delete_button = QPushButton("Supprimer", self)
        delete_button.setStyleSheet("""
            background-color: #dc3545; 
            color: #ffffff; 
            padding: 8px 12px; 
            border-radius: 4px;
        """)
        layout.addWidget(delete_button)

        # Table
        self.department_table = QTableWidget(self)
        self.department_table.setColumnCount(2)
        self.department_table.setHorizontalHeaderLabels(["ID", "Nom du Département"])
        self.department_table.horizontalHeader().setStretchLastSection(True)
        self.department_table.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                border: 1px solid #bdc3c7;
                gridline-color: #dcdde1;
            }
            QHeaderView::section {
                background-color: #2c3e50;
                color: white;
                font-weight: bold;
                padding: 4px;
            }
            QTableWidget::item {
                padding: 10px;
            }
        """)
        layout.addWidget(self.department_table, stretch=1)  # Allocate more space to the table

        # Refresh Button
        refresh_button = QPushButton("Rafraîchir la Liste", self)
        refresh_button.setStyleSheet("""
            background-color: #17a2b8; 
            color: #ffffff; 
            padding: 8px 12px; 
            border-radius: 4px;
        """)
        layout.addWidget(refresh_button)

        # Connect buttons to their functions
        add_button.clicked.connect(self.add_department)
        update_button.clicked.connect(self.update_department)
        delete_button.clicked.connect(self.delete_department)
        refresh_button.clicked.connect(self.refresh_table)

        # Load departments on startup
        self.refresh_table()

    def add_department(self):
        """Add a new department to the database."""
        name = self.add_name_input.text()
        if name:
            try:
                self.department_methods.add_department(name)
                self.add_name_input.clear()
                self.refresh_table()
                QMessageBox.information(self, "Succès", "Département ajouté avec succès!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de l'ajout du département: {e}")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un nom de département.")

    def update_department(self):
        """Update an existing department in the database."""
        department_id = self.update_id_input.text()
        new_name = self.update_name_input.text()
        if department_id and new_name:
            try:
                self.department_methods.update_department(department_id, new_name)
                self.update_id_input.clear()
                self.update_name_input.clear()
                self.refresh_table()
                QMessageBox.information(self, "Succès", "Département mis à jour avec succès!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de la mise à jour du département: {e}")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un ID et un nouveau nom.")

    def delete_department(self):
        """Delete a department from the database."""
        department_id = self.delete_id_input.text()
        if department_id:
            try:
                self.department_methods.delete_department(department_id)
                self.delete_id_input.clear()
                self.refresh_table()
                QMessageBox.information(self, "Succès", "Département supprimé avec succès!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de la suppression du département: {e}")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un ID de département.")

    def refresh_table(self):
        """Refresh the department table with data from the database."""
        try:
            departments = self.department_methods.get_all_departments()
            self.department_table.setRowCount(0)  # Clear the table
            for row_number, department in enumerate(departments):
                self.department_table.insertRow(row_number)
                self.department_table.setItem(row_number, 0, QTableWidgetItem(str(department[0])))  # ID
                self.department_table.setItem(row_number, 1, QTableWidgetItem(department[1]))  # Name
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors du chargement des départements: {e}")