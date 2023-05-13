from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout
import sys

class MainWindow(QMainWindow):
    def btn_clicked(self):
        first = int(self.first_lineEdit.text())
        operator = self.operator_spisok.currentText()
        resultat = None

    def exit(self):
        app.exit()
        
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 350)
        
        main_grid = QGridLayout()
        widget = QWidget()

        self.setWindowTitle("Регистрация")

        self.first_lbl = QLabel("Добавить ФИО ")
        self.first_lineEdit = QLineEdit()

        self.second_lbl2 = QLabel("Выбрать класс ")
        self.operator_spisok2 = QComboBox()
        self.operator_spisok2.addItem("1")
        self.operator_spisok2.addItem("2")
        self.operator_spisok2.addItem("3")
        self.operator_spisok2.addItem("4")
        self.operator_spisok2.addItem("5")
        self.operator_spisok2.addItem("6")
        self.operator_spisok2.addItem("7")
        self.operator_spisok2.addItem("8")
        self.operator_spisok2.addItem("9")
        self.operator_spisok2.addItem("10")
        self.operator_spisok2.addItem("11")

        self.operator_lbl = QLabel("Выбрать индекс класса ")
        self.operator_spisok = QComboBox()

        self.operator_spisok.addItem("А")
        self.operator_spisok.addItem("Б")
        self.operator_spisok.addItem("В")
        self.operator_spisok.addItem("Г")

        self.btn = QPushButton("Добавить")
        self.btn2 = QPushButton("Выход")
        main_grid.addWidget(self.btn, 0, 0)
        main_grid.addWidget(self.btn2, 1, 0)
        self.btn2.clicked.connect(self.exit)
        self.btn.clicked.connect(self.btn_clicked)
        self.resultat = QLabel("")
        layout = QVBoxLayout()
        widget = QWidget()
        
        
        layout.addWidget(self.first_lbl)
        layout.addWidget(self.first_lineEdit)
        layout.addWidget(self.second_lbl2)
        layout.addWidget(self.operator_spisok2)
        layout.addWidget(self.operator_lbl)
        layout.addWidget(self.operator_spisok)
        layout.addWidget(self.btn)
        layout.addWidget(self.btn2)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        layout.addWidget(self.btn)
        layout.addWidget(self.btn2)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()