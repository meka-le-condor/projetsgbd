import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QMessageBox

import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sgbda"
)
cursor = conn.cursor()

# Classe UI pour la première page
class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: #333333;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Sidebar
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(10, 20, 150, 550))
        self.sidebar.setObjectName("sidebar")

        self.sidebar_label = QtWidgets.QLabel(self.sidebar)
        self.sidebar_label.setGeometry(QtCore.QRect(20, 20, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sidebar_label.setFont(font)
        self.sidebar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_label.setObjectName("sidebar_label")
        self.sidebar_label.setText("Menu")

        self.calendar_button = QtWidgets.QPushButton(self.sidebar)
        self.calendar_button.setGeometry(QtCore.QRect(10, 80, 130, 32))
        self.calendar_button.setObjectName("calendar_button")
        self.calendar_button.setText("Calendrier")

        self.form_button = QtWidgets.QPushButton(self.sidebar)
        self.form_button.setGeometry(QtCore.QRect(10, 140, 130, 32))
        self.form_button.setObjectName("form_button")
        self.form_button.setText("Formulaire")

        self.rapports_button = QtWidgets.QPushButton(self.sidebar)
        self.rapports_button.setGeometry(QtCore.QRect(10, 200, 130, 32))
        self.rapports_button.setObjectName("rapports_button")
        self.rapports_button.setText("Rapports")

        self.logout_button = QtWidgets.QPushButton(self.sidebar)
        self.logout_button.setGeometry(QtCore.QRect(10, 260, 130, 32))
        self.logout_button.setObjectName("logout_button")
        self.logout_button.setText("Déconnexion")

        # Main content
        self.main_content = QtWidgets.QFrame(self.centralwidget)
        self.main_content.setGeometry(QtCore.QRect(170, 20, 620, 550))
        self.main_content.setObjectName("main_content")

        # Cahier de texte (initialisé avec un label)
        self.textbook_label = QtWidgets.QLabel(self.main_content)
        self.textbook_label.setGeometry(QtCore.QRect(10, 10, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textbook_label.setFont(font)
        self.textbook_label.setObjectName("textbook_label")
        self.textbook_label.setText("Cahier de texte")

        # Calendrier
        self.calendarWidget = QtWidgets.QCalendarWidget(self.main_content)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 50, 300, 250))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.clicked.connect(self.show_events)

        # Liste des événements
        self.events_list = QtWidgets.QListWidget(self.main_content)
        self.events_list.setGeometry(QtCore.QRect(320, 50, 280, 250))
        self.events_list.setObjectName("events_list")

        # Formulaire (initialisé mais caché)
        self.form_frame = QtWidgets.QFrame(self.main_content)
        self.form_frame.setGeometry(QtCore.QRect(10, 310, 600, 200))
        self.form_frame.setObjectName("form_frame")
        self.form_frame.hide()

        self.label = QtWidgets.QLabel(self.form_frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Formulaire")

        self.formLayoutWidget = QtWidgets.QWidget(self.form_frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 581, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.lineEdit_1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)

        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Envoyer")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sidebar_label.setText(_translate("MainWindow", "Menu"))
        self.calendar_button.setText(_translate("MainWindow", "Calendrier"))
        self.form_button.setText(_translate("MainWindow", "Formulaire"))
        self.rapports_button.setText(_translate("MainWindow", "Rapports"))
        self.logout_button.setText(_translate("MainWindow", "Déconnexion"))
        self.label.setText(_translate("MainWindow", "Formulaire"))

# Classe UI pour la deuxième page
class Ui_RapportsWindow(object):
    def setupUi(self, RapportsWindow):
        RapportsWindow.setObjectName("RapportsWindow")
        RapportsWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(RapportsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 300, 200))
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 230, 100, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Envoyer Rapport")
        self.pushButton.clicked.connect(self.send_report)

        RapportsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RapportsWindow)
        QtCore.QMetaObject.connectSlotsByName(RapportsWindow)

    def retranslateUi(self, RapportsWindow):
        _translate = QtCore.QCoreApplication.translate
        RapportsWindow.setWindowTitle(_translate("RapportsWindow", "RapportsWindow"))
        self.pushButton.setText(_translate("RapportsWindow", "Envoyer Rapport"))

    def send_report(self):
        report_text = self.textEdit.toPlainText()
        query = "INSERT INTO rapports (rapport) VALUES (%s)"
        cursor.execute(query, (report_text,))
        conn.commit()
        QMessageBox.information(None, "Succès", "Rapport envoyé avec succès.")

# Classe pour la deuxième page
class RapportsApp(QtWidgets.QMainWindow, Ui_RapportsWindow):
    def __init__(self):
        super(RapportsApp, self).__init__()
        self.setupUi(self)

# MainApp avec la logique pour la première page
class MainApp(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)
        self.calendar_button.clicked.connect(self.show_calendar)
        self.form_button.clicked.connect(self.show_form)
        self.rapports_button.clicked.connect(self.show_rapports)
        self.logout_button.clicked.connect(self.logout)
        self.pushButton.clicked.connect(self.submit_form)
        self.selected_date = None

    def show_calendar(self):
        self.main_content.show()
        self.form_frame.hide()
        self.textbook_label.setText("Cahier de texte")

    def show_form(self):
        self.main_content.show()
        self.form_frame.show()
        self.textbook_label.setText("Formulaire")

    def show_rapports(self):
        self.rapports_page = RapportsApp()
        self.rapports_page.show()

    def logout(self):
        QMessageBox.information(None, "Déconnexion", "Vous avez été déconnecté.")
        sys.exit()

    def show_events(self):
        self.selected_date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        query = "SELECT description FROM events WHERE date = %s"
        cursor.execute(query, (self.selected_date,))
        events = cursor.fetchall()
        self.events_list.clear()
        if events:
            for event in events:
                self.events_list.addItem(event[0])
        else:
            self.events_list.addItem("Aucun événement pour cette date.")
            self.add_description_button = QtWidgets.QPushButton("Ajouter Description", self.main_content)
            self.add_description_button.setGeometry(320, 310, 150, 32)
            self.add_description_button.clicked.connect(self.add_description)

    def add_description(self):
        description, ok = QtWidgets.QInputDialog.getText(self, 'Ajouter Description', 'Entrez la description :')
        if ok:
            query = "INSERT INTO events (date, description) VALUES (%s, %s)"
            cursor.execute(query, (self.selected_date, description))
            conn.commit()
            self.events_list.clear()
            self.events_list.addItem(description)
            self.add_description_button.hide()
            QMessageBox.information(None, "Succès", "Description ajoutée avec succès.")

    def submit_form(self):
        if self.selected_date:
            # Récupérer les données du formulaire
            data_1 = self.lineEdit_1.text()
            data_2 = self.lineEdit_2.text()
            data_3 = self.lineEdit_3.text()
            data_4 = self.lineEdit_4.text()

            # Insérer les données dans la base de données
            query = "INSERT INTO table_name (column_name1, column_name2, column_name3, column_name4, event_date) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (data_1, data_2, data_3, data_4, self.selected_date))
            conn.commit()

            # Effacer les champs de saisie après l'envoi
            self.lineEdit_1.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            QMessageBox.information(None, "Succès", "Formulaire soumis avec succès.")
        else:
            QMessageBox.warning(None, "Erreur", "Veuillez sélectionner une date dans le calendrier.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
