#레이아웃 절대배치
import sys
from PyQt5.QtWidgets import *

class yourApp(QTabWidget):
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self):
        btnOk = QPushButton('Ok')
        btnCancel = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btnOk)
        hbox.addWidget(btnCancel)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)

        #필수설정
        self.setWindowTitle('박스배치')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = yourApp()
    sys.exit(app.exec_()) 
     

