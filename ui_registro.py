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
        MainWindow.resize(409, 196)
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
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.edit_nome = QLineEdit(self.centralwidget)
        self.edit_nome.setObjectName(u"edit_nome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.edit_nome.sizePolicy().hasHeightForWidth())
        self.edit_nome.setSizePolicy(sizePolicy1)
        self.edit_nome.setMinimumSize(QSize(0, 30))
        self.edit_nome.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        self.edit_nome.setFont(font)

        self.verticalLayout.addWidget(self.edit_nome)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.edit_email = QLineEdit(self.centralwidget)
        self.edit_email.setObjectName(u"edit_email")
        self.edit_email.setMinimumSize(QSize(0, 30))
        self.edit_email.setFont(font)

        self.verticalLayout.addWidget(self.edit_email)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_registrar = QPushButton(self.centralwidget)
        self.btn_registrar.setObjectName(u"btn_registrar")
        sizePolicy1.setHeightForWidth(self.btn_registrar.sizePolicy().hasHeightForWidth())
        self.btn_registrar.setSizePolicy(sizePolicy1)
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


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tela de registro", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"E-mail de compra:", None))
        self.btn_registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
    # retranslateUi

