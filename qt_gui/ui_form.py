# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyvistaqt import QtInteractor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(861, 581)
        self.mnOpen = QAction(MainWindow)
        self.mnOpen.setObjectName(u"mnOpen")
        self.mnLoad_data = QAction(MainWindow)
        self.mnLoad_data.setObjectName(u"mnLoad_data")
        self.mnSave = QAction(MainWindow)
        self.mnSave.setObjectName(u"mnSave")
        self.mnSave_as = QAction(MainWindow)
        self.mnSave_as.setObjectName(u"mnSave_as")
        self.mnQuit = QAction(MainWindow)
        self.mnQuit.setObjectName(u"mnQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_widget = QtInteractor(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.frame_controls = QFrame(self.main_widget)
        self.frame_controls.setObjectName(u"frame_controls")
        self.frame_controls.setGeometry(QRect(590, 0, 250, 270))
        self.frame_controls.setMinimumSize(QSize(250, 270))
        self.frame_controls.setAutoFillBackground(True)
        self.frame_controls.setFrameShape(QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_controls)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 241, 258))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameRegions = QFrame(self.layoutWidget)
        self.frameRegions.setObjectName(u"frameRegions")
        self.frameRegions.setMinimumSize(QSize(0, 150))
        self.frameRegions.setFrameShape(QFrame.StyledPanel)
        self.frameRegions.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frameRegions)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 231, 151))
        self.layout_regions = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_regions.setObjectName(u"layout_regions")
        self.layout_regions.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frameRegions, 0, 0, 1, 1)

        self.frameSliderRadius = QFrame(self.layoutWidget)
        self.frameSliderRadius.setObjectName(u"frameSliderRadius")
        self.frameSliderRadius.setMinimumSize(QSize(0, 80))
        self.frameSliderRadius.setFrameShape(QFrame.StyledPanel)
        self.frameSliderRadius.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frameSliderRadius)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 10, 231, 51))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelRadius = QLabel(self.layoutWidget1)
        self.labelRadius.setObjectName(u"labelRadius")

        self.gridLayout_3.addWidget(self.labelRadius, 0, 0, 1, 1)

        self.radiusSlider = QSlider(self.layoutWidget1)
        self.radiusSlider.setObjectName(u"radiusSlider")
        self.radiusSlider.setMinimum(10)
        self.radiusSlider.setMaximum(1000)
        self.radiusSlider.setSingleStep(10)
        self.radiusSlider.setPageStep(40)
        self.radiusSlider.setValue(100)
        self.radiusSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.radiusSlider, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameSliderRadius, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.main_widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 861, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.mnOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.mnSave)
        self.menuFile.addAction(self.mnSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.mnQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mnOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
#if QT_CONFIG(shortcut)
        self.mnOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.mnLoad_data.setText(QCoreApplication.translate("MainWindow", u"Load data...", None))
        self.mnSave.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
        self.mnSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.mnQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.labelRadius.setText(QCoreApplication.translate("MainWindow", u"Selection radius:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

