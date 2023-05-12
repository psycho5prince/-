import sys
from PyQt5.QtWidgets import QApplication,QWidget, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout 
from PyQt5 import QtWidgets
class TextWidget(QtWidgets.QWidget):
    def __init__(self, text):
        super().__init__()

        label = QtWidgets.QLabel(text)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Создаем экземпляры виджетов с текстом
        self.text1 = TextWidget('Это первый текст')
        self.text2 = TextWidget('Это второй текст')

        # Создаем QStackedWidget и добавляем в него виджеты
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.stacked_widget.addWidget(self.text1)
        self.stacked_widget.addWidget(self.text2)

        # Создаем кнопки для переключения между виджетами
        self.button1 = QtWidgets.QPushButton('Первый текст')
        self.button1.clicked.connect(lambda: self.change_widget(0))

        self.button2 = QtWidgets.QPushButton('Второй текст')
        self.button2.clicked.connect(lambda: self.change_widget(1))

        # Создаем макет и добавляем в него QStackedWidget и кнопки
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def change_widget(self, index):
        """Переключается на виджет с заданным индексом"""
        self.stacked_widget.setCurrentIndex(index)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())