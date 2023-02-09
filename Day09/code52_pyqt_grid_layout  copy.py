#레이아웃 절대배치
import sys
from PyQt5.QtWidgets import *

class yourApp(QTabWidget):
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('title'),0,0) # row, col =0 ,0
        grid.addWidget(QLabel('Author'),1,0)
        grid.addWidget(QLabel('Review'),2,0)

        grid.addWidget(QLineEdit(),0,1)#0행 1열
        grid.addWidget(QLineEdit(),1,1)#1행 1열
        grid.addWidget(QTextEdit(),2,1)#2행 1열

        btnOk = QPushButton('Ok')
        btnCancel = QPushButton('Cancel')

        grid.addWidget(btnCancel, 4 ,1)
        grid.addWidget(btnOk, 3, 1)
    


        #필수설정
        self.setWindowTitle('박스배치')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = yourApp()
    sys.exit(app.exec_()) 
     

