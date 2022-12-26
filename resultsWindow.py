# This Python file uses the following encoding: utf-8
import mainWindow
from PyQt5.QtCore import QFile, QIODevice, QTextStream
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QListWidget


class ResultsWindow(QWidget):
    def __init__(self, name):
        QWidget.__init__(self)
        self.nameUser = name
        #Настройка окна
        self.setWindowTitle("Результаты тестирования")
        self.setWindowIcon(QIcon("./files/images/icon.png"))
        self.setMinimumSize(450,200)
        #---------------------------------

        #Расположение элементов окна
        layout = QVBoxLayout()
        list = QListWidget(font = QFont('Aria', 10))
        backButton = QPushButton("Вернуться на главное меню", self, font = QFont('Franklin Gotic Book', 12))
        layout.addWidget(list)
        layout.addWidget(backButton)
        self.setLayout(layout)
        #---------------------------------

        #Считывание результатов
        teoryFile = QFile("./files/text/tests.txt")
        teoryFile.open(QIODevice.ReadOnly)
        textStream = QTextStream(teoryFile)
        allText = textStream.readAll()
        teoryFile.close()
        questions = allText.split("\r\n")
        #---------------------------------

        #Образование списка результатов
        i=0
        while i<len(questions):
            list.addItem(questions[i])
            i+=1
        #---------------------------------

        #Подключение процедур к событию нажатия кнопки
        backButton.clicked.connect(self.mainWindow)


    #Процедура перехода на главное окно
    def mainWindow(self):
        self.main = mainWindow.MainWindow(self.nameUser)
        self.main.show()
        self.hide()
