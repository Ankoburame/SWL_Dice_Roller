import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random


class Ui_MainWindow(object):
    
    def openwindow(self):
        from start import MainUI
        self.window=QtWidgets.QMainWindow()
        self.ui=MainUI()
        self.ui.mainui(self.window)
        self.window.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 270)
        MainWindow.setWindowIcon(QtGui.QIcon('cross_lightsaber.png'))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 18, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 18, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 18, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 18, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 20, 41, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 80, 41, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_2.addWidget(self.spinBox_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("d6white.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 41, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("d6red.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(50, 140, 231, 61))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lancerButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.lancerButton.setObjectName("lancerButton")
        self.lancerButton.setStyleSheet(
        "*{border: 2px solid '#208CE6';" +
        "border-radius: 5px;" +
        "font-size: 10px;" +
        "color: 'white';" +
        "padding: 15px 10px;" +
        "margin: 5px 0px;}" +
        "*:hover{background: #208CE6;}"
        )
        self.lancerButton.clicked.connect(self.system_defence)
        self.lancerButton.clicked.connect(self.resultat)
        self.verticalLayout_4.addWidget(self.lancerButton)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 210, 77, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.retourButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.retourButton.setPalette(palette)
        self.retourButton.setObjectName("retourButton")
        self.retourButton.setStyleSheet(
        "*{border: 2px solid '#41DB3A';" +
        "border-radius: 5px;" +
        "font-size: 10px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 10px 0px;}" +
        "*:hover{background: #41DB3A;}"
        )
        self.retourButton.clicked.connect(self.openwindow)
        self.retourButton.clicked.connect(MainWindow.close)
        self.verticalLayout_5.addWidget(self.retourButton)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(240, 210, 77, 41))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.quitterButton = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.quitterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quitterButton.setObjectName("quitterButton")
        self.quitterButton.setStyleSheet(
        "*{border: 2px solid '#EDFA53';" +
        "border-radius: 5px;" +
        "font-size: 10px;" +
        "color: 'white';" +
        "padding: 15px 0px;" +
        "margin: 10px 0px;}" +
        "*:hover{background: #EDFA53;}"
        )
        self.quitterButton.clicked.connect(QCoreApplication.instance().quit)
        self.verticalLayout_6.addWidget(self.quitterButton)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(140, 20, 181, 31))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 211, 61))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet(
            "font-size: 8ps;" +
            "color: 'white';"
        )
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(140, 50, 181, 31))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 30, 211, 61))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet(
            "font-size: 8ps;" +
            "color: 'white';"
        )
        self.label_4.setAlignment(QtCore.Qt.AlignLeft)
        self.verticalLayout_7.addWidget(self.label_4)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(140, 80, 181, 31))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 30, 211, 61))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet(
            "font-size: 8ps;" +
            "color: 'white';"
        )
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.verticalLayout_8.addWidget(self.label_5)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(140, 110, 181, 31))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 30, 211, 61))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet(
            "font-size: 8ps;" +
            "color: 'white';"
        )
        self.label_6.setAlignment(QtCore.Qt.AlignLeft)
        self.verticalLayout_9.addWidget(self.label_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Défense"))
        self.lancerButton.setText(_translate("MainWindow", "LANCER"))
        self.retourButton.setText(_translate("MainWindow", "RETOUR"))
        self.quitterButton.setText(_translate("MainWindow", "QUITTER"))
        
    def system_defence(self):
        self.value_1=self.spinBox.value()
        self.value_2=self.spinBox_2.value()
        if self.value_1 > 0:
            self.white_check(self.value_1)
        elif self.value_1 == 0:
            self.white_check(0)
        if self.value_2 > 0:
            self.red_check(self.value_2)
        elif self.value_2 == 0:
            self.red_check(0)
            
    def white_check(self, value_1):
        
        pool=value_1
        whitepool=[]
        for dice in range(1, pool):
            dice=random.randint(1,6)
            whitepool.append(dice)
        global whiteprotec
        global whiteadrenaline
        global whitemiss
        whiteprotec=0
        whiteadrenaline=0
        whitemiss=0
        for dice in whitepool:
            if dice == 5:
                whiteprotec +=1
        for dice in whitepool:
            if dice == 6:
                whiteadrenaline+=1
        for dice in whitepool:
            if dice == 1 or dice == 2 or dice == 3 or dice == 4:
                whitemiss+=1
    
    def red_check(self, value_3):
        roll=value_3
        redpool=[]
        for dice in range(0, roll):
            dice=random.randint(1,6)
            redpool.append(dice)
        global redprotec
        global redadrenaline
        global redmiss
        redprotec=0
        redadrenaline=0
        redmiss=0
        for dice in redpool:
            if dice == 4 or dice == 5 or dice == 6:
                redprotec+=1
        for dice in redpool:
            if dice == 2:
                redadrenaline+=1
        for dice in redpool:
            if dice == 1 or dice == 3:
                redmiss+=1
                
    def resultat(self):
        self.protects=whiteprotec+redprotec
        self.adrenalines=whiteadrenaline+redadrenaline
        self.misses=whitemiss+redmiss
        self.label_3.setText("Voici le résultat du jet:")
        self.label_4.setText("Touches: {}".format(self.protects))
        self.label_5.setText("Adrénalines: {}".format(self.adrenalines))
        self.label_6.setText("Manqués: {}".format(self.misses))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
