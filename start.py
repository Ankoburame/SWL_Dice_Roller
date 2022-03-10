import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainUI(object):
    
    def openwindow(self):
        from attack_display import Ui_MainWindow
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def opendef(self):
        from defence_display import Ui_MainWindow
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def mainui(self, MainWindow):
        MainWindow.setObjectName("SWL System")
        MainWindow.resize(420,220)
        MainWindow.setWindowIcon(QtGui.QIcon('cross_lightsaber.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
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
        brush = QtGui.QBrush(QtGui.QColor(21, 67, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 67, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 67, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 10, 160, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.attackButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.attackButton.setObjectName("ATTAQUE")
        self.attackButton.setStyleSheet(
            "*{border: 2px solid '#D80818';" +
            "border-radius: 15px;" +
            "font-size: 15px;" +
            "color: 'white';" +
            "padding: 25px 0;" +
            "margin: 2px 2px;}" +
            "*:hover{background: #D80818;}"
        )
        self.attackButton.clicked.connect(self.openwindow)
        self.attackButton.clicked.connect(MainWindow.close)
        self.verticalLayout.addWidget(self.attackButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 60, 160, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.defenceButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.defenceButton.setObjectName("DEFENSE")
        self.defenceButton.setStyleSheet(
            "*{border: 2px solid '#208CE6';" +
            "border-radius: 15px;" +
            "font-size: 15px;" +
            "color: 'white';" +
            "padding: 25px 0;" +
            "margin: 2px 2px;}" +
            "*:hover{background: #208CE6;}"
        )
        self.defenceButton.clicked.connect(self.opendef)
        self.defenceButton.clicked.connect(MainWindow.close)
        self.verticalLayout_2.addWidget(self.defenceButton)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(250, 110, 160, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(250, 150, 160, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.quitterButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.quitterButton.setObjectName("QUITTER")
        self.quitterButton.setStyleSheet(
            "*{border: 2px solid '#EDFA53';" +
            "border-radius: 15px;" +
            "font-size: 15px;" +
            "color: 'white';" +
            "padding: 25px 0;" +
            "margin: 2px 2px;}" +
            "*:hover{background: #EDFA53;}"
        )
        self.quitterButton.clicked.connect(QCoreApplication.instance().quit)
        self.verticalLayout_4.addWidget(self.quitterButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 171))
        self.label.setObjectName("logo")
        imglogo=QPixmap("fond.png")
        imglogo=imglogo.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(imglogo)
        self.label.setStyleSheet("margin-top: 20px;")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SWL Dice Generator"))
        self.attackButton.setText(_translate("MainWindow", "ATTAQUE"))
        self.defenceButton.setText(_translate("MainWindow", "DEFENSE"))
        self.quitterButton.setText(_translate("MainWindow", "QUITTER"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainUI()
    ui.mainui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())