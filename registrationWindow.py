# This Python file uses the following encoding: utf-8
import enter
import mainWindow
import hashlib
from PyQt5.QtCore import QFile, QIODevice, QTextStream, QSize,Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QFormLayout, QHBoxLayout, QLineEdit, QMessageBox, QSizePolicy,QLabel

class Registration(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        #Настройка окна
        self.setWindowTitle("Регистрация")
        self.setWindowIcon(QIcon("./files/images/icon.png"))

        #Расположение элементов окна
        layout = QFormLayout()
        layout.setContentsMargins(25,25,25,25)
        layout.setSpacing(15)
        buttonLayout = QHBoxLayout()
        buttonLayout.setSpacing(15)
        labelName= QLabel("Введите имя: ", font=QFont('Aria', 12))
        labelPassword= QLabel("Введите пароль: ", font=QFont('Aria', 12))
        labelTwoPassword= QLabel("Снова введите пароль: ", font=QFont('Aria', 12))
        self.editLogin = QLineEdit(self, font=QFont('Aria', 12))
        self.editPassword = QLineEdit(self, font=QFont('Aria', 12))
        self.editPassword.setEchoMode(QLineEdit.Password)
        self.editPasswordSecond = QLineEdit(self, font=QFont('Aria', 12))
        self.editPasswordSecond.setEchoMode(QLineEdit.Password)
        registButton = QPushButton("Зарегистрироваться", self, font=QFont('Franklin Gotic Book', 11), sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(160,30))
        backButton = QPushButton("Назад", self, font=QFont('Franklin Gotic Book', 11), sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(160,30))

        buttonLayout.addWidget(registButton)
        buttonLayout.addWidget(backButton)
        layout.addRow(labelName, self.editLogin)
        layout.addRow(labelPassword, self.editPassword)
        layout.addRow(labelTwoPassword, self.editPasswordSecond)
        layout.addRow(buttonLayout)

        self.setLayout(layout)
        #---------------------------------

        #Подключение процедур к событию нажатия кнопки
        backButton.clicked.connect(self.returnBack)
        registButton.clicked.connect(self.registration)

    #Процедура перехода на окно входа
    def returnBack(self):
        self.back = enter.Enter()
        self.back.show()
        self.hide()

    #Процедура регистрации
    def registration(self):
        accountsFile = QFile("./files/text/accounts.txt")#Файл с пользователями
        accountsFile.open(QIODevice.ReadOnly)#Открытие файла для считывание
        textStream = QTextStream(accountsFile)#Поток для работы с файлом
        all = textStream.readAll()#Считывание всех данных
        accountsFile.close()#Закрытие файла
        check=True
        lines = all.split("\n")
        for line in lines:
            accounts = line.split("/")
            if(self.editLogin.text()==accounts[0]):#Проверка на наличие пользователей с таким же именем
                QMessageBox.about(self, "Предупреждение", "Пользователь с данным именем уже существует")
                check=False
                break
            else:
                check=True
        if(self.editPassword.text()==self.editPasswordSecond.text() and check):#Проверка на совпадение паролей
            check=True
            accountsFile.open(QIODevice.Append)#Открытие файла для добавление
            textStream.setCodec("UTF-8")#Установка кодировки
            mdPas=hashlib.md5(self.editPassword.text().encode())#Хэширование пароля
            textStream<<self.editLogin.text()+"/"+mdPas.hexdigest()+"\n"#ЗАпись в файл
            accountsFile.close()
            #Переход на главное окно
            self.main = mainWindow.MainWindow(self.editLogin.text())
            self.main.show()
            self.hide()
        else:
            QMessageBox.about(self, "Предупреждение", "Пароли не совпадают")

