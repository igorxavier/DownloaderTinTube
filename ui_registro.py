# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(551, 308)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icons/savevideo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
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
"}")
        MainWindow.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, 20)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.label)

        self.edit_nome = QLineEdit(self.widget_2)
        self.edit_nome.setObjectName(u"edit_nome")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.edit_nome.sizePolicy().hasHeightForWidth())
        self.edit_nome.setSizePolicy(sizePolicy3)
        self.edit_nome.setMinimumSize(QSize(0, 30))
        self.edit_nome.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(10)
        self.edit_nome.setFont(font1)

        self.verticalLayout_3.addWidget(self.edit_nome)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.label_2)

        self.edit_email = QLineEdit(self.widget_2)
        self.edit_email.setObjectName(u"edit_email")
        self.edit_email.setMinimumSize(QSize(0, 30))
        self.edit_email.setFont(font1)

        self.verticalLayout_3.addWidget(self.edit_email)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_registrar = QPushButton(self.widget_2)
        self.btn_registrar.setObjectName(u"btn_registrar")
        sizePolicy3.setHeightForWidth(self.btn_registrar.sizePolicy().hasHeightForWidth())
        self.btn_registrar.setSizePolicy(sizePolicy3)
        self.btn_registrar.setMinimumSize(QSize(0, 30))
        self.btn_registrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registrar.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(85, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(62, 125, 93);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_registrar)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.widget_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tela de registro", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Registre seu compudador utilizando aqui suas informa\u00e7\u00f5es de compra", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#55aa7f;\">Caso n\u00e3o tenha adquirido uma licen\u00e7a, acesse </span><a href=\"https://savevideo.com.br\"><span style=\" text-decoration: underline; color:#55ff7f;\">https://savevideo.com.br</span></a></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"E-mail de compra:", None))
        self.btn_registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Suporte via WhatApp (53) 99156-5693", None))
    # retranslateUi

