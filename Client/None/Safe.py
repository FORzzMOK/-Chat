#!python2
#!-*-coding: utf-8-*-

import sys
from PyQt4 import QtGui, QtCore
#from client import StartStop
class Tooltip(QtGui.QWidget):#мы создаем класс. Этот класс мы объявляем производным от класса QtGui.QWidget.
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)#Теперь мы вызываем конструктор класса-родителя и передаем туда в качестве параметров указатель на наш класс и указатель на родителя класса 

        #self.setGeometry(300, 300, 700, 400)#задает местоположение нашего окна и его размеры. 
        self.resize(400, 300)#размер окна
        self.setWindowTitle('Tooltip')#название окна
        self.setWindowIcon(QtGui.QIcon('500_F_1'))#определение иконки нашего приложения
        self.center()
        self.pushButton = QtGui.QPushButton("Send",self)
        self.pushButton.setGeometry(310, 240, 81, 51)
        self.pushButton.setObjectName("Send")
        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.isBackwardAvailable()
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 240, 291, 51))
        self.textEdit.setObjectName("textEdit")
        
    def closeEvent(self, event):#функция создает окно с сообщением.
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            StartStop = 'Stop'
            event.accept()
        elif reply == QtGui.QMessageBox.No:
            event.ignore()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()#получаем разрешение нашего дисплея
        size =  self.geometry()#размер нашего окна
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)#расчитываем центр дисплея

        #self.setToolTip('This is a <b>QWidget</b> widget')#контекстная подсказка
        #QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))#Исправляет шрифт подсказки