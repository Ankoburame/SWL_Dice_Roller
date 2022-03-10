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
        MainWindow.setObjectName("Attaque")
        MainWindow.resize(410, 250)
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 20, 41, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.valueChanged.connect(self.system_attack)
        self.verticalLayout.addWidget(self.spinBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("d8white.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 41, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("d8black.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 41, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("d8red.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 80, 41, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.valueChanged.connect(self.system_attack)
        self.verticalLayout_2.addWidget(self.spinBox_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(90, 140, 41, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spinBox_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.valueChanged.connect(self.system_attack)
        self.verticalLayout_3.addWidget(self.spinBox_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(150, 120, 201, 61))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lancerButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.lancerButton.setObjectName("lancerButton")
        self.lancerButton.setStyleSheet(
        "*{border: 2px solid '#D80818';" +
        "border-radius: 5px;" +
        "font-size: 10px;" +
        "color: 'white';" +
        "padding: 15px 10px;" +
        "margin: 5px 0px;}" +
        "*:hover{background: #D80818;}"
        )
        self.lancerButton.clicked.connect(self.system_attack)
        self.lancerButton.clicked.connect(self.resultat)
        self.verticalLayout_4.addWidget(self.lancerButton)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(30, 200, 77, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.retourButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
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
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(310, 200, 77, 41))
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
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(160, 20, 231, 16))
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
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(160, 40, 131, 21))
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
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(160, 60, 131, 21))
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
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(160, 80, 131, 21))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 30, 211, 61))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet(
            "font-size: 8ps;" +
            "color: 'white';"
        )
        self.label_7.setAlignment(QtCore.Qt.AlignLeft)
        self.verticalLayout_10.addWidget(self.label_7)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(160, 100, 131, 21))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 30, 211, 61))
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet(
            "font-size: 8ps;" +
            "color: 'white';"
        )
        self.label_8.setAlignment(QtCore.Qt.AlignLeft)
        self.verticalLayout_11.addWidget(self.label_8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attaque"))
        self.lancerButton.setText(_translate("MainWindow", "LANCER"))
        self.retourButton.setText(_translate("MainWindow", "RETOUR"))
        self.quitterButton.setText(_translate("MainWindow", "QUITTER"))
        
        

    def system_attack(self):
        self.value_1=self.spinBox.value()
        self.value_2=self.spinBox_2.value()
        self.value_3=self.spinBox_3.value()
        if self.value_1 > 0:
            self.white_check(self.value_1)
        elif self.value_1 == 0:
            self.white_check(0)
        if self.value_2 > 0:
            self.black_check(self.value_2)
        elif self.value_2 == 0:
            self.black_check(0)
        if self.value_3 > 0:
            self.red_check(self.value_3)
        elif self.value_3 == 0:
            self.red_check(0)
        
    def white_check(self, value_1):
        
        pool=value_1
        whitepool=[]
        for dice in range(1, pool):
            dice=random.randint(1,8)
            whitepool.append(dice)
        global whitehit
        global whitecritic
        global whiteadrenaline
        global whitemiss
        whitehit=0
        whitecritic=0
        whiteadrenaline=0
        whitemiss=0
        for dice in whitepool:
            if dice == 7:
                whitehit +=1
        for dice in whitepool:
            if dice == 6:
                whitecritic += 1
        for dice in whitepool:
            if dice == 4:
                whiteadrenaline+=1
        for dice in whitepool:
            if dice == 1 or dice == 2 or dice == 3 or dice == 5 or dice == 8:
                whitemiss+=1
                
    def black_check(self, value_2):
        roll=value_2
        blackpool=[]
        for dice in range(0, roll):
            dice=random.randint(1,8)
            blackpool.append(dice)
        global blackhit
        global blackcritic
        global blackadrenaline
        global blackmiss
        blackhit=0
        blackcritic=0
        blackadrenaline=0
        blackmiss=0
        for dice in blackpool:
            if dice == 3 or dice == 4 or dice == 7:
                blackhit+=1
        for dice in blackpool:
            if dice == 2:
                blackcritic+=1
        for dice in blackpool:
            if dice == 6 :
                blackadrenaline+=1
        for dice in blackpool:
            if dice == 1 or dice == 5 or dice == 8:
                blackmiss+=1
                
    def red_check(self, value_3):
        roll=value_3
        redpool=[]
        for dice in range(0, roll):
            dice=random.randint(1,8)
            redpool.append(dice)
        global redhit
        global redcritic
        global redadrenaline
        global redmiss
        redhit=0
        redcritic=0
        redadrenaline=0
        redmiss=0
        for dice in redpool:
            if dice == 2 or dice == 3 or dice == 4 or dice == 6 or dice ==7:
                redhit+=1
        for dice in redpool:
            if dice == 5:
                redcritic+=1
        for dice in redpool:
            if dice == 8:
                redadrenaline+=1
        for dice in redpool:
            if dice == 1:
                redmiss+=1

    def resultat(self):
        self.hits=whitehit+blackhit+redhit
        self.critics=whitecritic+blackcritic+redcritic
        self.adrenalines=whiteadrenaline+blackadrenaline+redadrenaline
        self.misses=whitemiss+blackmiss+redmiss
        self.label_4.setText("Voici le résultat du jet:")
        self.label_5.setText("Touches: {}".format(self.hits))
        self.label_6.setText("Critiques: {}".format(self.critics))
        self.label_7.setText("Adrénalines: {}".format(self.adrenalines))
        self.label_8.setText("Manqués: {}".format(self.misses))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
