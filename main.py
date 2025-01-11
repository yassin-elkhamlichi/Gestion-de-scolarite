from createTables import create_connection, create_tables
from PyQt5.QtWidgets import QApplication

from view.main_window import MainWindow


def initialize_database():
    """Initialize the database by creating tables if they do not exist."""
    conn = create_connection()  # Connect to the database
    create_tables(conn)  # Create necessary tables
    conn.close()  # Close the connection

if __name__ == "__main__":
    import sys

    # Initialize the database
    initialize_database()

    # Start the main application
    app = QApplication(sys.argv)  # Initialize the PyQt5 application
    main_window = MainWindow()  # MainWindow is a subclass of QMainWindow
    main_window.show()  # Show the main window
    sys.exit(app.exec_())  # Execute the application's event loop
