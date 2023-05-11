from PyQt6.QtWidgets import  QWidget, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout 
from PyQt6.QtGui import QPixmap 
from PyQt6.QtCore import  QTimer
a = "W68HP"

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Капча")
        self.setFixedSize(1500, 700)

        self.first_lbl2 = QLabel("Введите капчу")
        self.first_lineEdit = QLineEdit()
        photo = QLabel()
        pix = QPixmap("captcha.png")
        photo.setPixmap(pix)
        
        self.layout = QVBoxLayout()
        widget = QWidget()
        
        self.btn = QPushButton("Ввести капчу")
        self.btn.clicked.connect(self.btn_clicked)
        self.layout.addWidget(self.first_lbl2)
        self.layout.addWidget(self.first_lineEdit)
        self.layout.addWidget(photo)
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.layout.addWidget(self.btn)
   
    # def capcha_timer(self, timer):
    #     self.total_second = timer
    #     self.timeq = QTimer(self)
    #     self.timeq.setInterval(100)
    #     self.timeq.timeout.connect(functools.partial(self.update_timer, 0))
    #     self.timeq.start()
    # def captcha_clicked(self,captcha):
    #     if self.acess:
    #         self.timer    



    def btn_clicked(self):
        if self.first_lineEdit.text() == a:
            self.close()
        # else:
            

    


