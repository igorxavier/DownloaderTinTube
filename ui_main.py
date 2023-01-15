# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(753, 527)
        MainWindow.setStyleSheet(u"background-color: rgb(25, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.qlin1_2 = QWidget(self.widget)
        self.qlin1_2.setObjectName(u"qlin1_2")
        self.qlin1_2.setMinimumSize(QSize(0, 0))
        self.qlin1 = QHBoxLayout(self.qlin1_2)
        self.qlin1.setSpacing(20)
        self.qlin1.setObjectName(u"qlin1")
        self.btn_menu = QPushButton(self.qlin1_2)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QSize(70, 0))
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet(u":hover{\n"
"	\n"
"	\n"
"	background-color: rgb(14, 0, 190);\n"
"}\n"
"*{\n"
"	border:none;\n"
"}")
        self.btn_menu.setIconSize(QSize(32, 32))

        self.qlin1.addWidget(self.btn_menu)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_titulo = QLabel(self.qlin1_2)
        self.lbl_titulo.setObjectName(u"lbl_titulo")

        self.verticalLayout_3.addWidget(self.lbl_titulo)

        self.lbl_desc = QLabel(self.qlin1_2)
        self.lbl_desc.setObjectName(u"lbl_desc")

        self.verticalLayout_3.addWidget(self.lbl_desc)


        self.qlin1.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addWidget(self.qlin1_2)

        self.qlin2 = QHBoxLayout()
        self.qlin2.setSpacing(0)
        self.qlin2.setObjectName(u"qlin2")
        self.qlin2.setContentsMargins(-1, 0, -1, -1)
        self.qcol1 = QVBoxLayout()
        self.qcol1.setObjectName(u"qcol1")
        self.qcol1.setContentsMargins(0, -1, 0, -1)
        self.frm_lateral = QFrame(self.widget)
        self.frm_lateral.setObjectName(u"frm_lateral")
        self.frm_lateral.setMaximumSize(QSize(9, 16777215))
        self.frm_lateral.setLayoutDirection(Qt.LeftToRight)
        self.frm_lateral.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(108, 108, 108);\n"
"}\n"
"QFrame{\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.frm_lateral.setFrameShape(QFrame.StyledPanel)
        self.frm_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frm_lateral)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_colar = QPushButton(self.frm_lateral)
        self.btn_colar.setObjectName(u"btn_colar")
        self.btn_colar.setMinimumSize(QSize(0, 30))
        self.btn_colar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_colar)

        self.btn_excluir = QPushButton(self.frm_lateral)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_excluir)

        self.btn_limpar = QPushButton(self.frm_lateral)
        self.btn_limpar.setObjectName(u"btn_limpar")
        self.btn_limpar.setMinimumSize(QSize(0, 30))
        self.btn_limpar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_limpar)

        self.btn_baixar = QPushButton(self.frm_lateral)
        self.btn_baixar.setObjectName(u"btn_baixar")
        self.btn_baixar.setMinimumSize(QSize(0, 30))
        self.btn_baixar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_baixar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.qcol1.addWidget(self.frm_lateral)


        self.qlin2.addLayout(self.qcol1)

        self.qcol2_2 = QWidget(self.widget)
        self.qcol2_2.setObjectName(u"qcol2_2")
        self.qcol2_2.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.qcol2 = QVBoxLayout(self.qcol2_2)
        self.qcol2.setSpacing(0)
        self.qcol2.setObjectName(u"qcol2")
        self.list_links = QListWidget(self.qcol2_2)
        self.list_links.setObjectName(u"list_links")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.list_links.sizePolicy().hasHeightForWidth())
        self.list_links.setSizePolicy(sizePolicy1)
        self.list_links.setMaximumSize(QSize(300, 16777215))
        self.list_links.setStyleSheet(u"")
        self.list_links.setFrameShape(QFrame.NoFrame)

        self.qcol2.addWidget(self.list_links)

        self.pro_bar = QProgressBar(self.qcol2_2)
        self.pro_bar.setObjectName(u"pro_bar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pro_bar.sizePolicy().hasHeightForWidth())
        self.pro_bar.setSizePolicy(sizePolicy2)
        self.pro_bar.setMinimumSize(QSize(0, 0))
        self.pro_bar.setSizeIncrement(QSize(0, 0))
        self.pro_bar.setBaseSize(QSize(0, 0))
        self.pro_bar.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"color: rgb(64, 64, 64);")
        self.pro_bar.setValue(0)
        self.pro_bar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pro_bar.setTextVisible(True)
        self.pro_bar.setOrientation(Qt.Horizontal)
        self.pro_bar.setInvertedAppearance(False)
        self.pro_bar.setTextDirection(QProgressBar.TopToBottom)

        self.qcol2.addWidget(self.pro_bar)


        self.qlin2.addWidget(self.qcol2_2)


        self.verticalLayout_2.addLayout(self.qlin2)

        self.qlin3 = QVBoxLayout()
        self.qlin3.setSpacing(0)
        self.qlin3.setObjectName(u"qlin3")
        self.lbl_rodape = QLabel(self.widget)
        self.lbl_rodape.setObjectName(u"lbl_rodape")

        self.qlin3.addWidget(self.lbl_rodape)


        self.verticalLayout_2.addLayout(self.qlin3)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MultiDownloader", None))
        self.btn_menu.setText("")
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"Multi Downloader", None))
        self.lbl_desc.setText(QCoreApplication.translate("MainWindow", u"Baixe V\u00eddeos Do TikTok, Instagram e Youtube", None))
        self.btn_colar.setText(QCoreApplication.translate("MainWindow", u"Colar Links", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir Link", None))
        self.btn_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar Links", None))
        self.btn_baixar.setText(QCoreApplication.translate("MainWindow", u"Baixar", None))
        self.lbl_rodape.setText(QCoreApplication.translate("MainWindow", u"Suporte", None))
    # retranslateUi

