# This Python file uses the following encoding: utf-8
import teoryWindow
import mainWindow
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

#Класс с наследованием от QLabel
class Label(QLabel):
    clicked = pyqtSignal()#Сигнал при нажатии

    def __init__(self, parent=None):
        super(Label, self).__init__(parent)

    #Процедура обработки расположение мыши
    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()

    #Изменения цвета текста при наведении мыши
    def enterEvent(self, QEvent):
        self.setStyleSheet("color: rgb(150, 0, 0)")
        pass

    #Возвращение исходного цвета текста
    def leaveEvent(self, QEvent):
        self.setStyleSheet("color: rgb(230,230,230)")
        pass

class ThemesWindow(QWidget):
    def __init__(self, name):
        QWidget.__init__(self)
        self.nameUser = name
        #Настройка окна
        self.setWindowTitle("Темы")
        self.setWindowIcon(QIcon("./files/images/icon.png"))
        self.setFixedSize(1302,700)
        #---------------------------------

        #Расположение элементов окна
        mainLayout = QVBoxLayout()
        imageLayout = QHBoxLayout()
        imageLayout.setSpacing(0)
        imageLayout.setContentsMargins(0, 0, 0, 0)
        textLayout = QHBoxLayout()
        textLayout.setContentsMargins(30, 0, 0, 0)
        textLayout.setSpacing(25)

        fontLabel =QFont('DFKanTingLiu Std', 11)
        fontLabel.setLetterSpacing(QFont.AbsoluteSpacing, -3)
        fontLabel.setWordSpacing(5)

        textLabel1 = Label("До имперский\nКитай")
        textLabel1.setFont(fontLabel)
        imageLabel1 = Label()
        imageLabel1.setPixmap(QPixmap("./files/images/Path1.png"))
        imageLabel1.setAlignment(Qt.AlignLeft)

        imageLabel2 = Label()
        imageLabel2.setPixmap(QPixmap("./files/images/Path2.png"))
        imageLabel2.setAlignment(Qt.AlignLeft)
        textLabel2 = Label("Династия Цинь")
        textLabel2.setFont(fontLabel)

        imageLabel3 = Label()
        imageLabel3.setPixmap(QPixmap("./files/images/Path3.png"))
        imageLabel3.setAlignment(Qt.AlignLeft)
        textLabel3 = Label("Династия Хань")
        textLabel3.setFont(fontLabel)

        imageLabel4 = Label()
        imageLabel4.setPixmap(QPixmap("./files/images/Path4.png"))
        imageLabel4.setAlignment(Qt.AlignLeft)
        textLabel4 = Label("Троецарствие")
        textLabel4.setFont(fontLabel)

        imageLabel5 = Label()
        imageLabel5.setPixmap(QPixmap("./files/images/Path5.png"))
        imageLabel5.setAlignment(Qt.AlignLeft)
        textLabel5 = Label("Династия Мин")
        textLabel5.setFont(fontLabel)

        imageLabel6 = Label()
        imageLabel6.setPixmap(QPixmap("./files/images/Path6.png"))
        imageLabel6.setAlignment(Qt.AlignLeft)
        textLabel6 = Label("Династия Цин")
        textLabel6.setFont(fontLabel)

        imageLayout.addWidget(imageLabel1, 0, Qt.AlignLeft)
        imageLayout.addWidget(imageLabel2, 0, Qt.AlignLeft)
        imageLayout.addWidget(imageLabel3, 0, Qt.AlignLeft)
        imageLayout.addWidget(imageLabel4, 0, Qt.AlignLeft)
        imageLayout.addWidget(imageLabel5, 0, Qt.AlignLeft)
        imageLayout.addWidget(imageLabel6, 0, Qt.AlignLeft)

        textLayout.addWidget(textLabel1, 0, Qt.AlignRight)
        textLayout.addWidget(textLabel2, 0, Qt.AlignRight)
        textLayout.addWidget(textLabel3, 0, Qt.AlignRight)
        textLayout.addWidget(textLabel4, 0, Qt.AlignRight)
        textLayout.addWidget(textLabel5, 0, Qt.AlignRight)
        textLayout.addWidget(textLabel6, 0, Qt.AlignRight)

        mainLayout.addLayout(imageLayout)
        mainLayout.addLayout(textLayout)
        self.setLayout(mainLayout)
        back = QPushButton("Назад", self, font = QFont('Franklin Gotic Book', 10))
        mainLayout.addWidget(back, 0, Qt.AlignLeft)
        #---------------------------------

        #Подключение процедур к событию нажатия на текст или картинку
        imageLabel1.clicked.connect(self.openFirstThem)
        imageLabel2.clicked.connect(self.openSecondThem)
        imageLabel3.clicked.connect(self.openThirdThem)
        imageLabel4.clicked.connect(self.openFourthThem)
        imageLabel5.clicked.connect(self.openFifthThem)
        imageLabel6.clicked.connect(self.openSixthThem)

        textLabel1.clicked.connect(self.openFirstThem)
        textLabel2.clicked.connect(self.openSecondThem)
        textLabel3.clicked.connect(self.openThirdThem)
        textLabel4.clicked.connect(self.openFourthThem)
        textLabel5.clicked.connect(self.openFifthThem)
        textLabel6.clicked.connect(self.openSixthThem)

        back.clicked.connect(self.backWindow)
        #---------------------------------

    #Процедура перехода на главное окно
    def backWindow(self):
        self.back = mainWindow.MainWindow(self.nameUser)
        self.back.show()
        self.hide()

    #Процедура перехода на окно с теорией по первой теме
    def openFirstThem(self):
        self.them1 = teoryWindow.TeoryWindow(1,self.nameUser)
        self.them1.show()
        self.hide()

    #Процедура перехода на окно с теорией по второй теме
    def openSecondThem(self):
        self.them2 = teoryWindow.TeoryWindow(2,self.nameUser)
        self.them2.show()
        self.hide()

    #Процедура перехода на окно с теорией по третьей теме
    def openThirdThem(self):
        self.them3 = teoryWindow.TeoryWindow(3,self.nameUser)
        self.them3.show()
        self.hide()

    #Процедура перехода на окно с теорией по четвертой теме
    def openFourthThem(self):
        self.them4 = teoryWindow.TeoryWindow(4,self.nameUser)
        self.them4.show()
        self.hide()

    #Процедура перехода на окно с теорией по пятой теме
    def openFifthThem(self):
        self.them5 = teoryWindow.TeoryWindow(5,self.nameUser)
        self.them5.show()
        self.hide()

    #Процедура перехода на окно с теорией по шестой теме
    def openSixthThem(self):
        self.them6 = teoryWindow.TeoryWindow(6,self.nameUser)
        self.them6.show()
        self.hide()
