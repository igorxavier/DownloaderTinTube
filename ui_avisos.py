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
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_msg = QLabel(self.centralwidget)
        self.lbl_msg.setObjectName(u"lbl_msg")
        self.lbl_msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_msg)

        self.lbl_link = QLabel(self.centralwidget)
        self.lbl_link.setObjectName(u"lbl_link")
        font = QFont()
        font.setUnderline(True)
        self.lbl_link.setFont(font)
        self.lbl_link.setCursor(QCursor(Qt.PointingHandCursor))
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

