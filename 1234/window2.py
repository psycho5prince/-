from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout



class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.setWindowTitle("Второе окно")
        self.num_lbl = QLabel("Вход успешен!!!")
        vbox = QVBoxLayout()
        vbox.addWidget(self.num_lbl)
        self.setLayout(vbox)
       

