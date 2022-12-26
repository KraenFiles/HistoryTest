# This Python file uses the following encoding: utf-8
import themesWindow
from PyQt5.QtCore import Qt, QFile, QIODevice, QTextStream
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QTextEdit


class TeoryWindow(QWidget):
    def __init__(self, num, name):
        super(TeoryWindow, self).__init__()
        self.nameUser = name
        #Настройка окна
        self.setWindowTitle("Темы")
        self.setWindowIcon(QIcon("./files/images/icon.png"))
        self.setMinimumSize(1200,800)
        #---------------------------------

        #Расположение элементов окна
        fontLabel = QFont('DFKanTingLiu Std', 15)
        fontLabel.setLetterSpacing(QFont.AbsoluteSpacing, -3)
        fontLabel.setWordSpacing(5)

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)
        name = QLabel(font=fontLabel)
        labelImage = QLabel()
        name.setAlignment(Qt.AlignCenter)
        textEdit = QTextEdit(font=QFont("Aria", 12))
        layout.addWidget(name)
        layout.addWidget(labelImage, 0, Qt.AlignCenter)
        layout.addWidget(textEdit)

        back = QPushButton("Назад", self, font = QFont('Franklin Gotic Book', 10))
        layout.addWidget(back, 0, Qt.AlignLeft)
        self.setLayout(layout)
        #---------------------------------

        #Считывание теории
        teoryFile = QFile("./files/text/history.txt")
        teoryFile.open(QIODevice.ReadOnly)
        textStream = QTextStream(teoryFile)
        allText = textStream.readAll()
        teoryFile.close()
        paragraphs = allText.split("\n")
        #---------------------------------

        #Вывод информации взависимости от выбранной темы
        if(num==1):
            name.setText(paragraphs[0])
            labelImage.setPixmap(QPixmap("./files/images/Sia.png"))

            text = ""
            i=2
            while i<=3:
                text +="\t"+paragraphs[i]+"\n"
                i+=1
            textEdit.setPlainText(text)
        elif(num==2):
            name.setText(paragraphs[5])
            labelImage.setPixmap(QPixmap("./files/images/cinImper.png"))

            text = ""
            i=7
            while i<=9:
                text +="\t"+paragraphs[i]+"\n"
                i+=1
            textEdit.setPlainText(text)
        elif(num==3):
            name.setText(paragraphs[11])
            labelImage.setPixmap(QPixmap("./files/images/han.png"))

            text = ""
            i=13
            while i<=17:
                text +="\t"+paragraphs[i]+"\n"
                i+=1
            textEdit.setPlainText(text)
        elif(num==4):
            name.setText(paragraphs[19])
            labelImage.setPixmap(QPixmap("./files/images/three.png"))

            text = ""
            i=21
            while i<=30:
                text +="\t"+paragraphs[i]+"\n"
                i+=1
            textEdit.setPlainText(text)
        elif(num==5):
            name.setText(paragraphs[32])
            labelImage.setPixmap(QPixmap("./files/images/Min.png"))

            text = ""
            i=34
            while i<=37:
                text +="\t"+paragraphs[i]+"\n"
                i+=1
            textEdit.setPlainText(text)
        else:
            name.setText(paragraphs[39])
            labelImage.setPixmap(QPixmap("./files/images/cin.png"))

            text = ""
            i=41
            while i<=47:
                text +="\t"+paragraphs[i]+"\n"
                i+=1
            textEdit.setPlainText(text)
        #---------------------------------

        #Подключение процедур к событию нажатия кнопки
        back.clicked.connect(self.backWindow)

    #Процедура перехода на окно с темами
    def backWindow(self):
        self.back = themesWindow.ThemesWindow(self.nameUser)
        self.back.show()
        self.hide()
