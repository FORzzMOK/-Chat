#!python2
#!-*-coding: utf-8-*-

import sys
from threading import Thread
from PyQt4 import QtGui, QtCore
#from Safe import Tooltip
import socket
import host

StartStop = 'Start'
Messedge = ""

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
    	global StartStop
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

app = QtGui.QApplication(sys.argv)#создает объект приложения
tooltip = Tooltip()#Создает экземпляр класса
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def STARTSTOP():
	while True:
		if StartStop == 'Stop':
			sock.send("StopProgramm")
			sock.close()
			break

def START():
	sock.connect((host.ip, host.port))
	tooltip.textBrowser.append('Input your name')
	threadSockRecv = Thread(target=sockRecv, args=())
	threadSockRecv.start()
	threadSockRecv.join()
		
def sockRecv():
	while True:
		text = sock.recv(1024).decode('utf-8')
		tooltip.textBrowser.append(text)

def SendTextToBrowser():
	Messedge = tooltip.textEdit.toPlainText()
	sock.send(Messedge)
	tooltip.textEdit.clear()
	


def StartWidget():
	tooltip.show()#show() отображает наше окно на экране
	tooltip.pushButton.clicked.connect(SendTextToBrowser)
	app.exec_()#основной цикл нашей программы. Обработка сообщений начинается с этой строчки


thread_STARTCLIENT = Thread(target=START, args=())
thread_STARTSTOP = Thread(target=STARTSTOP, args=())

thread_STARTCLIENT.start()
thread_STARTSTOP.start()

StartWidget()

thread_STARTCLIENT.join()
thread_STARTSTOP.join()