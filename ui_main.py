# -*- coding: utf-8 -*-
################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QRegExp)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QRegExpValidator)
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-3d.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        #self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")




        #######################
        #######################

        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.verticalLayout_M18 = QVBoxLayout(self.page_main)
        self.verticalLayout_M18.setObjectName(u"verticalLayout_M18")

        #######################

        self.frame_help = QFrame(self.page_main)
        self.frame_help.setObjectName(u"frame_2")
        #self.frame_help.setMinimumSize(QSize(0, 150))
        self.frame_help.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;")
        self.frame_help.setFrameShape(QFrame.StyledPanel)
        self.frame_help.setFrameShadow(QFrame.Raised)

        #######

        self.verticalLayout_M0 = QVBoxLayout(self.frame_help)
        self.verticalLayout_M0.setSpacing(0)
        self.verticalLayout_M0.setObjectName(u"verticalLayout_M0")
        self.verticalLayout_M0.setContentsMargins(0, 0, 0, 0)

        self.label_help_info = QLabel(self.frame_help)
        self.label_help_info.setMaximumSize(QSize(16777215, 133))
        self.label_help_info.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_help_info.setTextFormat(Qt.RichText)
        self.label_help_info.setOpenExternalLinks(True)
        self.label_help_info.setWordWrap(True)
        self.label_help_info.setMargin(10)
        self.label_help_info.setAlignment(Qt.AlignTop)
        self.label_help_info.setObjectName(u"label_top_info_1")
        #self.label_help_info.setMinimumSize(QSize(50, 0))
        #self.label_help_info.setMaximumSize(QSize(16777215, 140))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_help_info.setFont(font2)
        #self.label_help_info.setStyleSheet(u"color: rgb(255, 255, 255); ")

        self.verticalLayout_M0.addWidget(self.label_help_info)

        #######


        #self.verticalLayout_M18.addWidget(self.frame_help)


        #######################

        self.gridLayout_M1 = QGridLayout()
        self.gridLayout_M1.setObjectName(u"gridLayout_M1")
        self.gridLayout_M1.setContentsMargins(-1, -1, -1, 0)


        #############

        self.frame_actions = QFrame(self.page_main)
        self.frame_actions.setObjectName(u"frame_actions")
        self.frame_actions.setMinimumSize(QSize(0, 150))
        self.frame_actions.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;")
        self.frame_actions.setFrameShape(QFrame.StyledPanel)
        self.frame_actions.setFrameShadow(QFrame.Raised)

        #######

        self.verticalLayout_M1a = QVBoxLayout(self.frame_actions)
        self.verticalLayout_M1a.setSpacing(0)
        self.verticalLayout_M1a.setObjectName(u"verticalLayout_M1a")
        self.verticalLayout_M1a.setContentsMargins(0, 0, 0, 0)

        #######


        self.gridLayout_M1a = QGridLayout()
        self.gridLayout_M1a.setObjectName(u"gridLayout_M1a")
        self.gridLayout_M1a.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_M1a.setMargin(10)


        self.labelBoxCamera = QLabel(self.frame_actions)
        self.labelBoxCamera.setObjectName(u"labelBoxCamera")
        self.labelBoxCamera.setFont(font1)
        self.labelBoxCamera.setStyleSheet(u"")


        self.gridLayout_M1a.addWidget(self.labelBoxCamera, 0, 0, 1, 6)

        ##

        self.pushButton_backward = QToolButton(self.frame_actions)
        self.pushButton_backward.setObjectName(u"pushButton_backward")
        self.pushButton_backward.setMinimumSize(QSize(100, 153))
        self.pushButton_backward.setMaximumSize(QSize(300, 153))
        self.pushButton_backward.setToolTip(u"move along camera path (backward)")
        fontM1d = QFont()
        fontM1d.setFamily(u"Segoe UI")
        fontM1d.setPointSize(11)
        self.pushButton_backward.setFont(fontM1d)
        self.pushButton_backward.setStyleSheet(u"QToolButton {\n"
"	padding-top: 35px;\n"
"	padding-bottom: 15px;\n"
"	margin-right: 5px;\n"
"	margin-bottom: 10px;\n"
"	margin-top: 20px;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QToolButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.pushButton_backward.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        iconM1d = QIcon()
        iconM1d.addFile(u":/20x20/icons/20x20/cil-media-skip-backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_backward.setIcon(iconM1d)

        self.gridLayout_M1a.addWidget(self.pushButton_backward, 1, 0, 1, 3)

        ##

        self.pushButton_forward = QToolButton(self.frame_actions)
        self.pushButton_forward.setObjectName(u"pushButton_forward")
        self.pushButton_forward.setToolTip(u"move along camera path (forward)")
        self.pushButton_forward.setMinimumSize(QSize(100, 153))
        self.pushButton_forward.setMaximumSize(QSize(300, 153))
        fontM1e = QFont()
        fontM1e.setFamily(u"Segoe UI")
        fontM1e.setPointSize(11)
        self.pushButton_forward.setFont(fontM1e)
        self.pushButton_forward.setStyleSheet(u"QToolButton {\n"
"	padding-top: 35px;\n"
"	padding-bottom: 15px;\n"
"	margin-left: 5px;\n"
"	margin-bottom: 10px;\n"
"	margin-top: 20px;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QToolButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_forward.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        iconM1e = QIcon()
        iconM1e.addFile(u":/20x20/icons/20x20/cil-media-skip-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_forward.setIcon(iconM1e)

        self.gridLayout_M1a.addWidget(self.pushButton_forward, 1, 3, 1, 3)

        ##

        self.pushButton_prev = QPushButton(self.frame_actions)
        self.pushButton_prev.setObjectName(u"pushButton_prev")
        self.pushButton_prev.setToolTip(u"skip to previous waypoint")
        self.pushButton_prev.setMinimumSize(QSize(80, 60))
        self.pushButton_prev.setMaximumSize(QSize(200, 60))
        fontM1a = QFont()
        fontM1a.setFamily(u"Segoe UI")
        fontM1a.setPointSize(11)
        self.pushButton_prev.setFont(fontM1a)
        self.pushButton_prev.setStyleSheet(u"QPushButton {\n"
"	margin-right: 5px;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        iconM1a = QIcon()
        iconM1a.addFile(u":/20x20/icons/20x20/cil-media-step-backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_prev.setIcon(iconM1a)

        self.gridLayout_M1a.addWidget(self.pushButton_prev, 2, 0, 1, 2)

        ##

        self.pushButton_home = QPushButton(self.frame_actions)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setToolTip(u"go to origin")
        self.pushButton_home.setMinimumSize(QSize(80, 60))
        self.pushButton_home.setMaximumSize(QSize(200, 60))
        fontM1b = QFont()
        fontM1b.setFamily(u"Segoe UI")
        fontM1b.setPointSize(11)
        self.pushButton_home.setFont(fontM1b)
        self.pushButton_home.setStyleSheet(u"QPushButton {\n"
"	margin-left: 5px;\n"
"	margin-right: 5px;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        iconM1b = QIcon()
        iconM1b.addFile(u":/20x20/icons/20x20/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_home.setIcon(iconM1b)

        self.gridLayout_M1a.addWidget(self.pushButton_home, 2, 2, 1, 2)

        ##

        self.pushButton_next = QPushButton(self.frame_actions)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setToolTip(u"skip to next waypoint")
        self.pushButton_next.setMinimumSize(QSize(80, 60))
        self.pushButton_next.setMaximumSize(QSize(200, 60))
        fontM1c = QFont()
        fontM1c.setFamily(u"Segoe UI")
        fontM1c.setPointSize(11)
        self.pushButton_next.setFont(fontM1c)
        self.pushButton_next.setStyleSheet(u"QPushButton {\n"
"	margin-left: 5px;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        iconM1c = QIcon()
        iconM1c.addFile(u":/20x20/icons/20x20/cil-media-step-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_next.setIcon(iconM1c)

        self.gridLayout_M1a.addWidget(self.pushButton_next, 2, 4, 1, 2)

        ##

        self.verticalLayout_M1a.addLayout(self.gridLayout_M1a)
        self.gridLayout_M1.addWidget(self.frame_actions)

        #######

        #############

        #############

        self.frame_speed = QFrame(self.page_main)
        self.frame_speed.setObjectName(u"frame_speed")
        self.frame_speed.setMinimumSize(QSize(210, 50))
        self.frame_speed.setMaximumSize(QSize(210, 16777215))
        self.frame_speed.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;")
        self.frame_speed.setFrameShape(QFrame.StyledPanel)
        self.frame_speed.setFrameShadow(QFrame.Raised)

        #######

        self.verticalLayout_M2a = QVBoxLayout(self.frame_speed)
        self.verticalLayout_M2a.setAlignment(Qt.AlignTop)
        self.verticalLayout_M2a.setSpacing(5)
        self.verticalLayout_M2a.setObjectName(u"verticalLayout_M2a")
        self.verticalLayout_M2a.setContentsMargins(10, 10, 10, 10)

        #######




        self.labelBoxSpeed = QLabel(self.frame_speed)
        self.labelBoxSpeed.setObjectName(u"labelBoxSpeed")
        self.labelBoxSpeed.setAlignment(Qt.AlignTop)
        self.labelBoxSpeed.setFont(font1)
        self.labelBoxSpeed.setStyleSheet(u"")


        self.verticalLayout_M2a.addWidget(self.labelBoxSpeed)

        ##

        self.label_pathtime_info = QLabel(self.frame_speed)
        self.label_pathtime_info.setObjectName(u"label_pathtime_info")
        self.label_pathtime_info.setMaximumSize(QSize(210, 16777215))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_pathtime_info.setFont(font2)
        self.label_pathtime_info.setAlignment(Qt.AlignBottom)
        self.label_pathtime_info.setStyleSheet(u"color: rgb(98, 103, 111); margin-top: 17px; margin-bottom: 3px;")

        self.verticalLayout_M2a.addWidget(self.label_pathtime_info)

        ##

        self.pathtimeEdit = QDoubleSpinBox(self.frame_speed)
        self.pathtimeEdit.setObjectName(u"pathtimeEdit")
        self.pathtimeEdit.setSuffix(u" seconds")
        self.pathtimeEdit.setMinimum(.01)
        self.pathtimeEdit.setValue(3.00)
        self.pathtimeEdit.setMaximum(3600)
        self.pathtimeEdit.setMinimumSize(QSize(0, 30))
        self.pathtimeEdit.setStyleSheet(u"QDoubleSpinBox{\n"
                                       "	background-color: rgb(27, 29, 35);\n"
                                       "	border-radius: 5px;\n"
                                       "	border: 2px solid rgb(27, 29, 35);\n"
                                       "	padding: 5px;\n"
                                       "	padding-left: 10px;\n"
                                       "}\n"
                                       "QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {"
                                        "width: 26px;"
                                        "background-color: transparent;"
                                       "}"
                                       "QDoubleSpinBox::up-arrow {"
                                       "    image: url(icons/16x16/cil-arrow-top.png);"
                                       "    width: 16px;"
                                       "    height: 16px;"
                                       "}"
                                       "QDoubleSpinBox::down-arrow {"
                                       "    image: url(icons/16x16/cil-arrow-bottom.png);"
                                       "    width: 16px;"
                                       "    height: 16px;"
                                       "}"
                                       "QDoubleSpinBox:hover{\n"
                                       "	border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n")

        self.verticalLayout_M2a.addWidget(self.pathtimeEdit)


        ##

        self.label_ease_info = QLabel(self.frame_speed)
        self.label_ease_info.setObjectName(u"label_ease_info")
        self.label_ease_info.setMaximumSize(QSize(210, 16777215))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_ease_info.setFont(font2)
        self.label_ease_info.setAlignment(Qt.AlignBottom)
        self.label_ease_info.setStyleSheet(u"color: rgb(98, 103, 111); margin-top: 13px; margin-bottom: 3px;")
        self.verticalLayout_M2a.addWidget(self.label_ease_info)

        ##

        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)

        self.easeSelection = QComboBox(self.frame_speed)
        self.easeSelection.setObjectName(u"comboBox")
        self.easeSelection.setFont(font8)
        self.easeSelection.setAutoFillBackground(False)
        self.easeSelection.setMinimumSize(QSize(100, 30))
        self.easeSelection.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.easeSelection.setIconSize(QSize(16, 16))
        self.easeSelection.setFrame(True)


        self.easeSelection.addItem("")
        self.easeSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"ease in/out", None))
        self.easeSelection.addItem("")
        self.easeSelection.setItemText(1, QCoreApplication.translate("MainWindow", u"ease in", None))
        self.easeSelection.addItem("")
        self.easeSelection.setItemText(2, QCoreApplication.translate("MainWindow", u"ease out", None))
        self.easeSelection.addItem("")
        self.easeSelection.setItemText(3, QCoreApplication.translate("MainWindow", u"DISABLED", None))

        self.verticalLayout_M2a.addWidget(self.easeSelection)

        ##

        self.label_pointtime_info = QLabel(self.frame_speed)
        self.label_pointtime_info.setObjectName(u"label_pointtime_info")
        self.label_pointtime_info.setMaximumSize(QSize(210, 16777215))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_pointtime_info.setFont(font2)
        self.label_pointtime_info.setAlignment(Qt.AlignBottom)
        self.label_pointtime_info.setStyleSheet(u"color: rgb(98, 103, 111); margin-top: 13px; margin-bottom: 3px;")

        self.verticalLayout_M2a.addWidget(self.label_pointtime_info)

        ##

        self.pointtimeEdit = QDoubleSpinBox(self.frame_speed)
        self.pointtimeEdit.setSuffix(u" seconds")
        self.pointtimeEdit.setMinimum(0.01)
        self.pointtimeEdit.setMaximum(60)
        self.pointtimeEdit.setObjectName(u"pointtimeEdit")
        self.pointtimeEdit.setMinimumSize(QSize(0, 30))
        self.pointtimeEdit.setValue(1.00)
        self.pointtimeEdit.setStyleSheet(u"QDoubleSpinBox{\n"
                                        "	background-color: rgb(27, 29, 35);\n"
                                        "	border-radius: 5px;\n"
                                        "	border: 2px solid rgb(27, 29, 35);\n"
                                        "	padding: 5px;\n"
                                        "	padding-left: 10px;\n"
                                        "}\n"
                                        "QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {"
                                        "width: 26px;"
                                        "background-color: transparent;"
                                        "}"
                                        "QDoubleSpinBox::up-arrow {"
                                        "    image: url(icons/16x16/cil-arrow-top.png);"
                                        "    width: 16px;"
                                        "    height: 16px;"
                                        "}"
                                        "QDoubleSpinBox::down-arrow {"
                                        "    image: url(icons/16x16/cil-arrow-bottom.png);"
                                        "    width: 16px;"
                                        "    height: 16px;"
                                        "}"
                                        "QDoubleSpinBox:hover{\n"
                                        "	border: 2px solid rgb(64, 71, 88);\n"
                                        "}\n")

        self.verticalLayout_M2a.addWidget(self.pointtimeEdit)

        ##

        #self.verticalLayout_M2a.addLayout(self.gridLayout_M2a)

        #######


        self.gridLayout_M1.addWidget(self.frame_speed, 0, 1, 1, 1)

        #############

        self.verticalLayout_M18.addLayout(self.gridLayout_M1)

        self.verticalLayout_M18.addWidget(self.frame_help)

        #######################

        self.frame_div_table_widget_M1 = QFrame(self.page_main)
        self.frame_div_table_widget_M1.setObjectName(u"frame_div_table_widget_M1")
        self.frame_div_table_widget_M1.setMinimumSize(QSize(0, 58))
        self.frame_div_table_widget_M1.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_table_widget_M1.setFrameShape(QFrame.StyledPanel)
        self.frame_div_table_widget_M1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_M20 = QVBoxLayout(self.frame_div_table_widget_M1)
        self.verticalLayout_M20.setObjectName(u"verticalLayout_M20")
        self.verticalLayout_M20.setAlignment(Qt.AlignTop)
        self.gridLayout_M6 = QGridLayout()
        self.gridLayout_M6.setObjectName(u"gridLayout_M6")
        self.pushButton_delete_all = QPushButton(self.frame_div_table_widget_M1)
        self.pushButton_delete_all.setObjectName(u"pushButton_delete_all")
        self.pushButton_delete_all.setMinimumSize(QSize(200, 40))
        self.pushButton_delete_all.setMaximumSize(QSize(200, 40))
        fontM7 = QFont()
        fontM7.setFamily(u"Segoe UI")
        fontM7.setPointSize(11)
        self.pushButton_delete_all.setFont(fontM7)
        self.pushButton_delete_all.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	padding-right: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        iconM4 = QIcon()
        iconM4.addFile(u":/20x20/icons/20x20/cil-trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_delete_all.setIcon(iconM4)

        self.gridLayout_M6.addWidget(self.pushButton_delete_all, 0, 1, 1, 1)




        self.pushButton_add_waypoint = QPushButton(self.frame_div_table_widget_M1)
        self.pushButton_add_waypoint.setObjectName(u"pushButton_add_waypoint")
        self.pushButton_add_waypoint.setMinimumSize(QSize(150, 40))
        fontM8 = QFont()
        fontM8.setFamily(u"Segoe UI")
        fontM8.setPointSize(11)
        self.pushButton_add_waypoint.setFont(fontM7)
        self.pushButton_add_waypoint.setStyleSheet(u"QPushButton {\n"
"	margin-right: 10px;\n"
"	border: 2px solid rgb(70, 124, 0);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(70, 124, 0);\n"
"	padding-right: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(77, 137, 0);\n"
"	border: 2px solid rgb(84, 147, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(48, 84, 0);\n"
"	border: 2px solid rgb(63, 104, 0);\n"
"}")
        iconM5 = QIcon()
        iconM5.addFile(u":/20x20/icons/20x20/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add_waypoint.setIcon(iconM5)

        self.gridLayout_M6.addWidget(self.pushButton_add_waypoint, 0, 0, 1, 1)



        self.tableWidget_waypoints = QTableWidget(self.frame_div_table_widget_M1)
        if (self.tableWidget_waypoints.columnCount() < 3):
            self.tableWidget_waypoints.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_waypoints.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_waypoints.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setText(u"DEL")
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter)
        self.tableWidget_waypoints.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_waypoints.setObjectName(u"tableWidget_waypoints")
        sizePolicy.setHeightForWidth(self.tableWidget_waypoints.sizePolicy().hasHeightForWidth())
        self.tableWidget_waypoints.setSizePolicy(sizePolicy)
        self.tableWidget_waypoints.setMinimumSize(QSize(0, 50))
        self.tableWidget_waypoints.setMaximumSize(QSize(16777215, 116))
        brushM1 = QBrush(QColor(0, 0, 0, 0))
        brushM1.setStyle(Qt.SolidPattern)
        brushM6 = QBrush(QColor(210, 210, 210, 255))
        brushM6.setStyle(Qt.SolidPattern)
        paletteM1 = QPalette()
        paletteM1.setBrush(QPalette.Active, QPalette.WindowText, brushM6)
        paletteM1.setBrush(QPalette.Active, QPalette.Button, brushM1)
        paletteM1.setBrush(QPalette.Active, QPalette.Text, brushM6)
        paletteM1.setBrush(QPalette.Active, QPalette.ButtonText, brushM6)
        brushM15 = QBrush(QColor(0, 0, 0, 255))
        brushM15.setStyle(Qt.NoBrush)
        paletteM1.setBrush(QPalette.Active, QPalette.Base, brushM15)
        paletteM1.setBrush(QPalette.Active, QPalette.Window, brushM1)
        brushM16 = QBrush(QColor(210, 210, 210, 128))
        brushM16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        paletteM1.setBrush(QPalette.Active, QPalette.PlaceholderText, brushM16)
#endif
        paletteM1.setBrush(QPalette.Inactive, QPalette.WindowText, brushM6)
        paletteM1.setBrush(QPalette.Inactive, QPalette.Button, brushM1)
        paletteM1.setBrush(QPalette.Inactive, QPalette.Text, brushM6)
        paletteM1.setBrush(QPalette.Inactive, QPalette.ButtonText, brushM6)
        brushM17 = QBrush(QColor(0, 0, 0, 255))
        brushM17.setStyle(Qt.NoBrush)
        paletteM1.setBrush(QPalette.Inactive, QPalette.Base, brushM17)
        paletteM1.setBrush(QPalette.Inactive, QPalette.Window, brushM1)
        brushM18 = QBrush(QColor(210, 210, 210, 128))
        brushM18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        paletteM1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brushM18)
#endif
        paletteM1.setBrush(QPalette.Disabled, QPalette.WindowText, brushM6)
        paletteM1.setBrush(QPalette.Disabled, QPalette.Button, brushM1)
        paletteM1.setBrush(QPalette.Disabled, QPalette.Text, brushM6)
        paletteM1.setBrush(QPalette.Disabled, QPalette.ButtonText, brushM6)
        brushM19 = QBrush(QColor(0, 0, 0, 255))
        brushM19.setStyle(Qt.NoBrush)
        paletteM1.setBrush(QPalette.Disabled, QPalette.Base, brushM19)
        paletteM1.setBrush(QPalette.Disabled, QPalette.Window, brushM1)
        brush20 = QBrush(QColor(210, 210, 210, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        paletteM1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.tableWidget_waypoints.setPalette(paletteM1)
        self.tableWidget_waypoints.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(52, 59, 72);	\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
""
                        "}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_waypoints.setFrameShape(QFrame.NoFrame)
        self.tableWidget_waypoints.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_waypoints.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_waypoints.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_waypoints.setAutoScroll(False)
        self.tableWidget_waypoints.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_waypoints.setTabKeyNavigation(False)
        self.tableWidget_waypoints.setProperty("showDropIndicator", False)
        self.tableWidget_waypoints.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_waypoints.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_waypoints.setShowGrid(True)
        self.tableWidget_waypoints.setGridStyle(Qt.SolidLine)
        self.tableWidget_waypoints.setSortingEnabled(False)
        self.tableWidget_waypoints.horizontalHeader().setVisible(False)
        self.tableWidget_waypoints.verticalHeader().setVisible(False)

        self.gridLayout_M6.addWidget(self.tableWidget_waypoints, 1, 0, 1, 2)



        self.verticalLayout_M20.addLayout(self.gridLayout_M6)


        self.verticalLayout_M18.addWidget(self.frame_div_table_widget_M1)

        self.stackedWidget.addWidget(self.page_main)



        #######################
        #######################

        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.verticalLayout_I18 = QVBoxLayout(self.page_info)
        self.verticalLayout_I18.setObjectName(u"verticalLayout_I18")

        #######################

        self.frame_resources = QFrame(self.page_info)
        self.frame_resources.setObjectName(u"frame_2")
        #self.frame_resources.setMinimumSize(QSize(0, 150))
        self.frame_resources.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;")
        self.frame_resources.setFrameShape(QFrame.StyledPanel)
        self.frame_resources.setFrameShadow(QFrame.Raised)

        #######

        self.verticalLayout_I0 = QVBoxLayout(self.frame_resources)
        self.verticalLayout_I0.setSpacing(0)
        self.verticalLayout_I0.setObjectName(u"verticalLayout_I0")
        self.verticalLayout_I0.setContentsMargins(0, 0, 0, 0)

        self.labelBoxResources = QLabel(self.frame_actions)
        self.labelBoxResources.setObjectName(u"labelBoxResources")
        self.labelBoxResources.setMargin(10)
        self.labelBoxResources.setMaximumSize(QSize(16777215, 35))
        self.labelBoxResources.setFont(font1)
        self.labelBoxResources.setStyleSheet(u"")

        self.verticalLayout_I0.addWidget(self.labelBoxResources)

        self.label_resources_info = QLabel(self.frame_resources)
        self.label_resources_info.setMaximumSize(QSize(16777215, 16777215))
        self.label_resources_info.setTextFormat(Qt.RichText)
        self.label_resources_info.setOpenExternalLinks(True)
        self.label_resources_info.setWordWrap(True)
        self.label_resources_info.setMargin(10)
        self.label_resources_info.setAlignment(Qt.AlignTop)
        self.label_resources_info.setObjectName(u"label_top_info_1")
        #self.label_resources_info.setMinimumSize(QSize(50, 0))
        #self.label_resources_info.setMaximumSize(QSize(16777215, 140))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_resources_info.setFont(font2)
        #self.label_resources_info.setStyleSheet(u"color: rgb(255, 255, 255); ")

        self.verticalLayout_I0.addWidget(self.label_resources_info)

        self.verticalLayout_I18.addWidget(self.frame_resources)

        #######

        self.stackedWidget.addWidget(self.page_info)

        #######################

        self.frame_license = QFrame(self.page_info)
        self.frame_license.setObjectName(u"frame_2")
        #self.frame_license.setMinimumSize(QSize(0, 150))
        self.frame_license.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;")
        self.frame_license.setFrameShape(QFrame.StyledPanel)
        self.frame_license.setFrameShadow(QFrame.Raised)

        #######

        self.verticalLayout_I1 = QVBoxLayout(self.frame_license)
        self.verticalLayout_I1.setSpacing(0)
        self.verticalLayout_I1.setObjectName(u"verticalLayout_I1")
        self.verticalLayout_I1.setContentsMargins(0, 0, 0, 0)

        self.labelBoxLicense = QLabel(self.frame_actions)
        self.labelBoxLicense.setObjectName(u"labelBoxLicense")
        self.labelBoxLicense.setMargin(10)
        self.labelBoxLicense.setMaximumSize(QSize(16777215, 35))
        self.labelBoxLicense.setFont(font1)
        self.labelBoxLicense.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.verticalLayout_I1.addWidget(self.labelBoxLicense)

        self.label_license_info = QLabel(self.frame_license)
        self.label_license_info.setMaximumSize(QSize(16777215, 16777215))
        self.label_license_info.setTextFormat(Qt.RichText)
        self.label_license_info.setOpenExternalLinks(True)
        self.label_license_info.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_license_info.setWordWrap(True)
        self.label_license_info.setMargin(10)
        self.label_license_info.setAlignment(Qt.AlignTop)
        self.label_license_info.setObjectName(u"label_top_info_1")
        #self.label_license_info.setMinimumSize(QSize(50, 0))
        #self.label_license_info.setMaximumSize(QSize(16777215, 140))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_license_info.setFont(font2)
        #self.label_license_info.setStyleSheet(u"color: rgb(255, 255, 255); ")

        self.verticalLayout_I1.addWidget(self.label_license_info)

        self.verticalLayout_I18.addWidget(self.frame_license)

        #######

        self.stackedWidget.addWidget(self.page_info)

        #######################

        #######################
        #######################

        self.page_controllers = QWidget()
        self.page_controllers.setObjectName(u"page_controllers")
        self.verticalLayout_C6 = QVBoxLayout(self.page_controllers)
        self.verticalLayout_C6.setObjectName(u"verticalLayout_C6")
        self.frame_C1 = QFrame(self.page_controllers)
        self.frame_C1.setObjectName(u"frame_C1")
        self.frame_C1.setStyleSheet(u"border-radius: 5px;")
        self.frame_C1.setFrameShape(QFrame.StyledPanel)
        self.frame_C1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_C15 = QVBoxLayout(self.frame_C1)
        self.verticalLayout_C15.setSpacing(0)
        self.verticalLayout_C15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_C15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_C1 = QFrame(self.frame_C1)
        self.frame_div_content_C1.setObjectName(u"frame_div_content_C1")
        self.frame_div_content_C1.setMinimumSize(QSize(0, 330))
        self.frame_div_content_C1.setMaximumSize(QSize(16777215, 350))
        self.frame_div_content_C1.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_C1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_C1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_C7 = QVBoxLayout(self.frame_div_content_C1)
        self.verticalLayout_C7.setSpacing(0)
        self.verticalLayout_C7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_C7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_C1 = QFrame(self.frame_div_content_C1)
        self.frame_title_wid_C1.setObjectName(u"frame_title_wid_C1")
        self.frame_title_wid_C1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_C1.setStyleSheet(u"background-color: rgb(41, 46, 57);")
        self.frame_title_wid_C1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_C1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_C8 = QVBoxLayout(self.frame_title_wid_C1)
        self.verticalLayout_C8.setObjectName(u"verticalLayout_C8")
        self.labelBoxControllers = QLabel(self.frame_title_wid_C1)
        self.labelBoxControllers.setObjectName(u"labelBoxControllers")
        self.labelBoxControllers.setFont(font1)
        self.labelBoxControllers.setStyleSheet(u"")

        self.verticalLayout_C8.addWidget(self.labelBoxControllers)


        self.verticalLayout_C7.addWidget(self.frame_title_wid_C1)

        ##

        self.frame_content_wid_1a = QFrame(self.frame_div_content_C1)
        self.frame_content_wid_1a.setObjectName(u"frame_content_wid_1a")
        self.frame_content_wid_1a.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1a.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9a = QHBoxLayout(self.frame_content_wid_1a)
        self.horizontalLayout_9a.setObjectName(u"horizontalLayout_9")


        self.keyboardAndMouseButton = QPushButton(self.frame_content_wid_1a)
        self.keyboardAndMouseButton.setObjectName(u"keyboardAndMouseButton")
        self.keyboardAndMouseButton.setMinimumSize(QSize(140, 140))
        self.keyboardAndMouseButton.setMaximumSize(QSize(140, 140))
        font8a = QFont()
        font8a.setFamily(u"Segoe UI")
        font8a.setPointSize(9)
        self.keyboardAndMouseButton.setFont(font8a)
        self.keyboardAndMouseButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(85, 170, 255);\n"
"	background-image: url(images/controllers-04.png);\n"
"}")

        self.horizontalLayout_9a.addWidget(self.keyboardAndMouseButton)


        self.spaceMouseButton = QPushButton(self.frame_content_wid_1a)
        self.spaceMouseButton.setObjectName(u"spaceMouseButton")
        self.spaceMouseButton.setMinimumSize(QSize(140, 140))
        self.spaceMouseButton.setMaximumSize(QSize(140, 140))
        font8a = QFont()
        font8a.setFamily(u"Segoe UI")
        font8a.setPointSize(9)
        self.spaceMouseButton.setFont(font8a)
        self.spaceMouseButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	background-image: url(images/controllers-01.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_9a.addWidget(self.spaceMouseButton)

        self.xBoxButton = QPushButton(self.frame_content_wid_1a)
        self.xBoxButton.setObjectName(u"xBoxButton")
        self.xBoxButton.setMinimumSize(QSize(140, 140))
        self.xBoxButton.setMaximumSize(QSize(140, 140))
        font8a = QFont()
        font8a.setFamily(u"Segoe UI")
        font8a.setPointSize(9)
        self.xBoxButton.setFont(font8a)
        self.xBoxButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	background-image: url(images/controllers-02.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_9a.addWidget(self.xBoxButton)

        self.label_controller_info = QLabel(self.frame_top_info)
        self.label_controller_info.setWordWrap(True)
        self.label_controller_info.setMargin(10)
        self.label_controller_info.setAlignment(Qt.AlignTop)
        self.label_controller_info.setObjectName(u"label_top_info_1")
        self.label_controller_info.setMaximumSize(QSize(16777215, 140))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_controller_info.setFont(font2)
        self.label_controller_info.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_9a.addWidget(self.label_controller_info)

        self.verticalLayout_C7.addWidget(self.frame_content_wid_1a)

##

        self.frame_content_wid_C1 = QFrame(self.frame_div_content_C1)
        self.frame_content_wid_C1.setObjectName(u"frame_content_wid_C1")
        self.frame_content_wid_C1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_C1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_C9 = QHBoxLayout(self.frame_content_wid_C1)
        self.horizontalLayout_C9.setObjectName(u"horizontalLayout_C9")

        self.gridLayout_C1 = QGridLayout()
        self.gridLayout_C1.setObjectName(u"gridLayout_C1")
        self.gridLayout_C1.setContentsMargins(-1, -1, -1, 0)

        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)


        self.controllerUpdateButton = QPushButton(self.frame_content_wid_C1)
        self.controllerUpdateButton.setObjectName(u"controllerUpdateButton")
        self.controllerUpdateButton.setToolTip(u"update controller list")
        self.controllerUpdateButton.setMinimumSize(QSize(30, 30))
        self.controllerUpdateButton.setMaximumSize(QSize(30, 30))

        self.controllerUpdateButton.setFont(font8)
        self.controllerUpdateButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-loop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.controllerUpdateButton.setIcon(icon3)

        self.gridLayout_C1.addWidget(self.controllerUpdateButton, 0, 0, 1, 1)

        self.controllerSelection = QComboBox(self.frame_content_wid_C1)
        self.controllerSelection.setObjectName(u"comboBox")
        self.controllerSelection.setFont(font8)
        self.controllerSelection.setAutoFillBackground(False)
        self.controllerSelection.setMinimumSize(QSize(397, 30))
        self.controllerSelection.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.controllerSelection.setIconSize(QSize(16, 16))
        self.controllerSelection.setFrame(True)

        self.gridLayout_C1.addWidget(self.controllerSelection, 0, 1, 1, 1)

        self.controllerTestButton = QPushButton(self.frame_content_wid_C1)
        self.controllerTestButton.setObjectName(u"controllerTestButton")
        self.controllerTestButton.setMinimumSize(QSize(50, 30))

        self.controllerTestButton.setFont(font8)
        self.controllerTestButton.setStyleSheet(u"QPushButton {\n"
"	margin-left: 5px;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.controllerTestButton.setIcon(icon3)

        self.gridLayout_C1.addWidget(self.controllerTestButton, 0, 2, 1, 1)



        self.horizontalLayout_C9.addLayout(self.gridLayout_C1)
        self.verticalLayout_C7.addWidget(self.frame_content_wid_C1)



##

        self.frame_3 = QFrame(self.frame_div_content_C1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12 = QVBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitemH1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitemH1)
        __qtablewidgetitemH2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitemH2)
        __qtablewidgetitemH3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitemH3)
        __qtablewidgetitemH4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitemH4)
        __qtablewidgetitemH5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitemH5)
        __qtablewidgetitemH6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitemH6)

        self.tableWidget.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem25)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        #self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)

        self.verticalLayout_C7.addWidget(self.frame_3)

##

        self.verticalLayout_C15.addWidget(self.frame_div_content_C1)

        self.verticalLayout_C6.addWidget(self.frame_C1)




        ####
        #BOX START
        ####


        self.frame_C31 = QFrame(self.page_controllers)
        self.frame_C31.setObjectName(u"frame_C31")
        self.frame_C31.setStyleSheet(u"border-radius: 5px;")
        self.frame_C31.setFrameShape(QFrame.StyledPanel)
        self.frame_C31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_C315 = QVBoxLayout(self.frame_C31)
        self.verticalLayout_C315.setSpacing(0)
        self.verticalLayout_C315.setObjectName(u"verticalLayout_C315")
        self.verticalLayout_C315.setContentsMargins(0, 0, 0, 0)


        ####
        ####


        self.frame_div_content_C31 = QFrame(self.frame_C31)
        self.frame_div_content_C31.setObjectName(u"frame_div_content_C31")
        self.frame_div_content_C31.setMinimumSize(QSize(0, 130))
        self.frame_div_content_C31.setMaximumSize(QSize(16777215, 450))
        self.frame_div_content_C31.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_C31.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_C31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_C37 = QVBoxLayout(self.frame_div_content_C31)
        self.verticalLayout_C37.setSpacing(0)
        self.verticalLayout_C37.setObjectName(u"verticalLayout_7")
        self.verticalLayout_C37.setContentsMargins(0, 0, 0, 0)

        self.frame_title_wid_C31 = QFrame(self.frame_div_content_C31)
        self.frame_title_wid_C31.setObjectName(u"frame_title_wid_C31")
        self.frame_title_wid_C31.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_C31.setStyleSheet(u"background-color: rgb(41, 46, 57);")
        self.frame_title_wid_C31.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_C31.setFrameShadow(QFrame.Raised)

##

        self.verticalLayout_C38 = QVBoxLayout(self.frame_title_wid_C31)
        self.verticalLayout_C38.setObjectName(u"verticalLayout_C38")
        self.labelBoxControllerCustomization = QLabel(self.frame_title_wid_C31)
        self.labelBoxControllerCustomization.setObjectName(u"labelBoxControllerCustomization")
        self.labelBoxControllerCustomization.setFont(font1)
        self.labelBoxControllerCustomization.setStyleSheet(u"")

        self.verticalLayout_C38.addWidget(self.labelBoxControllerCustomization)


        self.verticalLayout_C37.addWidget(self.frame_title_wid_C31)

##

        self.frame_content_wid_C31 = QFrame(self.frame_div_content_C31)
        self.frame_content_wid_C31.setObjectName(u"frame_content_wid_C31")
        self.frame_content_wid_C31.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_C31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_C39 = QHBoxLayout(self.frame_content_wid_C31)
        self.horizontalLayout_C39.setObjectName(u"horizontalLayout_C39")

        self.gridLayout_C31 = QGridLayout()
        self.gridLayout_C31.setObjectName(u"gridLayout_C31")
        self.gridLayout_C31.setContentsMargins(-1, -1, -1, 0)

        self.invertRollCheckBox = QCheckBox(self.frame_content_wid_C31)
        self.invertRollCheckBox.setObjectName(u"checkBox")
        self.invertRollCheckBox.setAutoFillBackground(False)
        self.invertRollCheckBox.setStyleSheet(u"")

        self.gridLayout_C31.addWidget(self.invertRollCheckBox, 0, 0, 1, 1)

        self.invertPitchCheckBox = QCheckBox(self.frame_content_wid_C31)
        self.invertPitchCheckBox.setObjectName(u"checkBox")
        self.invertPitchCheckBox.setAutoFillBackground(False)
        self.invertPitchCheckBox.setStyleSheet(u"")

        self.gridLayout_C31.addWidget(self.invertPitchCheckBox, 1, 0, 1, 1)

        self.invertYawCheckBox = QCheckBox(self.frame_content_wid_C31)
        self.invertYawCheckBox.setObjectName(u"checkBox")
        self.invertYawCheckBox.setAutoFillBackground(False)
        self.invertYawCheckBox.setStyleSheet(u"")

        self.gridLayout_C31.addWidget(self.invertYawCheckBox, 2, 0, 1, 1)

        self.horizontalLayout_C39.addLayout(self.gridLayout_C31)
        self.verticalLayout_C37.addWidget(self.frame_content_wid_C31)


        ##

        self.verticalLayout_C315.addWidget(self.frame_div_content_C31)

        ####
        ####

        self.verticalLayout_C6.addWidget(self.frame_C31)


        ####
        #BOX END
        ####



        self.stackedWidget.addWidget(self.page_controllers)

        #######################
        #######################


        #######################
        #######################

        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_S6 = QVBoxLayout(self.page_settings)
        self.verticalLayout_S6.setObjectName(u"verticalLayout_S6")

#####



        self.gridLayout_A1 = QGridLayout()
        self.gridLayout_A1.setObjectName(u"gridLayout_A1")
        self.gridLayout_A1.setContentsMargins(-1, -1, -1, 0)

        ####
        #BOX START
        ####

        self.frame_S41 = QFrame(self.page_settings)
        self.frame_S41.setObjectName(u"frame_S41")
        self.frame_S41.setStyleSheet(u"border-radius: 5px;")
        self.frame_S41.setFrameShape(QFrame.StyledPanel)
        self.frame_S41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_S415 = QVBoxLayout(self.frame_S41)
        self.verticalLayout_S415.setSpacing(0)
        self.verticalLayout_S415.setObjectName(u"verticalLayout_S415")
        self.verticalLayout_S415.setContentsMargins(0, 0, 0, 0)


        ####
        ####


        self.frame_div_content_S41 = QFrame(self.frame_S41)
        self.frame_div_content_S41.setObjectName(u"frame_div_content_S41")
        self.frame_div_content_S41.setMinimumSize(QSize(0, 100))
        self.frame_div_content_S41.setMaximumSize(QSize(16777215, 350))
        self.frame_div_content_S41.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_S41.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_S41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_S47 = QVBoxLayout(self.frame_div_content_S41)
        self.verticalLayout_S47.setSpacing(0)
        self.verticalLayout_S47.setObjectName(u"verticalLayout_7")
        self.verticalLayout_S47.setContentsMargins(0, 0, 0, 0)

        self.frame_title_wid_S41 = QFrame(self.frame_div_content_S41)
        self.frame_title_wid_S41.setObjectName(u"frame_title_wid_S41")
        self.frame_title_wid_S41.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_S41.setStyleSheet(u"background-color: rgb(41, 46, 57);")
        self.frame_title_wid_S41.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_S41.setFrameShadow(QFrame.Raised)

        self.verticalLayout_S48 = QVBoxLayout(self.frame_title_wid_S41)
        self.verticalLayout_S48.setObjectName(u"verticalLayout_S48")
        self.labelBoxGeneralSettings = QLabel(self.frame_title_wid_S41)
        self.labelBoxGeneralSettings.setObjectName(u"labelBoxGeneralSettings")
        self.labelBoxGeneralSettings.setFont(font1)
        self.labelBoxGeneralSettings.setStyleSheet(u"")

        self.verticalLayout_S48.addWidget(self.labelBoxGeneralSettings)


        self.verticalLayout_S47.addWidget(self.frame_title_wid_S41)

        ##

        self.frame_content_wid_S42 = QFrame(self.frame_div_content_S41)
        self.frame_content_wid_S42.setObjectName(u"frame_content_wid_S42")
        self.frame_content_wid_S42.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_S42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_S49 = QHBoxLayout(self.frame_content_wid_S42)
        self.horizontalLayout_S49.setObjectName(u"horizontalLayout_S49")

        self.gridLayout_S41 = QGridLayout()
        self.gridLayout_S41.setObjectName(u"gridLayout_S41")
        self.gridLayout_S41.setContentsMargins(-1, -1, -1, 0)

        self.hotkeyCheckBox = QCheckBox(self.frame_content_wid_S42)
        self.hotkeyCheckBox.setObjectName(u"checkBox")
        self.hotkeyCheckBox.setAutoFillBackground(False)
        self.hotkeyCheckBox.setStyleSheet(u"")

        self.gridLayout_S41.addWidget(self.hotkeyCheckBox, 0, 0, 1, 1)

        self.voiceCheckBox = QCheckBox(self.frame_content_wid_S42)
        self.voiceCheckBox.setObjectName(u"checkBox")
        self.voiceCheckBox.setAutoFillBackground(False)
        self.voiceCheckBox.setStyleSheet(u"")

        self.gridLayout_S41.addWidget(self.voiceCheckBox, 1, 0, 1, 1)

        self.MQTTCheckBox = QCheckBox(self.frame_content_wid_S42)
        self.MQTTCheckBox.setObjectName(u"checkBox")
        self.MQTTCheckBox.setAutoFillBackground(False)
        self.MQTTCheckBox.setStyleSheet(u"")

        self.gridLayout_S41.addWidget(self.MQTTCheckBox, 2, 0, 1, 1)


        self.horizontalLayout_S49.addLayout(self.gridLayout_S41)

        self.verticalLayout_S47.addWidget(self.frame_content_wid_S42)
        ##

        self.verticalLayout_S415.addWidget(self.frame_div_content_S41)

        ####
        ####

        ####
        #BOX END
        ####

        self.gridLayout_A1.addWidget(self.frame_S41, 0, 0, 1, 1)

        ####
        #BOX START
        ####

        self.frame_S1 = QFrame(self.page_settings)
        self.frame_S1.setObjectName(u"frame_S1")
        self.frame_S1.setStyleSheet(u"border-radius: 5px;")
        self.frame_S1.setFrameShape(QFrame.StyledPanel)
        self.frame_S1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_S15 = QVBoxLayout(self.frame_S1)
        self.verticalLayout_S15.setSpacing(0)
        self.verticalLayout_S15.setObjectName(u"verticalLayout_S15")
        self.verticalLayout_S15.setContentsMargins(0, 0, 0, 0)

        ####
        ####

        self.frame_div_content_S1 = QFrame(self.frame_S1)
        self.frame_div_content_S1.setObjectName(u"frame_div_content_S1")
        self.frame_div_content_S1.setMinimumSize(QSize(0, 100))
        self.frame_div_content_S1.setMaximumSize(QSize(16777215, 350))
        self.frame_div_content_S1.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_S1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_S1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_S7 = QVBoxLayout(self.frame_div_content_S1)
        self.verticalLayout_S7.setSpacing(0)
        self.verticalLayout_S7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_S7.setContentsMargins(0, 0, 0, 0)

        self.frame_title_wid_S1 = QFrame(self.frame_div_content_S1)
        self.frame_title_wid_S1.setObjectName(u"frame_title_wid_S1")
        self.frame_title_wid_S1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_S1.setStyleSheet(u"background-color: rgb(41, 46, 57);")
        self.frame_title_wid_S1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_S1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_S8 = QVBoxLayout(self.frame_title_wid_S1)
        self.verticalLayout_S8.setObjectName(u"verticalLayout_S8")
        self.labelBoxOpentrackSettings = QLabel(self.frame_title_wid_S1)
        self.labelBoxOpentrackSettings.setObjectName(u"labelBoxOpentrackSettings")
        self.labelBoxOpentrackSettings.setFont(font1)
        self.labelBoxOpentrackSettings.setStyleSheet(u"")

        self.verticalLayout_S8.addWidget(self.labelBoxOpentrackSettings)


        self.verticalLayout_S7.addWidget(self.frame_title_wid_S1)


        ##

        self.frame_content_wid_S2 = QFrame(self.frame_div_content_S1)
        self.frame_content_wid_S2.setObjectName(u"frame_content_wid_S2")
        self.frame_content_wid_S2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_S2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_S10 = QHBoxLayout(self.frame_content_wid_S2)
        self.horizontalLayout_S10.setObjectName(u"horizontalLayout_S10")


        self.gridLayout_S2 = QGridLayout()
        self.gridLayout_S2.setObjectName(u"gridLayout_S2")
        self.gridLayout_S2.setContentsMargins(-1, -1, -1, 0)

        self.label_opentrack_info = QLabel(self.frame_div_content_S1)
        self.label_opentrack_info.setWordWrap(True)
        self.label_opentrack_info.setMargin(0)
        self.label_opentrack_info.setAlignment(Qt.AlignTop)
        self.label_opentrack_info.setObjectName(u"label_opentrack_info")
        self.label_opentrack_info.setMaximumSize(QSize(16777215, 140))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_opentrack_info.setFont(font2)
        self.label_opentrack_info.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.gridLayout_S2.addWidget(self.label_opentrack_info, 0, 0, 1, 1)


        self.opentrackIPEdit = QLineEdit(self.frame_title_wid_S1)
        self.opentrackIPEdit.setObjectName(u"opentrackIPEdit")
        self.opentrackIPEdit.setMinimumSize(QSize(0, 30))
        self.opentrackIPEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_S2.addWidget(self.opentrackIPEdit, 2, 0, 1, 1)

        self.opentrackPortEdit = QLineEdit(self.frame_title_wid_S1)
        self.opentrackPortEdit.setObjectName(u"opentrackPortEdit")
        self.opentrackPortEdit.setMinimumSize(QSize(0, 30))
        self.opentrackPortEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_S2.addWidget(self.opentrackPortEdit, 4, 0, 1, 1)



        self.label_S1 = QLabel(self.frame_title_wid_S1)
        self.label_S1.setObjectName(u"label_S1")
        self.label_S1.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_S1.setLineWidth(1)
        self.label_S1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_S2.addWidget(self.label_S1, 1, 0, 1, 1)

        self.label_S2 = QLabel(self.frame_title_wid_S1)
        self.label_S2.setObjectName(u"label_S2")
        self.label_S2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_S2.setLineWidth(1)
        self.label_S2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_S2.addWidget(self.label_S2, 3, 0, 1, 1)

        self.opentrackTestButton = QPushButton(self.frame_title_wid_S1)
        self.opentrackTestButton.setObjectName(u"opentrackTestButton")
        self.opentrackTestButton.setMinimumSize(QSize(0, 30))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        self.opentrackTestButton.setFont(font8)
        self.opentrackTestButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.opentrackTestButton.setIcon(icon3)

        self.gridLayout_S2.addWidget(self.opentrackTestButton, 6, 0, 1, 1)

        self.label_S3 = QLabel(self.frame_title_wid_S1)
        self.label_S3.setObjectName(u"label_S3")
        self.label_S3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_S3.setLineWidth(1)
        self.label_S3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_S2.addWidget(self.label_S3, 5, 0, 1, 1)

        self.horizontalLayout_S10.addLayout(self.gridLayout_S2)
        self.verticalLayout_S7.addWidget(self.frame_content_wid_S2)


        ##





        ##

        self.verticalLayout_S15.addWidget(self.frame_div_content_S1)


        ####
        #BOX END
        ####

        self.gridLayout_A1.addWidget(self.frame_S1, 1, 0, 1, 1)


        ####
        #BOX START
        ####

        self.frame_S11 = QFrame(self.page_settings)
        self.frame_S11.setObjectName(u"frame_S11")
        self.frame_S11.setStyleSheet(u"border-radius: 5px;")
        self.frame_S11.setFrameShape(QFrame.StyledPanel)
        self.frame_S11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_S115 = QVBoxLayout(self.frame_S11)
        self.verticalLayout_S115.setSpacing(0)
        self.verticalLayout_S115.setObjectName(u"verticalLayout_S115")
        self.verticalLayout_S115.setContentsMargins(0, 0, 0, 0)


        ####
        ####


        self.frame_div_content_S11 = QFrame(self.frame_S11)
        self.frame_div_content_S11.setObjectName(u"frame_div_content_S11")
        self.frame_div_content_S11.setMinimumSize(QSize(0, 100))
        self.frame_div_content_S11.setMaximumSize(QSize(16777215, 178))
        self.frame_div_content_S11.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_S11.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_S11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_S17 = QVBoxLayout(self.frame_div_content_S11)
        self.verticalLayout_S17.setSpacing(0)
        self.verticalLayout_S17.setObjectName(u"verticalLayout_7")
        self.verticalLayout_S17.setContentsMargins(0, 0, 0, 0)

        self.frame_title_wid_S11 = QFrame(self.frame_div_content_S11)
        self.frame_title_wid_S11.setObjectName(u"frame_title_wid_S11")
        self.frame_title_wid_S11.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_S11.setStyleSheet(u"background-color: rgb(41, 46, 57);")
        self.frame_title_wid_S11.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_S11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_S18 = QVBoxLayout(self.frame_title_wid_S11)
        self.verticalLayout_S18.setObjectName(u"verticalLayout_S18")
        self.labelBoxVoiceSettings = QLabel(self.frame_title_wid_S11)
        self.labelBoxVoiceSettings.setObjectName(u"labelBoxVoiceSettings")
        self.labelBoxVoiceSettings.setFont(font1)
        self.labelBoxVoiceSettings.setStyleSheet(u"")

        self.verticalLayout_S18.addWidget(self.labelBoxVoiceSettings)


        self.verticalLayout_S17.addWidget(self.frame_title_wid_S11)



##

        self.frame_content_wid_S11 = QFrame(self.frame_div_content_S11)
        self.frame_content_wid_S11.setObjectName(u"frame_content_wid_S11")
        self.frame_content_wid_S11.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_S11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_S19 = QHBoxLayout(self.frame_content_wid_S11)
        self.horizontalLayout_S19.setObjectName(u"horizontalLayout_S19")

        self.gridLayout_S11 = QGridLayout()
        self.gridLayout_S11.setObjectName(u"gridLayout_S11")
        self.gridLayout_S11.setContentsMargins(-1, -1, -1, 0)

        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)

        self.label_voice_info = QLabel(self.frame_div_content_S11)
        self.label_voice_info.setWordWrap(True)
        self.label_voice_info.setMargin(0)
        self.label_voice_info.setAlignment(Qt.AlignTop)
        self.label_voice_info.setObjectName(u"label_voice_info")
        self.label_voice_info.setMaximumSize(QSize(16777215, 140))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_voice_info.setFont(font2)
        self.label_voice_info.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.gridLayout_S11.addWidget(self.label_voice_info, 0, 0, 1, 1)

        self.voiceSelection = QComboBox(self.frame_content_wid_S11)
        self.voiceSelection.setObjectName(u"comboBox")
        self.voiceSelection.setFont(font8)
        self.voiceSelection.setAutoFillBackground(False)
        self.voiceSelection.setMinimumSize(QSize(370, 30))
        self.voiceSelection.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.voiceSelection.setIconSize(QSize(16, 16))
        self.voiceSelection.setFrame(True)

        self.gridLayout_S11.addWidget(self.voiceSelection, 1, 0, 1, 1)

        self.label_S22 = QLabel(self.frame_title_wid_S1)
        self.label_S22.setObjectName(u"label_S2")
        self.label_S22.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_S22.setLineWidth(1)
        self.label_S22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_S11.addWidget(self.label_S22, 2, 0, 1, 1)

        self.voiceTestButton = QPushButton(self.frame_content_wid_S11)
        self.voiceTestButton.setObjectName(u"voiceTestButton")
        self.voiceTestButton.setMinimumSize(QSize(50, 30))

        self.voiceTestButton.setFont(font8)
        self.voiceTestButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        iconS3 = QIcon()
        iconS3.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.voiceTestButton.setIcon(iconS3)

        self.gridLayout_S11.addWidget(self.voiceTestButton, 3, 0, 1, 1)


        self.horizontalLayout_S19.addLayout(self.gridLayout_S11)
        self.verticalLayout_S17.addWidget(self.frame_content_wid_S11)


        ##

        self.verticalLayout_S115.addWidget(self.frame_div_content_S11)

        ####
        ####

        ####
        #BOX END
        ####


        self.gridLayout_A1.addWidget(self.frame_S11, 0, 1, 1, 1)

        ####
        #BOX START
        ####

        self.frame_S21 = QFrame(self.page_settings)
        self.frame_S21.setObjectName(u"frame_S21")
        self.frame_S21.setStyleSheet(u"border-radius: 5px;")
        self.frame_S21.setFrameShape(QFrame.StyledPanel)
        self.frame_S21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_S215 = QVBoxLayout(self.frame_S21)
        self.verticalLayout_S215.setSpacing(0)
        self.verticalLayout_S215.setObjectName(u"verticalLayout_S215")
        self.verticalLayout_S215.setContentsMargins(0, 0, 0, 0)


        ####
        ####


        self.frame_div_content_S21 = QFrame(self.frame_S21)
        self.frame_div_content_S21.setObjectName(u"frame_div_content_S21")
        self.frame_div_content_S21.setMinimumSize(QSize(0, 100))
        self.frame_div_content_S21.setMaximumSize(QSize(16777215, 350))
        self.frame_div_content_S21.setStyleSheet(u"background-color: rgb(41, 46, 57);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_S21.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_S21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_S27 = QVBoxLayout(self.frame_div_content_S21)
        self.verticalLayout_S27.setSpacing(0)
        self.verticalLayout_S27.setObjectName(u"verticalLayout_7")
        self.verticalLayout_S27.setContentsMargins(0, 0, 0, 0)

        self.frame_title_wid_S21 = QFrame(self.frame_div_content_S21)
        self.frame_title_wid_S21.setObjectName(u"frame_title_wid_S21")
        self.frame_title_wid_S21.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_S21.setStyleSheet(u"background-color: rgb(41, 46, 57);")
        self.frame_title_wid_S21.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_S21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_S28 = QVBoxLayout(self.frame_title_wid_S21)
        self.verticalLayout_S28.setObjectName(u"verticalLayout_S28")
        self.labelBoxMQTTSettings = QLabel(self.frame_title_wid_S21)
        self.labelBoxMQTTSettings.setObjectName(u"labelBoxMQTTSettings")
        self.labelBoxMQTTSettings.setFont(font1)
        self.labelBoxMQTTSettings.setStyleSheet(u"")

        self.verticalLayout_S28.addWidget(self.labelBoxMQTTSettings)


        self.verticalLayout_S27.addWidget(self.frame_title_wid_S21)

        ##

        self.frame_content_wid_S52 = QFrame(self.frame_div_content_S21)
        self.frame_content_wid_S52.setObjectName(u"frame_content_wid_S52")
        self.frame_content_wid_S52.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_S52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_S510 = QHBoxLayout(self.frame_content_wid_S52)
        self.horizontalLayout_S510.setObjectName(u"horizontalLayout_S510")

        self.gridLayout_S52 = QGridLayout()
        self.gridLayout_S52.setObjectName(u"gridLayout_S52")
        self.gridLayout_S52.setContentsMargins(-1, -1, -1, 0)


        self.label_mqtt_info = QLabel(self.frame_div_content_S21)
        self.label_mqtt_info.setWordWrap(True)
        self.label_mqtt_info.setMargin(0)
        self.label_mqtt_info.setAlignment(Qt.AlignTop)
        self.label_mqtt_info.setObjectName(u"label_mqtt_info")
        self.label_mqtt_info.setMaximumSize(QSize(16777215, 140))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_mqtt_info.setFont(font2)
        self.label_mqtt_info.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.gridLayout_S52.addWidget(self.label_mqtt_info, 0, 0, 1, 2)


        self.MQTTIPEdit = QLineEdit(self.frame_title_wid_S21)
        self.MQTTIPEdit.setObjectName(u"MQTTIPEdit")
        self.MQTTIPEdit.setMinimumSize(QSize(0, 30))
        self.MQTTIPEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_S52.addWidget(self.MQTTIPEdit, 2, 0, 1, 1)

        self.MQTTPortEdit = QLineEdit(self.frame_title_wid_S21)
        #iprx = QRegExp("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
        #iprxv = QRegExpValidator(iprx, self.frame_title_wid_S21)
        #self.MQTTPortEdit.setValidator(iprxv)
        self.MQTTPortEdit.setObjectName(u"MQTTPortEdit")
        self.MQTTPortEdit.setMinimumSize(QSize(0, 30))
        self.MQTTPortEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_S52.addWidget(self.MQTTPortEdit, 4, 0, 1, 1)


        self.MQTTUserEdit = QLineEdit(self.frame_title_wid_S21)
        self.MQTTUserEdit.setObjectName(u"MQTTUserEdit")
        self.MQTTUserEdit.setMinimumSize(QSize(0, 30))
        self.MQTTUserEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_S52.addWidget(self.MQTTUserEdit, 2, 1, 1, 1)

        self.MQTTPassEdit = QLineEdit(self.frame_title_wid_S21)
        self.MQTTPassEdit.setObjectName(u"MQTTPassEdit")
        self.MQTTPassEdit.setEchoMode(QLineEdit.Password)
        self.MQTTPassEdit.setMinimumSize(QSize(0, 30))
        self.MQTTPassEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_S52.addWidget(self.MQTTPassEdit, 4, 1, 1, 1)


        self.label_S51 = QLabel(self.frame_title_wid_S21)
        self.label_S51.setObjectName(u"label_S51")
        self.label_S51.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_S51.setLineWidth(1)
        self.label_S51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_S52.addWidget(self.label_S51, 1, 0, 1, 1)

        self.label_S52 = QLabel(self.frame_title_wid_S21)
        self.label_S52.setObjectName(u"label_S52")
        self.label_S52.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_S52.setLineWidth(1)
        self.label_S52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_S52.addWidget(self.label_S52, 3, 0, 1, 1)

        self.label_S54 = QLabel(self.frame_title_wid_S21)
        self.label_S54.setObjectName(u"label_S51")
        self.label_S54.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_S54.setLineWidth(1)
        self.label_S54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_S52.addWidget(self.label_S54, 1, 1, 1, 1)

        self.label_S55 = QLabel(self.frame_title_wid_S21)
        self.label_S55.setObjectName(u"label_S52")
        self.label_S55.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_S55.setLineWidth(1)
        self.label_S55.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_S52.addWidget(self.label_S55, 3, 1, 1, 1)

        self.MQTTTestButton = QPushButton(self.frame_title_wid_S21)
        self.MQTTTestButton.setObjectName(u"MQTTTestButton")
        self.MQTTTestButton.setMinimumSize(QSize(0, 30))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        self.MQTTTestButton.setFont(font8)
        self.MQTTTestButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MQTTTestButton.setIcon(icon3)

        self.gridLayout_S52.addWidget(self.MQTTTestButton, 6, 0, 1, 2)

        self.label_S53 = QLabel(self.frame_title_wid_S21)
        self.label_S53.setObjectName(u"label_S53")
        self.label_S53.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_S53.setLineWidth(1)
        self.label_S53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_S52.addWidget(self.label_S53, 5, 0, 1, 1)

        self.horizontalLayout_S510.addLayout(self.gridLayout_S52)
        self.verticalLayout_S27.addWidget(self.frame_content_wid_S52)

        ##

        self.verticalLayout_S215.addWidget(self.frame_div_content_S21)

        ####
        ####

        ####
        #BOX END
        ####


        self.gridLayout_A1.addWidget(self.frame_S21, 1, 1, 1, 1)

        ####
        self.verticalLayout_S6.addLayout(self.gridLayout_A1)
        #####


        self.stackedWidget.addWidget(self.page_settings)

        #######################
        #######################


        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setTextFormat(Qt.RichText)
        self.label_credits.setOpenExternalLinks(True)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setTextFormat(Qt.RichText)
        self.label_version.setOpenExternalLinks(True)
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)


        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_controller_info.setText(QCoreApplication.translate("MainWindow", u"CamBot 6D is compatible with any regular keyboard and mouse.\n\nNote: Does not work in fullscreen mode. Will display an overlay window that captures all mouse and keyboard input while setting waypoints. Can be activated via graphical user interface or Stream Deck MQTT remote.", None))
        self.label_voice_info.setText(QCoreApplication.translate("MainWindow", "Audio feedback useful for single monitor gaming setups in 'Fullscreen' window mode where you can't watch the interface for messages.\n", None))
        self.label_opentrack_info.setText(QCoreApplication.translate("MainWindow", "Please start opentrack on your gaming PC with 'UDP over network' input and 'freetrack 2.0 Enhanced' output. CamBot 6D can connect to opentrack from any PC within the same network.\n", None))
        self.label_mqtt_info.setText(QCoreApplication.translate("MainWindow", "MQTT is a network messaging protocol that allows you to connect CamBot 6D to programmable devices (like the Elgato Stream Deck) or smart home interfaces (like the Home Assistant control system). This feature requires an MQTT broker such as Eclipse Mosquitto™.\n", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| CAMERA", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"WM", None))

        self.label_help_info.setText(QCoreApplication.translate("MainWindow", u"<p style=\"margin: 0;\">For any of this to work, you need:<p><p style=\"margin: 0; margin-top: 5px;\"><a style=\"color: #d2d2d2; text-decoration: none;\" href=\"https://github.com/opentrack/opentrack/releases\"><strong>opentrack</strong></a> (a head tracking data relay software)</p><p style=\"margin: 0; margin-left: 10px;\">started with linear mapping, 'UDP over network' input, 'freetrack 2.0 Enhanced' output,<br/>filter set to 'Accela' with low smoothing (Rotation 1°, Position 0.3mm) and no deadzone (Rotation 0°, Position 0mm)</p><p style=\"margin: 0; margin-top: 3px;\"><a style=\"color: #d2d2d2;  text-decoration: none;\" href=\"https://robertsspaceindustries.com/enlist?referral=STAR-F3GJ-MFBD\"><strong>Star Citizen</strong></a> (coming soon™)</p><p style=\"margin: 0; margin-left: 10px;\">set to 'COMMS, FOIP & HEADTRACKING' → 'Head Tracking' → 'General' → 'Source' = [ <strong>TrackIR</strong> ], 'Toggle Enabled' = [ <strong>No</strong> ]<br/>and 'KEYBINDINGS' → 'Keyboard / Mouse' → 'ADVANCED CONTROLS CUSTOMIZATION' → 'VOIP, FOIP and Head Tracking' → 'Enable / Disable Head Tracking for 3rd Person Camera (Toggle)' = [ <strong>Left Shift + Numpad /</strong> ] (and <strong>toggled on</strong> in game)</p>", None))


        self.pushButton_add_waypoint.setText(QCoreApplication.translate("MainWindow", u" ADD WAYPOINT", None))
        self.pushButton_delete_all.setText(QCoreApplication.translate("MainWindow", u" DELETE ALL", None))

        self.labelBoxCamera.setText(QCoreApplication.translate("MainWindow", u"CAMERA CONTROLS", None))
        self.labelBoxSpeed.setText(QCoreApplication.translate("MainWindow", u"SPEED", None))

        self.pushButton_prev.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.pushButton_home.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.pushButton_forward.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.pushButton_backward.setText(QCoreApplication.translate("MainWindow", u"REVERSE", None))

        self.labelBoxControllers.setText(QCoreApplication.translate("MainWindow", u"CONTROLLER SETUP", None))
        self.labelBoxOpentrackSettings.setText(QCoreApplication.translate("MainWindow", u"OPENTRACK COMMUNICATION", None))
        self.labelBoxVoiceSettings.setText(QCoreApplication.translate("MainWindow", u"VOICE OUTPUT", None))
        self.labelBoxMQTTSettings.setText(QCoreApplication.translate("MainWindow", u"MQTT REMOTE", None))
        self.labelBoxGeneralSettings.setText(QCoreApplication.translate("MainWindow", u"GENERAL", None))
        self.labelBoxControllerCustomization.setText(QCoreApplication.translate("MainWindow", u"CUSTOMIZATION", None))

        self.labelBoxGeneralSettings.setText(QCoreApplication.translate("MainWindow", u"GENERAL", None))
        self.labelBoxGeneralSettings.setText(QCoreApplication.translate("MainWindow", u"GENERAL", None))

        self.labelBoxResources.setText(QCoreApplication.translate("MainWindow", u"ONLINE RESOURCES", None))
        self.label_resources_info.setText(QCoreApplication.translate("MainWindow", u"CamBot 6D was developed by LordSkippy.com &ndash; subscribe to my <a style=\"color: white;\" href=\"https://www.youtube.com/LordSkippyTheMeh?sub_confirmation=1\"><strong>YouTube channel</strong></a> for news and updates.</p><p>Documentation</p><p>Installation instructions</p><p>MQTT API commands</p><p>Source code</p><p>Issue council</p>", None))

        self.labelBoxLicense.setText(QCoreApplication.translate("MainWindow", u"DISTRIBUTED UNDER MIT LICENSE", None))
        self.label_license_info.setText(QCoreApplication.translate("MainWindow", u"<strong>Copyright © 2020 Wanderson M. Pimenta<br/>Copyright © 2022 Simon F. Barke</strong><p>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:</p><p>The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.</p><p>THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>", None))

        self.label_ease_info.setText(QCoreApplication.translate("MainWindow", u"Camera path time interpolation", None))
        self.label_pathtime_info.setText(QCoreApplication.translate("MainWindow", u"Duration of full camera path motion", None))
        self.label_pointtime_info.setText(QCoreApplication.translate("MainWindow", u"Duration of single waypoint skip", None))

        self.opentrackIPEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"default: 127.0.0.1", None))
        self.opentrackPortEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"default: 4242", None))
        self.opentrackTestButton.setText(QCoreApplication.translate("MainWindow", u" SEND TEST DATA", None))
        self.MQTTTestButton.setText(QCoreApplication.translate("MainWindow", u" CONNECT TO BROKER", None))
        self.controllerTestButton.setText(QCoreApplication.translate("MainWindow", u" TEST", None))
        self.voiceTestButton.setText(QCoreApplication.translate("MainWindow", u" PLAY VOICE SAMPLE", None))
        self.label_S1.setText(QCoreApplication.translate("MainWindow", u"IP address of gaming PC:", None))
        self.label_S2.setText(QCoreApplication.translate("MainWindow", u"opentrack UDP port:", None))

        self.label_S51.setText(QCoreApplication.translate("MainWindow", u"IP address of MQTT broker:", None))
        self.label_S52.setText(QCoreApplication.translate("MainWindow", u"MQTT broker port:", None))
        self.label_S54.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_S55.setText(QCoreApplication.translate("MainWindow", u"Password:", None))

        self.MQTTIPEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"default: 127.0.0.1", None))
        self.MQTTPortEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"default: 1883", None))

        self.voiceCheckBox.setText(QCoreApplication.translate("MainWindow", u" Enable voice output", None))
        self.hotkeyCheckBox.setText(QCoreApplication.translate("MainWindow", u" Enable hot key: [Alt] + [Num+]", None))
        self.MQTTCheckBox.setText(QCoreApplication.translate("MainWindow", u" Enable MQTT remote", None))


        self.invertRollCheckBox.setText(QCoreApplication.translate("MainWindow", u" Invert roll axis", None))
        self.invertPitchCheckBox.setText(QCoreApplication.translate("MainWindow", u" Invert pitch axis", None))
        self.invertYawCheckBox.setText(QCoreApplication.translate("MainWindow", u" Invert yaw axis", None))



        ___qtablewidgetitemH1 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitemH1.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitemH2 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitemH2.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        ___qtablewidgetitemH3 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitemH3.setText(QCoreApplication.translate("MainWindow", u"Z", None));
        ___qtablewidgetitemH4 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitemH4.setText(QCoreApplication.translate("MainWindow", u"Yaw", None));
        ___qtablewidgetitemH5 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitemH5.setText(QCoreApplication.translate("MainWindow", u"Pitch", None));
        ___qtablewidgetitemH6 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitemH6.setText(QCoreApplication.translate("MainWindow", u"Roll", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"", None));
        ___qtablewidgetitem24 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"", None));
        ___qtablewidgetitem25 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"<a style=\"text-decoration: none; color: #62676f;\" href=\"https://robertsspaceindustries.com/citizens/LordSkippy\">by /citizens/LordSkippy</a>", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"<a style=\"text-decoration: none; color: #62676f;\" href=\"https://www.lordskippy.com/software/virtual-camera-robot#h.nrhw9hcv3l2i\">v0.3.0</a>", None))
    # retranslateUi
