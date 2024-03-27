import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QWidget, QLabel, QStackedWidget


class accueil(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PAGE ACCUEIL")
        self.setGeometry(500, 500, 500, 500)

if __name__ == '__main__':
    app = QApplication([]) 
    window = accueil()
    window.show()
    sys.exit(app.exec_())
