from PyQt6.QtWidgets import QHBoxLayout, QLabel, QMainWindow, QPushButton, QStackedLayout, QVBoxLayout, QWidget, QRadioButton
from PyQt6 import QtCore

# Тест.................................................................................................................................................
class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,450)
        lbl1 = QLabel("1.Первый скил ёжика из доты ?")
        self.rb1 = QRadioButton(text="Плевок")
        rb2 = QRadioButton(text="Колючки")
        rb3 = QRadioButton(text="Пасивка")
        vbox = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(vbox)
        vbox.addWidget(lbl1)
        vbox.addWidget(self.rb1)
        vbox.addWidget(rb2)
        vbox.addWidget(rb3)

        lbl2 = QLabel("2.Сколько персонажей в доте?")
        rb1_1 = QRadioButton(text="157")
        self.rb2_1 = QRadioButton(text="124")
        rb3_1 = QRadioButton(text="30")
        vbox2 = QVBoxLayout()
        widget2 = QWidget()
        widget2.setLayout(vbox2)
        vbox2.addWidget(lbl2)
        vbox2.addWidget(rb1_1)
        vbox2.addWidget(self.rb2_1)
        vbox2.addWidget(rb3_1)
 
        lbl3 = QLabel("3.Сколько длится турбо?")
        self.rb1_2 = QRadioButton(text="20-25 мин")
        rb2_2 = QRadioButton(text="1 час")
        rb3_2 = QRadioButton(text="2 дня")
        vbox3 = QVBoxLayout()
        widget3 = QWidget()
        widget3.setLayout(vbox3)
        vbox3.addWidget(lbl3)
        vbox3.addWidget(self.rb1_2)
        vbox3.addWidget(rb2_2)
        vbox3.addWidget(rb3_2)
        
        lbl4 = QLabel("4.Какое звание идёт после рекрутов")
        rb1_3 = QRadioButton(text="Рыцарь")
        rb2_3 = QRadioButton(text="Титан")
        self.rb3_3 = QRadioButton(text="Страж")
        vbox4 = QVBoxLayout()
        widget4 = QWidget()
        widget4.setLayout(vbox4)
        vbox4.addWidget(lbl4)
        vbox4.addWidget(rb1_3)
        vbox4.addWidget(rb2_3)
        vbox4.addWidget(self.rb3_3)
        
        lbl5 = QLabel("5.Через что в патче 7.33с играется арк?")
        rb1_4 = QRadioButton(text="Октарин")
        self.rb2_4 = QRadioButton(text="Манта")
        rb3_4 = QRadioButton(text="Радик")
        vbox5 = QVBoxLayout()
        widget5 = QWidget()
        widget5.setLayout(vbox5)
        vbox5.addWidget(lbl5)
        vbox5.addWidget(rb1_4)
        vbox5.addWidget(self.rb2_4)
        vbox5.addWidget(rb3_4)
        
        lbl6 = QLabel("Готов увидеть что натыкал?")
        lbl6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        rb3_5 = QPushButton("Да")
        rb3_5.clicked.connect(self.activate_tab_v)
        rb3_5.clicked.connect(self.result)
        vbox6 = QVBoxLayout()
        widget6 = QWidget()
        widget6.setLayout(vbox6)
        vbox6.addWidget(lbl6)
        vbox6.addWidget(rb3_5)
 #Результаты............................................................................................................................................ 
        lbl7 = QLabel("Результаты теста:")
        self.v6 = QLabel()
        self.v2 = QLabel()
        self.v3 = QLabel()
        self.v4 = QLabel()
        self.v5 = QLabel()
        self.res = QLabel()
        vbox7 = QVBoxLayout()
        widget7 = QWidget()
        widget7.setLayout(vbox7)
        vbox7.addWidget(lbl7)
        vbox7.addWidget(self.v6)
        vbox7.addWidget(self.v2)
        vbox7.addWidget(self.v3)
        vbox7.addWidget(self.v4)
        vbox7.addWidget(self.v5)
        vbox7.addWidget(self.res)
        
        pagelayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(self.stacklayout)
        pagelayout.addLayout(self.button_layout)
        
        self.btnb = QPushButton("back")
        self.btn = QPushButton("next")
        
        self.btnb.clicked.connect(self.activate_tab_b)
        self.btn.clicked.connect(self.activate_tab_v)
        self.stacklayout.addWidget(widget)
        self.button_layout.addWidget(self.btnb)
        self.button_layout.addWidget(self.btn)
        self.stacklayout.addWidget(widget2)
        self.stacklayout.addWidget(widget3)
        self.stacklayout.addWidget(widget4)
        self.stacklayout.addWidget(widget5)
        self.stacklayout.addWidget(widget6)
        self.stacklayout.addWidget(widget7)
        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
#css...................................................................................................................................................        
        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())
# .....................................................................................................................................................
    def activate_tab_v(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()+1)
            
    def activate_tab_b(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()-1)
        
    def result(self):
        if self.rb1.isChecked():
            self.v6.setText("1.Верно")
            a = 1
        else: 
            self.v6.setText("1.Не верно")
            a = 0
        if self.rb2_1.isChecked():
            self.v2.setText("2.Верно")
            b = a + 1
        else:
            self.v2.setText("2.Не верно")
            b = a
        if self.rb1_2.isChecked():
            self.v3.setText("3.Верно")
            t = b + 1
        else:
            self.v3.setText("3.Не верно")
            t = b
        if self.rb3_3.isChecked():
            self.v4.setText("4.Верно")
            d = t + 1
        else:
            self.v4.setText("4.Не верно")
            d = t
        if self.rb2_4.isChecked():
            self.v5.setText("5.Верно")
            e = d + 1
        else:
            self.v5.setText("5.Не верно")
            e = d
            
        self.setFixedSize(400, 300)
        self.res.setText(f"Ваш результат:{e}")
        with open ('results.txt', "w", encoding="utf-8")as f:
            f.write(str(e))
        
            
        

        

        

