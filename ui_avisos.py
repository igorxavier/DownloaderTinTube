# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'avisos.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(645, 325)
        icon = QIcon()
        icon.addFile(u"icons/savevideo.ico", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(u"*{\n"
"	background-color: rgb(26, 26, 26);\n"
"}\n"
"QLineEdit, QPushButton, QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	border-radius: 5;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(108, 108, 108);\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(225, 225, 225);\n"
"	color: rgb(68, 68, 68);\n"
"}\n"
"a{\n"
"	color: rgb(85, 255, 127);\n"
"}")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_msg = QLabel(self.centralwidget)
        self.lbl_msg.setObjectName(u"lbl_msg")
        font = QFont()
        font.setPointSize(16)
        self.lbl_msg.setFont(font)
        self.lbl_msg.setStyleSheet(u"color: rgb(85, 170, 127);")
        self.lbl_msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_msg)

        self.lbl_link = QLabel(self.centralwidget)
        self.lbl_link.setObjectName(u"lbl_link")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setUnderline(True)
        self.lbl_link.setFont(font1)
        self.lbl_link.setCursor(QCursor(Qt.PointingHandCursor))
        self.lbl_link.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.lbl_link.setAlignment(Qt.AlignCenter)
        self.lbl_link.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.lbl_link)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Avisos Do Sistema", None))
        self.lbl_msg.setText(QCoreApplication.translate("mainWindow", u"TextLabel", None))
        self.lbl_link.setText(QCoreApplication.translate("mainWindow", u"TextLabel", None))
    # retranslateUi

