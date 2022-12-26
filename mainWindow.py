# This Python file uses the following encoding: utf-8
import themesWindow
import testWindow
import resultsWindow
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout,QSizePolicy


class MainWindow(QWidget):
    def __init__(self, name):
        QWidget.__init__(self)
        self.nameUser = name
        #Настройка окна
        self.setWindowTitle("Главное меню")
        self.setWindowIcon(QIcon("./files/images/icon.png"))
        #---------------------------------

        #Расположение элементов окна
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(50)
        teory = QPushButton("Темы", self, font=QFont('Franklin Gotic Book', 14), sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(250,50))
        test = QPushButton("Тест", self, font=QFont('Franklin Gotic Book', 14), sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(250,50))
        statics = QPushButton("Статистика", self, font=QFont('Franklin Gotic Book', 14), sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(250,50))

        layout.addWidget(teory)
        layout.addWidget(test)
        layout.addWidget(statics)
        self.setLayout(layout)
        #---------------------------------

        #Подключение процедур к событию нажатия кнопки
        teory.clicked.connect(self.goingThemesWindow)
        test.clicked.connect(self.openTest)
        statics.clicked.connect(self.openStatistic)

    #Процедура перехода на окно с темами
    def goingThemesWindow(self):
        self.themes = themesWindow.ThemesWindow(self.nameUser)
        self.themes.show()
        self.hide()

    #Процедура перехода на окно теста
    def openTest(self):
        self.test = testWindow.TestWindow(self.nameUser)
        self.test.show()
        self.hide()

    #Процедура перехода на окно результатов
    def openStatistic(self):
        self.results = resultsWindow.ResultsWindow(self.nameUser)
        self.results.show()
        self.hide()
