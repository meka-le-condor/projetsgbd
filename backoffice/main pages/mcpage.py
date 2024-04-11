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

class Ui_RecommendationPage(object):
    def setupUi(self, RecommendationPage):
        RecommendationPage.setObjectName("RecommendationPage")
        RecommendationPage.resize(800, 600)
        RecommendationPage.setStyleSheet("background-color: #333333;")  # Définition de la couleur de fond de la page

        self.centralwidget = QtWidgets.QWidget(RecommendationPage)
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

        self.recommendation_label = QtWidgets.QLabel(self.centralwidget)
        self.recommendation_label.setGeometry(QtCore.QRect(150, 50, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.recommendation_label.setFont(font)
        self.recommendation_label.setObjectName("recommendation_label")
        self.recommendation_label.setText("Formuler une recommandation :")

        self.recommendation_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.recommendation_textEdit.setGeometry(QtCore.QRect(150, 100, 600, 400))
        self.recommendation_textEdit.setObjectName("recommendation_textEdit")

        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(350, 520, 100, 30))
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setText("Soumettre")
        self.submit_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")
        self.submit_button.clicked.connect(self.submit_recommendation)

        RecommendationPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(RecommendationPage)
        QtCore.QMetaObject.connectSlotsByName(RecommendationPage)

    def retranslateUi(self, RecommendationPage):
        _translate = QtCore.QCoreApplication.translate
        RecommendationPage.setWindowTitle(_translate("RecommendationPage", "Page de recommandation"))
        self.recommendation_label.setText(_translate("RecommendationPage", "Formuler une recommandation :"))

    def submit_recommendation(self):
        recommendation_text = self.recommendation_textEdit.toPlainText()
        if recommendation_text:
            query = "INSERT INTO recommandation (text) VALUES (%s)"
            cursor.execute(query, (recommendation_text,))
            conn.commit()
            QtWidgets.QMessageBox.information(self, "Succès", "Recommandation soumise avec succès.")
        else:
            QtWidgets.QMessageBox.warning(self, "Erreur", "Veuillez saisir une recommandation.")

    def logout(self):
        QtWidgets.QMessageBox.information(self, "Déconnexion", "Vous avez été déconnecté.")
        sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RecommendationPage = QtWidgets.QMainWindow()
    ui = Ui_RecommendationPage()
    ui.setupUi(RecommendationPage)
    RecommendationPage.show()
    sys.exit(app.exec_())
