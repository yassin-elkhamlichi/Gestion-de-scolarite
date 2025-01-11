from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QTableWidget,
    QTableWidgetItem, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from controllers.module_controller import ModuleMethods  # Import your ModuleMethods class


class ModuleView(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Gestion des Modules")
        self.setGeometry(150, 150, 800, 600)
        self.setStyleSheet("background-color: #f8f9fa;")  # Light background for better visibility

        # Initialize the ModuleMethods class
        self.module_methods = ModuleMethods()

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
        title_label = QLabel("Gestion des Modules", self)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 10px;")  # Reduced margin
        layout.addWidget(title_label)

        # Ajouter un Module
        add_label = QLabel("Ajouter un Module:", self)
        add_label.setFont(label_font)
        layout.addWidget(add_label)

        self.add_name_input = QLineEdit(self)
        self.add_name_input.setPlaceholderText("Nom du Module")
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

        # Mettre à Jour un Module
        update_label = QLabel("Mettre à Jour un Module:", self)
        update_label.setFont(label_font)
        layout.addWidget(update_label)

        self.update_id_input = QLineEdit(self)
        self.update_id_input.setPlaceholderText("ID du Module")
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

        # Supprimer un Module
        delete_label = QLabel("Supprimer un Module:", self)
        delete_label.setFont(label_font)
        layout.addWidget(delete_label)

        self.delete_id_input = QLineEdit(self)
        self.delete_id_input.setPlaceholderText("ID du Module")
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
        self.module_table = QTableWidget(self)
        self.module_table.setColumnCount(2)
        self.module_table.setHorizontalHeaderLabels(["ID", "Nom du Module"])
        self.module_table.horizontalHeader().setStretchLastSection(True)
        self.module_table.setStyleSheet("""
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
        layout.addWidget(self.module_table, stretch=1)  # Allocate more space to the table

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
        add_button.clicked.connect(self.add_module)
        update_button.clicked.connect(self.update_module)
        delete_button.clicked.connect(self.delete_module)
        refresh_button.clicked.connect(self.view_modules)

        # Load modules on startup
        self.view_modules()

    def add_module(self):
        """Add a new module to the database."""
        name = self.add_name_input.text()
        if name:
            try:
                self.module_methods.add_module(name)
                self.add_name_input.clear()
                self.view_modules()
                QMessageBox.information(self, "Succès", "Module ajouté avec succès!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de l'ajout du module: {e}")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un nom de module.")

    def update_module(self):
        """Update an existing module in the database."""
        module_id = self.update_id_input.text()
        new_name = self.update_name_input.text()
        if module_id and new_name:
            try:
                self.module_methods.update_module(module_id, new_name)
                self.update_id_input.clear()
                self.update_name_input.clear()
                self.view_modules()
                QMessageBox.information(self, "Succès", "Module mis à jour avec succès!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de la mise à jour du module: {e}")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un ID et un nouveau nom.")

    def delete_module(self):
        """Delete a module from the database."""
        module_id = self.delete_id_input.text()
        if module_id:
            try:
                self.module_methods.delete_module(module_id)
                self.delete_id_input.clear()
                self.view_modules()
                QMessageBox.information(self, "Succès", "Module supprimé avec succès!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de la suppression du module: {e}")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un ID de module.")

    def view_modules(self):
        """Refresh the module table with data from the database."""
        try:
            modules = self.module_methods.get_all_modules()
            self.module_table.setRowCount(0)  # Clear the table
            for row_number, module in enumerate(modules):
                self.module_table.insertRow(row_number)
                self.module_table.setItem(row_number, 0, QTableWidgetItem(str(module[0])))  # ID
                self.module_table.setItem(row_number, 1, QTableWidgetItem(module[1]))  # Name
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors du chargement des modules: {e}")