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
        self.frame_controls.setGeometry(QRect(520, 0, 321, 311))
        self.frame_controls.setAutoFillBackground(True)
        self.frame_controls.setFrameShape(QFrame.WinPanel)
        self.frame_controls.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_controls)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalControlsLayout = QVBoxLayout()
        self.verticalControlsLayout.setObjectName(u"verticalControlsLayout")
        self.frame_regions = QFrame(self.frame_controls)
        self.frame_regions.setObjectName(u"frame_regions")
        self.frame_regions.setMinimumSize(QSize(250, 200))
        self.frame_regions.setFrameShape(QFrame.StyledPanel)
        self.frame_regions.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_regions)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.layout_regions = QVBoxLayout()
        self.layout_regions.setSpacing(0)
        self.layout_regions.setObjectName(u"layout_regions")

        self.gridLayout_5.addLayout(self.layout_regions, 0, 0, 1, 1)


        self.verticalControlsLayout.addWidget(self.frame_regions)

        self.frameSliderRadius = QFrame(self.frame_controls)
        self.frameSliderRadius.setObjectName(u"frameSliderRadius")
        self.frameSliderRadius.setMinimumSize(QSize(0, 50))
        self.frameSliderRadius.setMaximumSize(QSize(16777215, 50))
        self.frameSliderRadius.setFrameShape(QFrame.StyledPanel)
        self.frameSliderRadius.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameSliderRadius)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelRadius = QLabel(self.frameSliderRadius)
        self.labelRadius.setObjectName(u"labelRadius")

        self.verticalLayout.addWidget(self.labelRadius)

        self.radiusSlider = QSlider(self.frameSliderRadius)
        self.radiusSlider.setObjectName(u"radiusSlider")
        self.radiusSlider.setMinimum(10)
        self.radiusSlider.setMaximum(1000)
        self.radiusSlider.setSingleStep(10)
        self.radiusSlider.setPageStep(40)
        self.radiusSlider.setValue(100)
        self.radiusSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.radiusSlider)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalControlsLayout.addWidget(self.frameSliderRadius)


        self.gridLayout_4.addLayout(self.verticalControlsLayout, 0, 0, 1, 1)


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

