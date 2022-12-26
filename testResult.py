# This Python file uses the following encoding: utf-8
import mainWindow
from PyQt5.QtCore import QFile, QIODevice, QTextStream, QDateTime
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox


class TestResult(QWidget):
    def __init__(self, textTest, textResult, res, trueResult, name):
        super(TestResult, self).__init__()
        self.nameUser = name
        #Настройка окна
        self.setWindowTitle("Результаты")
        self.setWindowIcon(QIcon("./files/images/icon.png"))
        self.setMinimumSize(650,400)
        #---------------------------------

        result =[]
        i=0
        while i<10:
            if(res[i]):
                result.append("Верно")
            else:
                result.append("Неверно")
            i+=1

        #Запись результатов теста
        saveTestFile = QFile("./files/text/tests.txt")
        saveTestFile.open(QIODevice.Append)
        textStream = QTextStream(saveTestFile)
        textStream.setCodec("UTF-8")
        textStream<<"Пользователь "+self.nameUser+" ответил на "+str(trueResult)+" из 10 "+QDateTime.currentDateTime().toString()+"\n"
        saveTestFile.close()
        #---------------------------------

        #Расположение элементов окна
        layout = QVBoxLayout()
        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setRowCount(10)
        label = QLabel("Правильных ответов: "+str(trueResult)+" из 10")
        layoutButtons = QHBoxLayout()
        layout.addWidget(table)
        layout.addWidget(label)
        layout.addLayout(layoutButtons)
        self.setLayout(layout)
        newTestButton = QPushButton("Вернуться на главное меню", self, font = QFont('Franklin Gotic Book', 12))
        saveTestButton = QPushButton("Сохранить", self, font = QFont('Franklin Gotic Book', 12))
        layoutButtons.addWidget(newTestButton)
        layoutButtons.addWidget(saveTestButton)
        #---------------------------------

        #Подключение процедур к событию нажатия кнопки
        newTestButton.clicked.connect(self.mainWindow)
        saveTestButton.clicked.connect(self.saveResult)

        #Формирование строки для записи в файл
        self.stringResult=textTest[0]+" "+textResult[0]+" "+result[0]+"\n"+textTest[1]+" "+textResult[1]+" "+result[1]+"\n"+textTest[2]+" "+textResult[2]+" "+result[2]+"\n"+textTest[3]+" "+textResult[3]+" "+result[3]+"\n"+textTest[4]+" "+textResult[4]+" "+result[4]+"\n"+textTest[5]+" "+textResult[5]+" "+result[5]+"\n"+textTest[6]+" "+textResult[6]+" "+result[6]+"\n"+textTest[7]+" "+textResult[7]+" "+result[7]+"\n"+textTest[8]+" "+textResult[8]+" "+result[8]+"\n"+textTest[9]+" "+textResult[9]+" "+result[9]+"\n"

        #Заполнение таблицы результатов
        table.setItem(0,0,QTableWidgetItem(textTest[0]))
        table.setItem(0,1,QTableWidgetItem(textResult[0]))
        table.setItem(0,2,QTableWidgetItem(result[0]))
        table.setItem(1,0,QTableWidgetItem(textTest[1]))
        table.setItem(1,1,QTableWidgetItem(textResult[1]))
        table.setItem(1,2,QTableWidgetItem(result[1]))
        table.setItem(2,0,QTableWidgetItem(textTest[2]))
        table.setItem(2,1,QTableWidgetItem(textResult[2]))
        table.setItem(2,2,QTableWidgetItem(result[2]))
        table.setItem(3,0,QTableWidgetItem(textTest[3]))
        table.setItem(3,1,QTableWidgetItem(textResult[3]))
        table.setItem(3,2,QTableWidgetItem(result[3]))
        table.setItem(4,0,QTableWidgetItem(textTest[4]))
        table.setItem(4,1,QTableWidgetItem(textResult[4]))
        table.setItem(4,2,QTableWidgetItem(result[4]))
        table.setItem(5,0,QTableWidgetItem(textTest[5]))
        table.setItem(5,1,QTableWidgetItem(textResult[5]))
        table.setItem(5,2,QTableWidgetItem(result[5]))
        table.setItem(6,0,QTableWidgetItem(textTest[6]))
        table.setItem(6,1,QTableWidgetItem(textResult[6]))
        table.setItem(6,2,QTableWidgetItem(result[6]))
        table.setItem(7,0,QTableWidgetItem(textTest[7]))
        table.setItem(7,1,QTableWidgetItem(textResult[7]))
        table.setItem(7,2,QTableWidgetItem(result[7]))
        table.setItem(8,0,QTableWidgetItem(textTest[8]))
        table.setItem(8,1,QTableWidgetItem(textResult[8]))
        table.setItem(8,2,QTableWidgetItem(result[8]))
        table.setItem(9,0,QTableWidgetItem(textTest[9]))
        table.setItem(9,1,QTableWidgetItem(textResult[9]))
        table.setItem(9,2,QTableWidgetItem(result[9]))
        table.setColumnWidth(0,300)
        table.setColumnWidth(1,200)
        table.setColumnWidth(2,100)
        #---------------------------------

    #Процедура перехода на главное окно
    def mainWindow(self):
        self.main = mainWindow.MainWindow(self.nameUser)
        self.main.show()
        self.hide()

    #Процедура сохранения результатов
    def saveResult(self):
        #Открытие окна для выбора пути к файлу сохранения
        path=QFileDialog.getSaveFileName(self, "Save File", "C:/test.txt", "Text (*.txt)")
        if(path[0]!=''):
            file=QFile(path[0])
            file.open(QIODevice.WriteOnly)
            testStream = QTextStream(file)
            testStream.setCodec("UTF-8")
            testStream<<self.stringResult
            file.close()
        else:
            QMessageBox.about(self, "Предупреждение", "Файл не сохранен")
