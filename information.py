# This Python file uses the following encoding: utf-8
import enter
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QSizePolicy

class Information(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        #Настройка окна
        self.setWindowTitle("О приложении")
        self.setWindowIcon(QIcon("./files/images/icon.png"))
        #---------------------------------

        #Расположение элементов окна
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(50)
        text = QLabel("Данное приложение предназначено для совершенствования\nзнаний по истории Древнего Китая.\n\nАвтор приложения: Крашенинников Кирилл\n\nВерсия: 1.0 от 29 Янв 2021\n\n©Все права защищены", font = QFont('Franklin Gotic Book', 12))
        buttonEnter = QPushButton("Приступить к обучению", self, font = QFont('Franklin Gotic Book', 12), focusPolicy=Qt.NoFocus, sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(200,35))

        layout.addWidget(text)
        layout.addWidget(buttonEnter, 0, Qt.AlignCenter)
        self.setLayout(layout)
        #---------------------------------

        #Подключение процедур к событию нажатия кнопки
        buttonEnter.clicked.connect(self.goingEnter)

    #Процедура перехода на окно входа
    def goingEnter(self):
        self.enterWindow = enter.Enter()
        self.enterWindow.show()
        self.hide()
