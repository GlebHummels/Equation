from PIL import Image
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QPixmap
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        '''Created by: PyQt5 UI code generator 5.13.0
        Файл .ui превращённый в .py'''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 656)
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 130, 501, 441))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 570, 399, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(740, 576, 93, 24))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setProperty("value", 15)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 570, 93, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 891, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 381, 351))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 510, 201, 23))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 570, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(50, 510, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.spinBox_2.setObjectName("spinBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClos = QtWidgets.QAction(MainWindow)
        self.actionClos.setObjectName("actionClos")
        self.menuFile.addAction(self.actionClos)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вычислятор 3000"))
        self.label.setText(_translate("MainWindow", "График"))
        self.label_2.setText(_translate("MainWindow", "Корень"))
        self.pushButton.setText(_translate("MainWindow", "Go!"))
        self.label_5.setText(_translate("MainWindow", "Программа для решения уравнений любых степеней"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "степень"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "коэффициент"))
        self.pushButton_2.setText(_translate("MainWindow", "Ввести данные в таблицу"))
        self.label_6.setText(_translate("MainWindow", "Масштаб"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionClos.setText(_translate("MainWindow", "Close"))

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('math.ui', self)
        self.pushButton.clicked.connect(self.result)
        self.actionClos.triggered.connect(self.close)
        self.spinBox_2.valueChanged.connect(self.update_table)
        self.base = sqlite3.connect("math.db")
        self.data = self.base.cursor()

    def update_table(self):
        #Обновление таблицы
        self.tableWidget.setRowCount(0)
        if not self.spinBox_2.text().isdigit():
            return
        num = int(self.spinBox_2.text()) + 1
        for i in range(num):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(num - i - 1)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem('enter'))
        self.tableWidget.resizeColumnsToContents()

    def result(self):
        #Сборка информации с таблицы
        nums = []
        for i in range(self.tableWidget.rowCount()):
            nums.append(str(self.tableWidget.item(i, 1).text()))
        nums = ' '.join(nums)
        self.nums = nums
        self.ur(self.nums)

    def ris(self, nums):
        #Начало рисования графика
        s = nums.split()
        s = [int(s[i]) for i in range(len(s))]
        k = int(self.spinBox.text())
        s.reverse()
        im = Image.new('RGB', (400, 400), (255, 255, 255))
        pixels = im.load()
        for i in range(400):
            pixels[i, 200] = (255, 0, 0)
            pixels[200, i] = (255, 0, 0)
        for x in range(-200, 200, 1):
            x /= k
            pix = [x * k + 200, -(sum([s[i] * x ** i for i in range(len(s))]) * k) + 200]
            if 0 < pix[0] < 400 and 0 < pix[1] < 400:
                pixels[pix[0], pix[1]] = (0, 0, 0)
        #Конец рисования графика
        name = nums
        im.save(f'img/{name}.png')
        self.pixmap = QPixmap(f'img/{name}.png')
        self.label.setPixmap(self.pixmap)
        que = f"""insert into data(title, img) values('{nums}', 'img/{nums}.png')"""
        #Добавление фото в SQL
        self.data.execute(que)
        self.base.commit()

    def ur(self, nums):
        #Функция решения уравнения
        s = nums.split()
        s = [int(s[i]) for i in range(len(s))]
        s.reverse()
        x = 0
        l = 10000
        i = 0
        p = True
        y = sum([s[i] ** i for i in range(len(s))])
        if s[0] == 0:
            p = False
        while p:
            i += 1
            if sum([s[i] * x ** i for i in range(len(s))]) > 0:
                x -= l / 2 ** i
            elif sum([s[i] * x ** i for i in range(len(s))]) < 0:
                x += l / 2 ** i
            else:
                p = False
            if i == 5000:
                p = False
        if x == l or x == -l:
            x = 'Корень мнимый или не существует или бесконечность'
        self.label_2.setText(str(x))
        self.ris(self.nums)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())