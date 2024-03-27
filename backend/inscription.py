from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
import mysql.connector
from login import login

class inscription(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PAGE D'INSCRIPTION")
        self.setGeometry(500, 500, 700, 600)

        layout = QVBoxLayout()

        label = QLabel("INSCRIPTION", alignment=Qt.AlignCenter)
        layout.addWidget(label)

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.fonction_input = QLineEdit()


        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(QLabel("fonction:"))
        layout.addWidget(self.fonction_input)

        login_button = QPushButton("inscrire")
        login_button.clicked.connect(self.inscrire)
        layout.addWidget(login_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connexion à la base de données MySQL
        self.connection = mysql.connector.connect(
            host='localhost',
            user='meka',
            password='meka',
            database='projetsgbd'
        )
        self.cursor = self.connection.cursor()

    def inscrire(self):
        username = self.username_input.text()
        password = self.password_input.text()
        fonction = self.fonction_input.text()

        
        # enregistrement
        self.cursor.execute("INSERT INTO user (username,password,fonction) values (%s,%s,%s)", (username, password,fonction))
       # user = self.cursor.fetchone()
        
        self.connection.commit()
        self.cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
        user= self.cursor.fetchone()
        if user:
         QMessageBox.information(self, "inscription", "inscription successful!")
         window=login()
        else:
         QMessageBox.information(self, "inscription", "inscription failed!")
       



