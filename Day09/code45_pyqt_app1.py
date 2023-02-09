import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):    
        # GUI 화면 설정
        self.setWindowTitle('simple window')
        self.move(720,0)
        self.resize(400, 200)
        self.show() # 핵심!


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())