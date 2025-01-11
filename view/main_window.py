from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QGridLayout
from PyQt5.QtGui import QFont, QColor, QLinearGradient, QPalette
from PyQt5.QtCore import Qt
from view.prof_view import ProfView
from view.module_view import ModuleView
from view.department_view import DepartmentView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Scolaire")
        self.setGeometry(100, 100, 800, 600)  # Larger window size
        self.setStyleSheet("background-color: #ffffff;")

        # Set gradient background
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor("#1c92d2"))  # Light blue
        gradient.setColorAt(1, QColor("#f2fcfe"))  # Light cyan
        palette = QPalette()
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)

        # Central Widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)  # Add spacing between widgets
        layout.setContentsMargins(50, 50, 50, 50)  # Add margins

        # Custom Fonts
        title_font = QFont("Helvetica", 32, QFont.Bold)
        button_font = QFont("Helvetica", 16, QFont.Bold)

        # Title Label
        title_label = QLabel("Gestion Scolaire", self)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 30px;")
        layout.addWidget(title_label)

        # Button Grid Layout
        button_grid = QGridLayout()
        button_grid.setSpacing(20)  # Add spacing between buttons

        # Department Button
        department_btn = QPushButton("Gestion des Départements", self)
        department_btn.setFont(button_font)
        department_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: #ffffff;
                border-radius: 15px;
                padding: 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        department_btn.clicked.connect(self.open_department_view)
        button_grid.addWidget(department_btn, 0, 0)

        # Professor Button
        prof_btn = QPushButton("Gestion des Professeurs", self)
        prof_btn.setFont(button_font)
        prof_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: #ffffff;
                border-radius: 15px;
                padding: 20px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        prof_btn.clicked.connect(self.open_prof_view)
        button_grid.addWidget(prof_btn, 0, 1)

        # Module Button
        module_btn = QPushButton("Gestion des Modules", self)
        module_btn.setFont(button_font)
        module_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: #ffffff;
                border-radius: 15px;
                padding: 20px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        module_btn.clicked.connect(self.open_module_view)
        button_grid.addWidget(module_btn, 1, 0)

        # Add button grid to the main layout
        layout.addLayout(button_grid)

    def open_department_view(self):
        """Open the DepartmentView window."""
        if not hasattr(self, "department_view") or not self.department_view.isVisible():
            self.department_view = DepartmentView(self)
            self.department_view.show()
        else:
            self.department_view.raise_()  # Bring the existing window to the front

    def open_prof_view(self):
        """Open the ProfView window."""
        self.prof_view = ProfView(self)  # Pass self as the parent
        self.prof_view.show()

    def open_module_view(self):
        """Open the ModuleView window."""
        self.module_view = ModuleView(self)  # Pass self as the parent
        self.module_view.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())