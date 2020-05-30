# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\work\vscode\pyqt-camera-example\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 286)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sw_video = QtWidgets.QStackedWidget(self.centralwidget)
        self.sw_video.setObjectName("sw_video")
        self.w_video = QtWidgets.QWidget()
        self.w_video.setObjectName("w_video")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.w_video)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.v_video = Video(self.w_video)
        self.v_video.setObjectName("v_video")
        self.horizontalLayout_2.addWidget(self.v_video)
        self.sw_video.addWidget(self.w_video)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.sw_video.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.sw_video)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_start = QtWidgets.QPushButton(self.centralwidget)
        self.pb_start.setObjectName("pb_start")
        self.horizontalLayout.addWidget(self.pb_start)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.v_video.setText(_translate("MainWindow", "TextLabel"))
        self.pb_start.setText(_translate("MainWindow", "PushButton"))
from lib.video import Video
