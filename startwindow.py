# This Python file uses the following encoding: utf-8
import sys
import enter
import information
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, qApp, QStyleFactory, QSizePolicy
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QFontDatabase, QPalette, QColor, QIcon

class StartWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        #Настройка окна
        self.setWindowTitle("Обучающее приложение")
        self.setWindowIcon(QIcon("./files/images/icon.png"))
        #---------------------------------

        #Расположение элементов окна
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 150, 40, 25)
        layout.setSpacing(150)
        layoutButtons = QHBoxLayout()
        layoutButtons.setSpacing(200)
        fontLabel =QFont('DFBangShu Std', 24)
        fontLabel.setLetterSpacing(QFont.AbsoluteSpacing, -3)
        fontLabel.setWordSpacing(10)
        labelWelcome= QLabel("Обучающее приложение\n\nпо истории Древнего Китая", font = fontLabel)
        labelWelcome.setAlignment(Qt.AlignCenter)
        buttonEnter = QPushButton("Поехали!", self, font = QFont('Franklin Gotic Book', 12), focusPolicy=Qt.NoFocus, sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(160,30))
        informationButton = QPushButton("О приложении", self, font = QFont('Franklin Gotic Book', 12), focusPolicy=Qt.NoFocus, sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(160,30))

        layout.addWidget(labelWelcome)
        layoutButtons.addWidget(buttonEnter)
        layoutButtons.addWidget(informationButton)
        layout.addLayout(layoutButtons)
        self.setLayout(layout)
        #---------------------------------

        #Подключение процедур к событию нажатия кнопки
        buttonEnter.clicked.connect(self.goingEnter)
        informationButton.clicked.connect(self.lookInformation)

        #Создание оформления для приложения
        darkPalette = QPalette()
        darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.WindowText, QColor(230,230,230))
        darkPalette.setColor(QPalette.Base, QColor(25, 25, 25))
        darkPalette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.ToolTipBase, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.ToolTipText, QColor(200,200,200))
        darkPalette.setColor(QPalette.Text, QColor(186, 186, 186))
        darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.ButtonText, QColor(230,230,230))
        darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.Highlight, QColor(150,150,150))
        darkPalette.setColor(QPalette.HighlightedText, Qt.black)
        qApp.setPalette(darkPalette)
        #---------------------------------

    #Процедура перехода на окно входа
    def goingEnter(self):
        self.enterWindow = enter.Enter()
        self.enterWindow.show()
        self.hide()

    #Процедура перехода на окно информации
    def lookInformation(self):
        self.windowInformation = information.Information()
        self.windowInformation.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication([])#Создание приложения
    app.setStyle(QStyleFactory.create("Fusion"))#Установка стиля приложения
    #Подключение шрифтов
    QFontDatabase.addApplicationFont("./files/fonts/DFBangShu_Std_W8.ttf")
    QFontDatabase.addApplicationFont("./files/fonts/DFKanTingLiu_Std_W9.ttf")
    QFontDatabase.addApplicationFont("./files/fonts/FRABK.TTF")
    #---------------------
    window = StartWindow()#Создание окна
    window.show()#Отображение окна
    sys.exit(app.exec_())#Закрытие приложения
