# This Python file uses the following encoding: utf-8
import random
import mainWindow
import testResult
from PyQt5.QtCore import Qt, QFile, QIODevice, QTextStream, QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QToolBox, QGroupBox, QRadioButton, QSizePolicy


class TestWindow(QWidget):
    def __init__(self, name):
        QWidget.__init__(self)
        self.nameUser = name
        #Настройка окна
        self.setWindowTitle("Тест")
        self.setWindowIcon(QIcon("./files/images/icon.png"))
        self.setFixedSize(1024,550)
        #---------------------------------

        #Считывание вопросов
        teoryFile = QFile("./files/text/questions.txt")
        teoryFile.open(QIODevice.ReadOnly)
        textStream = QTextStream(teoryFile)
        allText = textStream.readAll()
        teoryFile.close()
        questions = allText.split("\n")
        #---------------------------------

        #Перемешивание вопросов и отбор 10
        allQuestions = range(0,16)
        self.listQuestions=random.sample(allQuestions,10)
        #---------------------------------

        #Расположение элементов окна
        answers = questions[self.listQuestions[0]].split(";")
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(25,25,25,25)
        self.setLayout(mainLayout)
        toolBox=QToolBox()
        mainLayout.addWidget(toolBox)
        Question1 = QWidget()
        toolBox.addItem(Question1,"Задание 1")
        layoutQuestion1 = QVBoxLayout()
        Question1.setLayout(layoutQuestion1)
        label1 = QLabel(answers[0],font = QFont('Franklin Gotic Book', 14))
        layoutQuestion1.addWidget(label1)

        self.groupBox1 = QGroupBox()
        radioLayout1 = QVBoxLayout()
        self.radio1_1 = QRadioButton(answers[1],font = QFont('Aria', 12))
        self.radio1_2 = QRadioButton(answers[2],font = QFont('Aria', 12))
        self.radio1_3 = QRadioButton(answers[3],font = QFont('Aria', 12))
        radioLayout1.addWidget(self.radio1_1)
        radioLayout1.addWidget(self.radio1_2)
        radioLayout1.addWidget(self.radio1_3)
        self.groupBox1.setLayout(radioLayout1)
        layoutQuestion1.addWidget(self.groupBox1)


        answers = questions[self.listQuestions[1]].split(";")
        Question2 = QWidget()
        toolBox.addItem(Question2,"Задание 2")
        layoutQuestion2 = QVBoxLayout()
        Question2.setLayout(layoutQuestion2)
        label2 = QLabel(answers[0],font = QFont('Franklin Gotic Book', 14))
        layoutQuestion2.addWidget(label2)

        self.groupBox2 = QGroupBox()
        radioLayout2 = QVBoxLayout()
        self.radio2_1 = QRadioButton(answers[1],font = QFont('Aria', 12))
        self.radio2_2 = QRadioButton(answers[2],font = QFont('Aria', 12))
        self.radio2_3 = QRadioButton(answers[3],font = QFont('Aria', 12))
        radioLayout2.addWidget(self.radio2_1)
        radioLayout2.addWidget(self.radio2_2)
        radioLayout2.addWidget(self.radio2_3)
        self.groupBox2.setLayout(radioLayout2)
        layoutQuestion2.addWidget(self.groupBox2)

        answers = questions[self.listQuestions[2]].split(";")
        Question3 = QWidget()
        toolBox.addItem(Question3,"Задание 3")
        layoutQuestion3 = QVBoxLayout()
        Question3.setLayout(layoutQuestion3)
        label3 = QLabel(answers[0],font = QFont('Franklin Gotic Book', 14))
        layoutQuestion3.addWidget(label3)

        self.groupBox3 = QGroupBox()
        radioLayout3 = QVBoxLayout()
        self.radio3_1 = QRadioButton(answers[1],font = QFont('Aria', 12))
        self.radio3_2 = QRadioButton(answers[2],font = QFont('Aria', 12))
        self.radio3_3 = QRadioButton(answers[3],font = QFont('Aria', 12))
        radioLayout3.addWidget(self.radio3_1)
        radioLayout3.addWidget(self.radio3_2)
        radioLayout3.addWidget(self.radio3_3)
        self.groupBox3.setLayout(radioLayout3)
        layoutQuestion3.addWidget(self.groupBox3)

        answers = questions[self.listQuestions[3]].split(";")
        Question4 = QWidget()
        toolBox.addItem(Question4,"Задание 4")
        layoutQuestion4 = QVBoxLayout()
        Question4.setLayout(layoutQuestion4)
        label4 = QLabel(answers[0],font = QFont('Franklin Gotic Book', 14))
        layoutQuestion4.addWidget(label4)

        self.groupBox4 = QGroupBox()
        radioLayout4 = QVBoxLayout()
        self.radio4_1 = QRadioButton(answers[1],font = QFont('Aria', 12))
        self.radio4_2 = QRadioButton(answers[2],font = QFont('Aria', 12))
        self.radio4_3 = QRadioButton(answers[3],font = QFont('Aria', 12))
        radioLayout4.addWidget(self.radio4_1)
        radioLayout4.addWidget(self.radio4_2)
        radioLayout4.addWidget(self.radio4_3)
        self.groupBox4.setLayout(radioLayout4)
        layoutQuestion4.addWidget(self.groupBox4)

        answers = questions[self.listQuestions[4]].split(";")
        Question5 = QWidget()
        toolBox.addItem(Question5,"Задание 5")
        layoutQuestion5 = QVBoxLayout()
        Question5.setLayout(layoutQuestion5)
        label5 = QLabel(answers[0],font = QFont('Franklin Gotic Book', 14))
        layoutQuestion5.addWidget(label5)

        self.groupBox5 = QGroupBox()
        radioLayout5 = QVBoxLayout()
        self.radio5_1 = QRadioButton(answers[1],font = QFont('Aria', 12))
        self.radio5_2 = QRadioButton(answers[2],font = QFont('Aria', 12))
        self.radio5_3 = QRadioButton(answers[3],font = QFont('Aria', 12))
        radioLayout5.addWidget(self.radio5_1)
        radioLayout5.addWidget(self.radio5_2)
        radioLayout5.addWidget(self.radio5_3)
        self.groupBox5.setLayout(radioLayout5)
        layoutQuestion5.addWidget(self.groupBox5)

        answers = questions[self.listQuestions[5]].split(";")
        Question6 = QWidget()
        toolBox.addItem(Question6,"Задание 6")
        layoutQuestion6 = QVBoxLayout()
        Question6.setLayout(layoutQuestion6)
        label6 = QLabel(answers[0],font = QFont('Franklin Gotic Book', 14))
        layoutQuestion6.addWidget(label6)

        self.groupBox6 = QGroupBox()
        radioLayout6 = QVBoxLayout()
        self.radio6_1 = QRadioButton(answers[1],font = QFont('Aria', 12))
        self.radio6_2 = QRadioButton(answers[2],font = QFont('Aria', 12))
        self.radio6_3 = QRadioButton(answers[3],font = QFont('Aria', 12))
        radioLayout6.addWidget(self.radio6_1)
        radioLayout6.addWidget(self.radio6_2)
        radioLayout6.addWidget(self.radio6_3)
        self.groupBox6.setLayout(radioLayout6)
        layoutQuestion6.addWidget(self.groupBox6)

        answers = questions[self.listQuestions[6]].split(";")
        Question7 = QWidget()
        toolBox.addItem(Question7,"Задание 7")
        layoutQuestion7 = QVBoxLayout()
        Question7.setLayout(layoutQuestion7)
        label7 = QLabel(answers[0],font = QFont('Franklin Gotic Book', 14))
        layoutQuestion7.addWidget(label7)

        self.groupBox7 = QGroupBox()
        radioLayout7 = QVBoxLayout()
        self.radio7_1 = QRadioButton(answers[1],font = QFont('Aria', 12))
        self.radio7_2 = QRadioButton(answers[2],font = QFont('Aria', 12))
        self.radio7_3 = QRadioButton(answers[3],font = QFont('Aria', 12))
        radioLayout7.addWidget(self.radio7_1)
        radioLayout7.addWidget(self.radio7_2)
        radioLayout7.addWidget(self.radio7_3)
        self.groupBox7.setLayout(radioLayout7)
        layoutQuestion7.addWidget(self.groupBox7)

        answers = questions[self.listQuestions[7]].split(";")
        Question8 = QWidget()
        toolBox.addItem(Question8,"Задание 8")
        layoutQuestion8 = QVBoxLayout()
        Question8.setLayout(layoutQuestion8)
        label8 = QLabel(answers[0],font = QFont('Franklin Gotic Book', 14))
        layoutQuestion8.addWidget(label8)

        self.groupBox8 = QGroupBox()
        radioLayout8 = QVBoxLayout()
        self.radio8_1 = QRadioButton(answers[1],font = QFont('Aria', 12))
        self.radio8_2 = QRadioButton(answers[2],font = QFont('Aria', 12))
        self.radio8_3 = QRadioButton(answers[3],font = QFont('Aria', 12))
        radioLayout8.addWidget(self.radio8_1)
        radioLayout8.addWidget(self.radio8_2)
        radioLayout8.addWidget(self.radio8_3)
        self.groupBox8.setLayout(radioLayout8)
        layoutQuestion8.addWidget(self.groupBox8)

        answers = questions[self.listQuestions[8]].split(";")
        Question9 = QWidget()
        toolBox.addItem(Question9,"Задание 9")
        layoutQuestion9 = QVBoxLayout()
        Question9.setLayout(layoutQuestion9)
        label9 = QLabel(answers[0],font = QFont('Franklin Gotic Book', 14))
        layoutQuestion9.addWidget(label9)

        self.groupBox9 = QGroupBox()
        radioLayout9 = QVBoxLayout()
        self.radio9_1 = QRadioButton(answers[1],font = QFont('Aria', 12))
        self.radio9_2 = QRadioButton(answers[2],font = QFont('Aria', 12))
        self.radio9_3 = QRadioButton(answers[3],font = QFont('Aria', 12))
        radioLayout9.addWidget(self.radio9_1)
        radioLayout9.addWidget(self.radio9_2)
        radioLayout9.addWidget(self.radio9_3)
        self.groupBox9.setLayout(radioLayout9)
        layoutQuestion9.addWidget(self.groupBox9)

        answers = questions[self.listQuestions[9]].split(";")
        Question10 = QWidget()
        toolBox.addItem(Question10,"Задание 10")
        layoutQuestion10 = QVBoxLayout()
        Question10.setLayout(layoutQuestion10)
        label10 = QLabel(answers[0],font = QFont('Franklin Gotic Book', 14))
        layoutQuestion10.addWidget(label10)

        self.groupBox10 = QGroupBox()
        radioLayout10 = QVBoxLayout()
        self.radio10_1 = QRadioButton(answers[1],font = QFont('Aria', 12))
        self.radio10_2 = QRadioButton(answers[2],font = QFont('Aria', 12))
        self.radio10_3 = QRadioButton(answers[3],font = QFont('Aria', 12))
        radioLayout10.addWidget(self.radio10_1)
        radioLayout10.addWidget(self.radio10_2)
        radioLayout10.addWidget(self.radio10_3)
        self.groupBox10.setLayout(radioLayout10)
        layoutQuestion10.addWidget(self.groupBox10)

        buttonBack=QPushButton("Назад", self, font = QFont('Franklin Gotic Book', 12), sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(150,30))
        buttonResult=QPushButton("Результаты", self, font = QFont('Franklin Gotic Book', 12),sizePolicy=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed), minimumSize=QSize(150,30))
        layoutButtons=QHBoxLayout()
        layoutButtons.setContentsMargins(25,10,25,10)
        layoutButtons.addWidget(buttonBack, 0, Qt.AlignLeft)
        layoutButtons.addWidget(buttonResult, 0, Qt.AlignRight)
        mainLayout.addLayout(layoutButtons)
        #---------------------------------

        #Подключение процедур к событию нажатия кнопки
        buttonBack.clicked.connect(self.backWindow)
        buttonResult.clicked.connect(self.calculResult)

        #Подключение процедур к событию нажатия радио кнопки
        self.radio1_1.clicked.connect(self.radioSlot1)
        self.radio1_2.clicked.connect(self.radioSlot1)
        self.radio1_3.clicked.connect(self.radioSlot1)

        self.radio2_1.clicked.connect(self.radioSlot2)
        self.radio2_2.clicked.connect(self.radioSlot2)
        self.radio2_3.clicked.connect(self.radioSlot2)

        self.radio3_1.clicked.connect(self.radioSlot3)
        self.radio3_2.clicked.connect(self.radioSlot3)
        self.radio3_3.clicked.connect(self.radioSlot3)

        self.radio4_1.clicked.connect(self.radioSlot4)
        self.radio4_2.clicked.connect(self.radioSlot4)
        self.radio4_3.clicked.connect(self.radioSlot4)

        self.radio5_1.clicked.connect(self.radioSlot5)
        self.radio5_2.clicked.connect(self.radioSlot5)
        self.radio5_3.clicked.connect(self.radioSlot5)

        self.radio6_1.clicked.connect(self.radioSlot6)
        self.radio6_2.clicked.connect(self.radioSlot6)
        self.radio6_3.clicked.connect(self.radioSlot6)

        self.radio7_1.clicked.connect(self.radioSlot7)
        self.radio7_2.clicked.connect(self.radioSlot7)
        self.radio7_3.clicked.connect(self.radioSlot7)

        self.radio8_1.clicked.connect(self.radioSlot8)
        self.radio8_2.clicked.connect(self.radioSlot8)
        self.radio8_3.clicked.connect(self.radioSlot8)

        self.radio9_1.clicked.connect(self.radioSlot9)
        self.radio9_2.clicked.connect(self.radioSlot9)
        self.radio9_3.clicked.connect(self.radioSlot9)

        self.radio10_1.clicked.connect(self.radioSlot10)
        self.radio10_2.clicked.connect(self.radioSlot10)
        self.radio10_3.clicked.connect(self.radioSlot10)
        #---------------------------------

    #Процедуры блокировки радио кнопок одной группы
    def radioSlot1(self):
        self.radio1_1.setEnabled(False)
        self.radio1_2.setEnabled(False)
        self.radio1_3.setEnabled(False)

    def radioSlot2(self):
        self.radio2_1.setEnabled(False)
        self.radio2_2.setEnabled(False)
        self.radio2_3.setEnabled(False)

    def radioSlot3(self):
        self.radio3_1.setEnabled(False)
        self.radio3_2.setEnabled(False)
        self.radio3_3.setEnabled(False)

    def radioSlot4(self):
        self.radio4_1.setEnabled(False)
        self.radio4_2.setEnabled(False)
        self.radio4_3.setEnabled(False)

    def radioSlot5(self):
        self.radio5_1.setEnabled(False)
        self.radio5_2.setEnabled(False)
        self.radio5_3.setEnabled(False)

    def radioSlot6(self):
        self.radio6_1.setEnabled(False)
        self.radio6_2.setEnabled(False)
        self.radio6_3.setEnabled(False)

    def radioSlot7(self):
        self.radio7_1.setEnabled(False)
        self.radio7_2.setEnabled(False)
        self.radio7_3.setEnabled(False)

    def radioSlot8(self):
        self.radio8_1.setEnabled(False)
        self.radio8_2.setEnabled(False)
        self.radio8_3.setEnabled(False)

    def radioSlot9(self):
        self.radio9_1.setEnabled(False)
        self.radio9_2.setEnabled(False)
        self.radio9_3.setEnabled(False)

    def radioSlot10(self):
        self.radio10_1.setEnabled(False)
        self.radio10_2.setEnabled(False)
        self.radio10_3.setEnabled(False)
    #---------------------------------

    #Процедура перехода на главное окно
    def backWindow(self):
        self.back = mainWindow.MainWindow(self.nameUser)
        self.back.show()
        self.hide()

    def calculResult(self):
        #Переменные результатов
        res =[False,False,False,False,False,False,False,False,False,False]
        trueRes=0
        textTest=[]
        textResult=[]

        #Считывание ответов
        teoryFile = QFile("./files/text/questions.txt")
        teoryFile.open(QIODevice.ReadOnly)
        textStream = QTextStream(teoryFile)
        allText = textStream.readAll()
        teoryFile.close()
        questions = allText.split("\n")
        answers = questions[self.listQuestions[0]].split(";")
        #---------------------------------

        #Добавление ответов и вопросов
        textTest.append(answers[0])
        if(self.radio1_1.isChecked()==True):
            textResult.append(self.radio1_1.text())
        elif(self.radio1_2.isChecked()==True):
            textResult.append(self.radio1_2.text())
        else:
            textResult.append(self.radio1_3.text())
        #---------------------------------

        #Проверка правильности выбранных решений
        if(answers[4]=="1\r" and self.radio1_1.isChecked()==True):
            res[0]=True
            trueRes+=1
        elif(answers[4]=="2\r" and self.radio1_2.isChecked()==True):
            res[0]=True
            trueRes+=1
        elif(answers[4]=="3\r" and self.radio1_3.isChecked()==True):
            res[0]=True
            trueRes+=1

        answers = questions[self.listQuestions[1]].split(";")
        textTest.append(answers[0])
        if(self.radio2_1.isChecked()==True):
            textResult.append(self.radio2_1.text())
        elif(self.radio2_2.isChecked()==True):
            textResult.append(self.radio2_2.text())
        else:
            textResult.append(self.radio2_3.text())

        if(answers[4]=="1\r" and self.radio2_1.isChecked()==True):
            res[1]=True
            trueRes+=1
        elif(answers[4]=="2\r" and self.radio2_2.isChecked()==True):
            res[1]=True
            trueRes+=1
        elif(answers[4]=="3\r" and self.radio2_3.isChecked()==True):
            res[1]=True
            trueRes+=1

        answers = questions[self.listQuestions[2]].split(";")
        textTest.append(answers[0])
        if(self.radio3_1.isChecked()==True):
            textResult.append(self.radio3_1.text())
        elif(self.radio3_2.isChecked()==True):
            textResult.append(self.radio3_2.text())
        else:
            textResult.append(self.radio3_3.text())

        if(answers[4]=="1\r" and self.radio3_1.isChecked()==True):
            res[2]=True
            trueRes+=1
        elif(answers[4]=="2\r" and self.radio3_2.isChecked()==True):
            res[2]=True
            trueRes+=1
        elif(answers[4]=="3\r" and self.radio3_3.isChecked()==True):
            res[2]=True
            trueRes+=1

        answers = questions[self.listQuestions[3]].split(";")
        textTest.append(answers[0])
        if(self.radio4_1.isChecked()==True):
            textResult.append(self.radio4_1.text())
        elif(self.radio4_2.isChecked()==True):
            textResult.append(self.radio4_2.text())
        else:
            textResult.append(self.radio4_3.text())

        if(answers[4]=="1\r" and self.radio4_1.isChecked()==True):
            res[3]=True
            trueRes+=1
        elif(answers[4]=="2\r" and self.radio4_2.isChecked()==True):
            res[3]=True
            trueRes+=1
        elif(answers[4]=="3\r" and self.radio4_3.isChecked()==True):
            res[3]=True
            trueRes+=1

        answers = questions[self.listQuestions[4]].split(";")
        textTest.append(answers[0])
        if(self.radio5_1.isChecked()==True):
            textResult.append(self.radio5_1.text())
        elif(self.radio5_2.isChecked()==True):
            textResult.append(self.radio5_2.text())
        else:
            textResult.append(self.radio5_3.text())

        if(answers[4]=="1\r" and self.radio5_1.isChecked()==True):
            res[4]=True
            trueRes+=1
        elif(answers[4]=="2\r" and self.radio5_2.isChecked()==True):
            res[4]=True
            trueRes+=1
        elif(answers[4]=="3\r" and self.radio5_3.isChecked()==True):
            res[4]=True
            trueRes+=1

        answers = questions[self.listQuestions[5]].split(";")
        textTest.append(answers[0])
        if(self.radio6_1.isChecked()==True):
            textResult.append(self.radio6_1.text())
        elif(self.radio6_2.isChecked()==True):
            textResult.append(self.radio6_2.text())
        else:
            textResult.append(self.radio6_3.text())

        if(answers[4]=="1\r" and self.radio6_1.isChecked()==True):
            res[5]=True
            trueRes+=1
        elif(answers[4]=="2\r" and self.radio6_2.isChecked()==True):
            res[5]=True
            trueRes+=1
        elif(answers[4]=="3\r" and self.radio6_3.isChecked()==True):
            res[5]=True
            trueRes+=1

        answers = questions[self.listQuestions[6]].split(";")
        textTest.append(answers[0])
        if(self.radio7_1.isChecked()==True):
            textResult.append(self.radio7_1.text())
        elif(self.radio7_2.isChecked()==True):
            textResult.append(self.radio7_2.text())
        else:
            textResult.append(self.radio7_3.text())

        if(answers[4]=="1\r" and self.radio7_1.isChecked()==True):
            res[6]=True
            trueRes+=1
        elif(answers[4]=="2\r" and self.radio7_2.isChecked()==True):
            res[6]=True
            trueRes+=1
        elif(answers[4]=="3\r" and self.radio7_3.isChecked()==True):
            res[6]=True
            trueRes+=1

        answers = questions[self.listQuestions[7]].split(";")
        textTest.append(answers[0])
        if(self.radio8_1.isChecked()==True):
            textResult.append(self.radio8_1.text())
        elif(self.radio8_2.isChecked()==True):
            textResult.append(self.radio8_2.text())
        else:
            textResult.append(self.radio8_3.text())

        if(answers[4]=="1\r" and self.radio8_1.isChecked()==True):
            res[7]=True
            trueRes+=1
        elif(answers[4]=="2\r" and self.radio8_2.isChecked()==True):
            res[7]=True
            trueRes+=1
        elif(answers[4]=="3\r" and self.radio8_3.isChecked()==True):
            res[7]=True
            trueRes+=1

        answers = questions[self.listQuestions[8]].split(";")
        textTest.append(answers[0])
        if(self.radio9_1.isChecked()==True):
            textResult.append(self.radio9_1.text())
        elif(self.radio9_2.isChecked()==True):
            textResult.append(self.radio9_2.text())
        else:
            textResult.append(self.radio9_3.text())

        if(answers[4]=="1\r" and self.radio9_1.isChecked()==True):
            res[8]=True
            trueRes+=1
        elif(answers[4]=="2\r" and self.radio9_2.isChecked()==True):
            res[8]=True
            trueRes+=1
        elif(answers[4]=="3\r" and self.radio9_3.isChecked()==True):
            res[8]=True
            trueRes+=1

        answers = questions[self.listQuestions[9]].split(";")
        textTest.append(answers[0])
        if(self.radio10_1.isChecked()==True):
            textResult.append(self.radio10_1.text())
        elif(self.radio10_2.isChecked()==True):
            textResult.append(self.radio10_2.text())
        else:
            textResult.append(self.radio10_3.text())

        if(answers[4]=="1\r" and self.radio10_1.isChecked()==True):
            res[9]=True
            trueRes+=1
        elif(answers[4]=="2\r" and self.radio10_2.isChecked()==True):
            res[9]=True
            trueRes+=1
        elif(answers[4]=="3\r" and self.radio10_3.isChecked()==True):
            res[9]=True
            trueRes+=1
        #---------------------------------

        #Переход на окно результатов
        self.winRes=testResult.TestResult(textTest, textResult, res, trueRes, self.nameUser)
        self.winRes.show()
        self.hide()
