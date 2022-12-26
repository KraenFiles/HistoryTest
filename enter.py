# This Python file uses the following encoding: utf-8
import registrationWindow
import mainWindow
import hashlib
from PyQt5.QtCore import QFile, QIODevice, QTextStream, QSize, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QFormLayout, QHBoxLayout, QLineEdit, QMessageBox, QSizePolicy,QLabel

class Enter(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        #Настройка окна
        self.setWindowTitle("Вход")
        self.setWindowIcon(QIcon("./files/images/icon.png"))
        #---------------------------------

        #Расположение элементов окна
        layout = QFormLayout()

        layout.setContentsMargins(25,25,25,25)
        layout.setSpacing(15)
        buttonLayout = QHBoxLayout()
        buttonLayout.setSpacing(15)
        labelName= QLabel("Введите имя: ", font=QFont('Aria', 12))
        labelPassword= QLabel("Введите пароль: ", font=QFont('Aria', 12))
        self.editLogin = QLineEdit(self, font=QFont('Aria', 12))
        self.editPassword = QLineEdit(self, font=QFont('Aria', 12))
        self.editPassword.setEchoMode(QLineEdit.Password)
        enterButton = QPushButton("Войти", self, font=QFont('Franklin Gotic Book', 11), sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(160,30))
        registButton = QPushButton("Зарегистрироваться", self, font=QFont('Franklin Gotic Book', 11), sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(160,30))

        buttonLayout.addWidget(enterButton)
        buttonLayout.addWidget(registButton)
        layout.addRow(labelName, self.editLogin)
        layout.addRow(labelPassword, self.editPassword)
        layout.addRow(buttonLayout)

        self.setLayout(layout)
        #---------------------------------

        #Подключение процедур к событию нажатия кнопки
        enterButton.clicked.connect(self.mainWindow)
        registButton.clicked.connect(self.regisrationWindow)

    #Процедура проверки данных для входа
    def mainWindow(self):
        accountsFile = QFile("./files/text/accounts.txt")#Файл с пользователями
        accountsFile.open(QIODevice.ReadOnly)#Открытие файла
        textStream = QTextStream(accountsFile)#Поток для работы с файлом
        all = textStream.readAll()#Считывание всех данных
        accountsFile.close()#Закрытие файла
        lines = all.split("\n")#Разделение файла по строкам
        check = False
        for line in lines:
            accounts = line.split("/")
            hashPas = hashlib.md5(self.editPassword.text().encode())#Хэширование пароля
            if(accounts[0]!=''):#Проверка на пустое значение
                if(self.editLogin.text()==accounts[0] and hashPas.hexdigest()==accounts[1]):#Проверка на наличие данного пользователя
                    check = True
                    break
        if(check):#Если пользователь найден то переход на главное окно
            self.main = mainWindow.MainWindow(self.editLogin.text())
            self.main.show()
            self.hide()
        else:#Иначе сообщение, что таких пользователей нет
            QMessageBox.about(self, "Предупреждение", "Неправильный логин или пароль")
    #Процедура перехода на окно регистрации
    def regisrationWindow(self):
        self.registration = registrationWindow.Registration()
        self.registration.show()
        self.hide()
