import sys, random, string
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout,QLineEdit, QPushButton, QWidget
from PyQt6.QtCore import QTimer, Qt
from test import TestWindow
from welcome import WelcomeWindow

#Регистрация.......................................................................................................................

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350,230)
        self.setWindowTitle("Регистрация")

        self.first_lb1=QLabel("Login in")
        self.first_lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_lineEdit=QLineEdit()
        self.first_lb2=QLabel("Password in")
        self.first_lb2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_lineEdit2=QLineEdit()

        self.btn=QPushButton("Open")
        self.btn2=QPushButton("Close")
        self.btn.clicked.connect(self.btn_clicked)
        self.btn2.clicked.connect(self.exit)
        self.layout=QVBoxLayout()
        widget=QWidget()

        self.layout.addWidget(self.first_lb1)
        self.layout.addWidget(self.first_lineEdit)
        self.layout.addWidget(self.first_lb2)
        self.layout.addWidget(self.first_lineEdit2)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn2)
        self.setCentralWidget(widget)
        widget.setLayout(self.layout)


        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())


    def btn_clicked(self):
        if self.first_lineEdit.text() == "dota" and self.first_lineEdit2.text() == "2":
            self.test=WelcomeWindow()
            self.test.show()
        else:
            self.kapcha = Kapcha()
            self.kapcha.show()
            
    def exit(self):
        self.close()

#Тест................................................................................................................

class  WelcomeWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        lbl = QLabel("Сделаем тестик?)))))")
        btn = QPushButton("Пошли- ка)))))")
        btn.clicked.connect(self.click_b)
        vbox = QVBoxLayout()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(vbox)
        vbox.addWidget(lbl)
        vbox.addWidget(btn)
        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())
            
    def click_b(self):
        self.test = TestWindow()
        self.test.show()
        self.close()

# Капча................................................................................................................

class Kapcha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle("Капча")
        self.setFixedSize(400, 200)
        self.len=4
        self.capcha=string.digits+string.ascii_uppercase
        rnd_string=''.join(random.sample(self.capcha, self.len))
        rnd=random.randint(1000,9999)
        self.first_lb1=QLabel("Captcha")
        self.first_lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.first_lineEdit=QLineEdit()
        self.first_lb12=QLabel(str(rnd_string))
        self.btn=QPushButton("Проверка")
        self.btn.clicked.connect(self.btn_clicked)
#Таймер.................................................................................................................................
        self.timer_label=QLabel("Таймер тик тик тик:")
        self.timer=QTimer()
        self.timer_counter = 4
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timer_tick)
 
        self.layout=QVBoxLayout()
        widget=QWidget()

        self.layout.addWidget(self.first_lb1)
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.first_lineEdit)
        self.layout.addWidget(self.first_lb12)
        self.layout.addWidget(self.btn)
        self.setCentralWidget(widget)
        widget.setLayout(self.layout)
#CSS.......................................................................................................................................
        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())
# .........................................................................................................................................
    def btn_clicked(self):
        if self.first_lineEdit.text() == self.first_lb12.text():
            self.close()
        else:
            self.timer.start()
            self.btn.setEnabled(False)   
            
    def timer_start(self):
        self.timer_counter = 4
        self.timer.start()
        
    def timer_tick(self):
        self.timer.start(1000)
        self.timer_counter -= 1
        self.timer_label.setText(f"Таймер: {self.timer_counter}")
        self.first_lb12.setText("")

        if self.timer_counter == 0 :

            self.timer.stop()
            self.timer_counter=4
            self.btn.setEnabled(True)
            rnd_string=''.join(random.sample(self.capcha, self.len))
            self.first_lb12.setText(str(rnd_string))
# ..............................................................................................................................................
app=QApplication(sys.argv)
window=Main()
window.show()
app.exec()