import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QWidget, QLabel, QStackedWidget

from login import login 
from inscription import inscription

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GESTION EFFECTIVITE ENSEIGNEMENT ESP")
        self.setGeometry(500, 500, 500, 500)

        # Création du menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&Menu")

        # Action pour accéder à la page de connexion
        login_action = QAction("&login", self)
        login_action.triggered.connect(self.open_login_page)
        file_menu.addAction(login_action)  
        

        # Action pour accéder à la page d'inscription
        inscription_action = QAction("&inscription", self)
        inscription_action.triggered.connect(self.open_inscription_page)
        file_menu.addAction(inscription_action)
        
    def open_login_page(self):   
        self.login_window = login()
        self.login_window.show()

    def open_inscription_page(self):
        self.inscription_window = inscription()
        self.inscription_window.show()



if __name__ == '__main__':
    app = QApplication([]) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
