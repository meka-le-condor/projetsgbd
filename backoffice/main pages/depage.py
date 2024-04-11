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

class Ui_CompteRendu(object):
    def setupUi(self, CompteRendu):
        CompteRendu.setObjectName("CompteRendu")
        CompteRendu.resize(800, 600)
        CompteRendu.setStyleSheet("background-color: #333333;")

        self.centralwidget = QtWidgets.QWidget(CompteRendu)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 380, 580))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Date"])
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.clicked.connect(self.show_details)

        self.textEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(400, 10, 380, 580))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("background-color: #2c3e50;")
       

        CompteRendu.setCentralWidget(self.centralwidget)

        self.retranslateUi(CompteRendu)
        QtCore.QMetaObject.connectSlotsByName(CompteRendu)

    def retranslateUi(self, CompteRendu):
        _translate = QtCore.QCoreApplication.translate
        CompteRendu.setWindowTitle(_translate("CompteRendu", "Compte Rendu"))

    def populate_table(self):
        # Récupérer les comptes rendus de la base de données
        query = "SELECT id, date_creation FROM compte_rendu"
        cursor.execute(query)
        compte_rendu = cursor.fetchall()

        # Remplir la table avec les données récupérées
        self.tableWidget.setRowCount(len(compte_rendu))
        for row, cr in enumerate(compte_rendu):
            for col, data in enumerate(cr):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget.setItem(row, col, item)

    def show_details(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            cr_id = int(self.tableWidget.item(selected_row, 0).text())
            query = "SELECT rapport FROM compte_rendu WHERE id = %s"
            cursor.execute(query, (cr_id,))
            cr_content = cursor.fetchone()[0]
            self.textEdit.setPlainText(cr_content)
        else:
            self.textEdit.clear()

class CompteRenduApp(QtWidgets.QMainWindow, Ui_CompteRendu):
    def __init__(self):
        super(CompteRenduApp, self).__init__()
        self.setupUi(self)
        self.populate_table()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CompteRenduApp()
    window.show()
    sys.exit(app.exec_())
