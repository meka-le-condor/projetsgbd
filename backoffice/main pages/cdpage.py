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

class Ui_RapportsReçus(object):
    def setupUi(self, RapportsReçus):
        RapportsReçus.setObjectName("RapportsReçus")
        RapportsReçus.resize(800, 600)
        RapportsReçus.setStyleSheet("background-color: #333333;")

        self.centralwidget = QtWidgets.QWidget(RapportsReçus)
        self.centralwidget.setObjectName("centralwidget")
        

        # Sidebar
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(10, 10, 150, 580))
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setStyleSheet("background-color: #2c3e50;")  # Couleur de fond de la sidebar

        self.logout_button = QtWidgets.QPushButton(self.sidebar)
        self.logout_button.setGeometry(QtCore.QRect(10, 540, 130, 32))
        self.logout_button.setObjectName("logout_button")
        self.logout_button.setText("Déconnexion")
        self.logout_button.setStyleSheet("background-color: #e74c3c; color: white;")  # Couleurs du bouton de déconnexion
        self.logout_button.clicked.connect(self.logout)

        # Bouton pour afficher les PV
        self.pv_button = QtWidgets.QPushButton(self.sidebar)
        self.pv_button.setGeometry(QtCore.QRect(10, 40, 130, 32))
        self.pv_button.setObjectName("pv_button")
        self.pv_button.setText("PV")
        self.pv_button.setStyleSheet("background-color: #3498db; color: white;")
        self.pv_button.clicked.connect(self.show_pv)

        # Table des rapports
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 10, 620, 550))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)  
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Personne", "Date", "En savoir plus", "Sélection"])

        # Ajouter les rapports dans la table
        self.populate_table()

        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setGeometry(QtCore.QRect(170, 570, 150, 32))
        self.pushButton_send.setObjectName("pushButton_send")
        self.pushButton_send.setText("Envoyer au compte rendu")
        self.pushButton_send.setStyleSheet("background-color: #3498db; color: white;")  # Couleurs du bouton "Envoyer"
        self.pushButton_send.clicked.connect(self.send_to_report)

        RapportsReçus.setCentralWidget(self.centralwidget)

    def populate_table(self):
        # Récupérer les rapports de la base de données
        query = "SELECT id, personne, date FROM rapports"
        cursor.execute(query)
        rapports = cursor.fetchall()

        # Remplir la table avec les données récupérées
        self.tableWidget.setRowCount(len(rapports))
        for row, rapport in enumerate(rapports):
            for col, data in enumerate(rapport):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget.setItem(row, col, item)

            # Ajouter un bouton "En savoir plus" dans la colonne appropriée
            button = QtWidgets.QPushButton("En savoir plus")
            button.setStyleSheet("background-color: #2ecc71; color: white;")  # Couleurs du bouton "En savoir plus"
            button.clicked.connect(lambda _, id=rapport[0]: self.show_more_info(id))
            self.tableWidget.setCellWidget(row, 3, button)

            # Ajouter une case à cocher dans la colonne appropriée
            checkbox = QtWidgets.QCheckBox()
            self.tableWidget.setCellWidget(row, 4, checkbox)

    def send_to_report(self):
        # Récupérer les rapports sélectionnés dans la table
        selected_reports = []
        for row in range(self.tableWidget.rowCount()):
            checkbox = self.tableWidget.cellWidget(row, 4)
            if checkbox.isChecked():
                id_item = self.tableWidget.item(row, 0)
                selected_reports.append(int(id_item.text()))

        # Envoyer les rapports sélectionnés dans la table des comptes rendus
        for report_id in selected_reports:
            query = "INSERT INTO compte_rendu (id) VALUES (%s)"
            cursor.execute(query, (report_id,))
            conn.commit()

    def show_more_info(self, report_id):
        # Récupérer plus d'informations sur le rapport avec l'ID donné
        query = "SELECT rapport FROM rapports WHERE id = %s"
        cursor.execute(query, (report_id,))
        rapport_info = cursor.fetchone()

        # Afficher les informations supplémentaires dans une boîte de dialogue
        QtWidgets.QMessageBox.information(None, "En savoir plus", "Contenu du rapport : {}".format(rapport_info[0]))

    def logout(self):
        QtWidgets.QMessageBox.information(None, "Déconnexion", "Vous avez été déconnecté.")
        sys.exit()

    def show_pv(self):
        # Récupérer les PV de la base de données
        query = "SELECT id, personne, date FROM pv"
        cursor.execute(query)
        pvs = cursor.fetchall()

        # Créer une nouvelle fenêtre pour afficher les PV
        pv_window = QtWidgets.QWidget()
        pv_window.setWindowTitle("Liste des PV")
        pv_window.setGeometry(100, 100, 600, 400)

        # Créer une table pour afficher les PV
        pv_table = QtWidgets.QTableWidget(pv_window)
        pv_table.setGeometry(QtCore.QRect(10, 10, 580, 350))
        pv_table.setColumnCount(4)
        pv_table.setHorizontalHeaderLabels(["ID", "Personne", "Date", "Sélection"])

        # Remplir la table avec les données des PV
        pv_table.setRowCount(len(pvs))
        for row, pv in enumerate(pvs):
            for col, data in enumerate(pv):
                item = QtWidgets.QTableWidgetItem(str(data))
                pv_table.setItem(row, col, item)

            # Ajouter une case à cocher pour chaque PV
            checkbox = QtWidgets.QCheckBox()
            pv_table.setCellWidget(row, 3, checkbox)

        # Ajouter un bouton pour envoyer les PV sélectionnés
        send_button = QtWidgets.QPushButton("Envoyer au compte rendu", pv_window)
        send_button.setGeometry(QtCore.QRect(10, 370, 200, 30))
        send_button.clicked.connect(self.send_pvs_to_report)

        pv_window.show()

class RapportsReçusApp(QtWidgets.QMainWindow, Ui_RapportsReçus):
    def __init__(self):
        super(RapportsReçusApp, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RapportsReçusApp()
    window.show()
    sys.exit(app.exec_())
