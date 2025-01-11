import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QTreeWidget, QTreeWidgetItem, QMessageBox, QGroupBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from controllers.prof_controller import ProfMethods


class ProfView(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Gestion des Professeurs")
        self.setGeometry(100, 100, 1000, 600)  # Set window size
        self.setStyleSheet("background-color: #ffffff;")  # White background

        self.prof_methods = ProfMethods()

        # Custom Fonts
        title_font = QFont("Helvetica", 18, QFont.Bold)  # Title font
        label_font = QFont("Helvetica", 12)  # Label font
        button_font = QFont("Helvetica", 10, QFont.Bold)  # Button font

        # Main Widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Title Label
        title_label = QLabel("Gestion des Professeurs")
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #2c3e50;")  # Dark blue text
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Input Frame
        input_frame = QWidget()
        input_layout = QVBoxLayout(input_frame)

        self.entries = {}
        fields = ["name", "prenom", "email", "date_nais", "tele", "adresse", "department_name"]
        labels = ["Nom", "Prénom", "Email", "Date de Naissance", "Téléphone", "Adresse", "Department Name"]

        for field, label in zip(fields, labels):
            row = QHBoxLayout()
            label_widget = QLabel(label)
            label_widget.setFont(label_font)
            label_widget.setStyleSheet("color: #2c3e50;")
            row.addWidget(label_widget)

            entry = QLineEdit()
            entry.setFont(label_font)
            entry.setStyleSheet("background-color: #ecf0f1; color: #2c3e50; border: none;")
            row.addWidget(entry)
            self.entries[field] = entry

            input_layout.addLayout(row)

        main_layout.addWidget(input_frame)

        # Buttons
        button_frame = QWidget()
        button_layout = QHBoxLayout(button_frame)

        self.add_button = QPushButton("Ajouter")
        self.add_button.setFont(button_font)
        self.add_button.setStyleSheet("background-color: green; color: #ffffff; border: none;")
        self.add_button.clicked.connect(self.add_prof)
        button_layout.addWidget(self.add_button)

        self.update_button = QPushButton("Modifier")
        self.update_button.setFont(button_font)
        self.update_button.setStyleSheet("background-color: blue; color: #ffffff; border: none;")
        self.update_button.clicked.connect(self.update_prof)
        button_layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Supprimer")
        self.delete_button.setFont(button_font)
        self.delete_button.setStyleSheet("background-color: red; color: #ffffff; border: none;")
        self.delete_button.clicked.connect(self.delete_prof)
        button_layout.addWidget(self.delete_button)

        main_layout.addWidget(button_frame)

        # TreeView Frame
        tree_frame = QWidget()
        tree_layout = QVBoxLayout(tree_frame)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["ID", "Nom", "Prénom", "Email", "DateNais", "Tele", "Adresse", "Department_id"])
        self.tree.setStyleSheet("background-color: #ffffff; color: #2c3e50;")
        tree_layout.addWidget(self.tree)

        # Connect double-click event
        self.tree.itemDoubleClicked.connect(self.on_double_click)

        self.refresh_button = QPushButton("Rafraîchir la Liste")
        self.refresh_button.setFont(button_font)
        self.refresh_button.setStyleSheet("background-color: #9b59b6; color: #ffffff; border: none;")
        self.refresh_button.clicked.connect(self.view_profs)
        tree_layout.addWidget(self.refresh_button)

        main_layout.addWidget(tree_frame)

        # Load professors on startup
        self.view_profs()

    def add_prof(self):
        """Add a new professor."""
        try:
            data = {k: v.text() for k, v in self.entries.items()}
            self.prof_methods.add_prof(data["name"], data["prenom"], data["email"], data["date_nais"],
                                       data["tele"], data["adresse"], data["department_name"])
            QMessageBox.information(self, "Succès", "Professeur ajouté avec succès !")
            self.clear_entries()
            self.view_profs()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors de l'ajout : {e}")

    def update_prof(self):
        """Update a professor."""
        try:
            selected_item = self.tree.currentItem()
            if not selected_item:
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un professeur à modifier.")
                return

            prof_id = selected_item.text(0)
            data = {k: v.text() for k, v in self.entries.items()}
            self.prof_methods.update_prof(prof_id, data["name"], data["prenom"], data["email"], data["date_nais"],
                                          data["tele"], data["adresse"], data["department_name"])
            QMessageBox.information(self, "Succès", "Professeur mis à jour avec succès !")
            self.clear_entries()
            self.view_profs()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors de la mise à jour : {e}")

    def delete_prof(self):
        """Delete a professor."""
        try:
            selected_item = self.tree.currentItem()
            if not selected_item:
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un professeur à supprimer.")
                return

            prof_id = selected_item.text(0)
            self.prof_methods.delete_prof(prof_id)
            QMessageBox.information(self, "Succès", "Professeur supprimé avec succès !")
            self.clear_entries()
            self.view_profs()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors de la suppression : {e}")

    def view_profs(self):
        """Display all professors in the Treeview."""
        self.tree.clear()  # Clear the treeview
        profs = self.prof_methods.get_all_profs()
        for prof in profs:
            item = QTreeWidgetItem(self.tree)
            for i, value in enumerate(prof):
                item.setText(i, str(value))

    def on_double_click(self, item):
        """Handle double-click to populate fields."""
        values = [item.text(i) for i in range(item.columnCount())]
        if values:
            # Populate fields
            self.entries["name"].setText(values[1])
            self.entries["prenom"].setText(values[2])
            self.entries["email"].setText(values[3])
            self.entries["date_nais"].setText(values[4])
            self.entries["tele"].setText(values[5])
            self.entries["adresse"].setText(values[6])

            # Fetch department name based on department_id
            department_id = values[7]
            department_name = self.prof_methods.get_department_name_by_id(department_id)
            self.entries["department_name"].setText(department_name)

    def clear_entries(self):
        """Clear all input fields."""
        for entry in self.entries.values():
            entry.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfView()
    window.show()
    sys.exit(app.exec_())