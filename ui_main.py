# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(749, 558)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(26, 26, 26, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(102, 102, 102, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        brush3 = QBrush(QColor(85, 170, 127, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush3)
        brush4 = QBrush(QColor(85, 255, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        brush6 = QBrush(QColor(239, 239, 239, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        brush7 = QBrush(QColor(48, 140, 198, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        brush8 = QBrush(QColor(0, 0, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush10 = QBrush(QColor(145, 145, 145, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        MainWindow.setPalette(palette)
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
"}")
        MainWindow.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.btn_menu.setIconSize(QSize(32, 32))

        self.qlin1.addWidget(self.btn_menu)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_titulo = QLabel(self.qlin1_2)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        font = QFont()
        font.setPointSize(23)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setStyleSheet(u"color: rgb(85, 170, 127);")

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
        self.frm_lateral.setMinimumSize(QSize(250, 0))
        self.frm_lateral.setMaximumSize(QSize(9, 16777215))
        self.frm_lateral.setLayoutDirection(Qt.LeftToRight)
        self.frm_lateral.setStyleSheet(u"QFrame{\n"
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

        self.btn_pasta = QPushButton(self.frm_lateral)
        self.btn_pasta.setObjectName(u"btn_pasta")
        self.btn_pasta.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.btn_pasta)

        self.edit_local = QLineEdit(self.frm_lateral)
        self.edit_local.setObjectName(u"edit_local")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.edit_local.sizePolicy().hasHeightForWidth())
        self.edit_local.setSizePolicy(sizePolicy1)
        self.edit_local.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.edit_local.setFont(font1)
        self.edit_local.setStyleSheet(u"background-color: rgb(188, 187, 188);\n"
"color: rgb(51, 52, 52);\n"
"border: none;")
        self.edit_local.setReadOnly(True)

        self.verticalLayout.addWidget(self.edit_local)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_baixar = QPushButton(self.frm_lateral)
        self.btn_baixar.setObjectName(u"btn_baixar")
        self.btn_baixar.setMinimumSize(QSize(0, 30))
        self.btn_baixar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_baixar.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(85, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(62, 124, 92);\n"
"}")

        self.verticalLayout.addWidget(self.btn_baixar)


        self.qcol1.addWidget(self.frm_lateral)


        self.qlin2.addLayout(self.qcol1)

        self.qcol2_2 = QWidget(self.widget)
        self.qcol2_2.setObjectName(u"qcol2_2")
        self.qcol2_2.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.qcol2 = QVBoxLayout(self.qcol2_2)
        self.qcol2.setSpacing(0)
        self.qcol2.setObjectName(u"qcol2")
        self.qcol2.setContentsMargins(0, -1, 0, 9)
        self.list_links = QListWidget(self.qcol2_2)
        self.list_links.setObjectName(u"list_links")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.list_links.sizePolicy().hasHeightForWidth())
        self.list_links.setSizePolicy(sizePolicy2)
        self.list_links.setMinimumSize(QSize(0, 0))
        self.list_links.setMaximumSize(QSize(16777215, 16777215))
        palette1 = QPalette()
        brush11 = QBrush(QColor(200, 200, 200, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush11)
        brush12 = QBrush(QColor(52, 52, 52, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush12)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush12)
        brush13 = QBrush(QColor(77, 90, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Link, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush12)
        brush14 = QBrush(QColor(77, 91, 0, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Link, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush12)
        brush15 = QBrush(QColor(58, 75, 0, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Link, brush15)
        self.list_links.setPalette(palette1)
        font2 = QFont()
        font2.setPointSize(12)
        self.list_links.setFont(font2)
        self.list_links.setFrameShape(QFrame.NoFrame)
        self.list_links.setGridSize(QSize(0, 22))

        self.qcol2.addWidget(self.list_links)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.lbl_pro_bar = QLabel(self.qcol2_2)
        self.lbl_pro_bar.setObjectName(u"lbl_pro_bar")
        font3 = QFont()
        font3.setBold(True)
        self.lbl_pro_bar.setFont(font3)
        self.lbl_pro_bar.setStyleSheet(u"color: rgb(85, 170, 127);")

        self.verticalLayout_4.addWidget(self.lbl_pro_bar)

        self.pro_bar = QProgressBar(self.qcol2_2)
        self.pro_bar.setObjectName(u"pro_bar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pro_bar.sizePolicy().hasHeightForWidth())
        self.pro_bar.setSizePolicy(sizePolicy3)
        self.pro_bar.setMinimumSize(QSize(0, 0))
        self.pro_bar.setMaximumSize(QSize(16777213, 16777215))
        self.pro_bar.setSizeIncrement(QSize(1, 2))
        palette2 = QPalette()
        brush16 = QBrush(QColor(64, 64, 64, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush16)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush16)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush16)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Link, brush3)
        brush17 = QBrush(QColor(64, 64, 64, 128))
        brush17.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush16)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush16)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush16)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Link, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush16)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Link, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pro_bar.setPalette(palette2)
        self.pro_bar.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"color: rgb(64, 64, 64);")
        self.pro_bar.setValue(0)
        self.pro_bar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pro_bar.setTextVisible(True)
        self.pro_bar.setOrientation(Qt.Horizontal)
        self.pro_bar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_4.addWidget(self.pro_bar)


        self.qcol2.addLayout(self.verticalLayout_4)


        self.qlin2.addWidget(self.qcol2_2)


        self.verticalLayout_2.addLayout(self.qlin2)

        self.qlin3 = QVBoxLayout()
        self.qlin3.setSpacing(0)
        self.qlin3.setObjectName(u"qlin3")
        self.qlin3.setContentsMargins(-1, 5, -1, 5)
        self.lbl_rodape1 = QLabel(self.widget)
        self.lbl_rodape1.setObjectName(u"lbl_rodape1")
        self.lbl_rodape1.setAlignment(Qt.AlignCenter)

        self.qlin3.addWidget(self.lbl_rodape1)

        self.lbl_rodape2 = QLabel(self.widget)
        self.lbl_rodape2.setObjectName(u"lbl_rodape2")
        self.lbl_rodape2.setAlignment(Qt.AlignCenter)

        self.qlin3.addWidget(self.lbl_rodape2)


        self.verticalLayout_2.addLayout(self.qlin3)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SaveVideo", None))
        self.btn_menu.setText("")
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"SaveVideo", None))
        self.lbl_desc.setText(QCoreApplication.translate("MainWindow", u"Baixe V\u00eddeos Em Lote Do TikTok, Instagram e Youtube", None))
        self.btn_colar.setText(QCoreApplication.translate("MainWindow", u"Colar Links", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir Link", None))
        self.btn_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar Links", None))
        self.btn_pasta.setText(QCoreApplication.translate("MainWindow", u"Onde Salvar", None))
        self.btn_baixar.setText(QCoreApplication.translate("MainWindow", u"Baixar", None))
        self.lbl_pro_bar.setText(QCoreApplication.translate("MainWindow", u"Aguardando...", None))
        self.lbl_rodape1.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por Igor Lem\u00f5es - Contato em todas as redes sociais - Suporte via WhatApp (53) 99156-5693", None))
        self.lbl_rodape2.setText(QCoreApplication.translate("MainWindow", u"Licen\u00e7a para uso pessoal e intransfer\u00edvel | https://robozinhos.com.br | https://igorlemoes.com.br", None))
    # retranslateUi

