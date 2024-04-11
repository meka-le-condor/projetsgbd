import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sgbda"
)
cursor = conn.cursor()

class Ui_PVPage(object):
    def setupUi(self, PVPage):
        PVPage.setObjectName("PVPage")
        PVPage.resize(800, 600)
        PVPage.setStyleSheet("background-color: #333333;")  # Définition de la couleur de fond de la page

        self.centralwidget = QtWidgets.QWidget(PVPage)
        self.centralwidget.setObjectName("centralwidget")

        # Sidebar
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(10, 10, 120, 580))
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setStyleSheet("background-color: #333333;")

        self.logout_button = QtWidgets.QPushButton(self.sidebar)
        self.logout_button.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.logout_button.setObjectName("logout_button")
        self.logout_button.setText("Déconnexion")
        self.logout_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")
        self.logout_button.clicked.connect(self.logout)

        self.pv_label = QtWidgets.QLabel(self.centralwidget)
        self.pv_label.setGeometry(QtCore.QRect(150, 50, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pv_label.setFont(font)
        self.pv_label.setObjectName("pv_label")
        self.pv_label.setText("Dresser un PV :")

        self.pv_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.pv_textEdit.setGeometry(QtCore.QRect(150, 100, 600, 400))
        self.pv_textEdit.setObjectName("pv_textEdit")

        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(350, 520, 100, 30))
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setText("Soumettre")
        self.submit_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")
        self.submit_button.clicked.connect(self.submit_pv)

        PVPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(PVPage)
        QtCore.QMetaObject.connectSlotsByName(PVPage)

    def retranslateUi(self, PVPage):
        _translate = QtCore.QCoreApplication.translate
        PVPage.setWindowTitle(_translate("PVPage", "Page des PV"))
        self.pv_label.setText(_translate("PVPage", "Dresser un PV :"))

    def submit_pv(self):
        pv_text = self.pv_textEdit.toPlainText()
        if pv_text:
            query = "INSERT INTO pv (text) VALUES (%s)"
            cursor.execute(query, (pv_text,))
            conn.commit()
            QtWidgets.QMessageBox.information(self, "Succès", "PV soumis avec succès.")
        else:
            QtWidgets.QMessageBox.warning(self, "Erreur", "Veuillez saisir le PV.")

    def logout(self):
        QtWidgets.QMessageBox.information(self, "Déconnexion", "Vous avez été déconnecté.")
        sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PVPage = QtWidgets.QMainWindow()
    ui = Ui_PVPage()
    ui.setupUi(PVPage)
    PVPage.show()
    sys.exit(app.exec_())
