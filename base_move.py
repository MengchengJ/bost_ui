# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base_move.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1545, 1045)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.incang_button = QtWidgets.QPushButton(self.centralwidget)
        self.incang_button.setGeometry(QtCore.QRect(80, 60, 93, 28))
        self.incang_button.setObjectName("incang_button")
        self.out_button = QtWidgets.QPushButton(self.centralwidget)
        self.out_button.setGeometry(QtCore.QRect(80, 110, 93, 28))
        self.out_button.setObjectName("out_button")
        self.z_move_button = QtWidgets.QPushButton(self.centralwidget)
        self.z_move_button.setGeometry(QtCore.QRect(220, 60, 93, 28))
        self.z_move_button.setObjectName("z_move_button")
        self.x_move_button = QtWidgets.QPushButton(self.centralwidget)
        self.x_move_button.setGeometry(QtCore.QRect(340, 60, 93, 28))
        self.x_move_button.setObjectName("x_move_button")
        self.y_move_button = QtWidgets.QPushButton(self.centralwidget)
        self.y_move_button.setGeometry(QtCore.QRect(450, 60, 93, 28))
        self.y_move_button.setObjectName("y_move_button")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(80, 160, 93, 28))
        self.close_button.setObjectName("close_button")
        self.x_reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.x_reset_button.setGeometry(QtCore.QRect(330, 300, 93, 28))
        self.x_reset_button.setObjectName("x_reset_button")
        self.y_reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.y_reset_button.setGeometry(QtCore.QRect(450, 300, 93, 28))
        self.y_reset_button.setObjectName("y_reset_button")
        self.x_value = QtWidgets.QLineEdit(self.centralwidget)
        self.x_value.setGeometry(QtCore.QRect(340, 110, 91, 21))
        self.x_value.setObjectName("x_value")
        self.y_value = QtWidgets.QLineEdit(self.centralwidget)
        self.y_value.setGeometry(QtCore.QRect(450, 110, 91, 21))
        self.y_value.setObjectName("y_value")
        self.fouce_on_button = QtWidgets.QPushButton(self.centralwidget)
        self.fouce_on_button.setGeometry(QtCore.QRect(70, 300, 93, 28))
        self.fouce_on_button.setObjectName("fouce_on_button")
        self.make_0_button = QtWidgets.QPushButton(self.centralwidget)
        self.make_0_button.setGeometry(QtCore.QRect(210, 300, 93, 28))
        self.make_0_button.setObjectName("make_0_button")
        self.z_value = QtWidgets.QLineEdit(self.centralwidget)
        self.z_value.setGeometry(QtCore.QRect(220, 110, 91, 21))
        self.z_value.setObjectName("z_value")
        self.fluorsecent_value = QtWidgets.QLineEdit(self.centralwidget)
        self.fluorsecent_value.setGeometry(QtCore.QRect(70, 430, 91, 21))
        self.fluorsecent_value.setObjectName("fluorsecent_value")
        self.Brightfield_value = QtWidgets.QLineEdit(self.centralwidget)
        self.Brightfield_value.setGeometry(QtCore.QRect(200, 430, 91, 21))
        self.Brightfield_value.setObjectName("Brightfield_value")
        self.y_positive_button = QtWidgets.QPushButton(self.centralwidget)
        self.y_positive_button.setGeometry(QtCore.QRect(450, 150, 93, 28))
        self.y_positive_button.setObjectName("y_positive_button")
        self.y_negative_button = QtWidgets.QPushButton(self.centralwidget)
        self.y_negative_button.setGeometry(QtCore.QRect(450, 230, 93, 28))
        self.y_negative_button.setObjectName("y_negative_button")
        self.x_negative_button = QtWidgets.QPushButton(self.centralwidget)
        self.x_negative_button.setGeometry(QtCore.QRect(340, 230, 93, 28))
        self.x_negative_button.setObjectName("x_negative_button")
        self.x_positive_button = QtWidgets.QPushButton(self.centralwidget)
        self.x_positive_button.setGeometry(QtCore.QRect(340, 150, 93, 28))
        self.x_positive_button.setObjectName("x_positive_button")
        self.z_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.z_up_button.setGeometry(QtCore.QRect(220, 150, 93, 28))
        self.z_up_button.setObjectName("z_up_button")
        self.z_down_button = QtWidgets.QPushButton(self.centralwidget)
        self.z_down_button.setGeometry(QtCore.QRect(220, 230, 93, 28))
        self.z_down_button.setObjectName("z_down_button")
        self.fluorsecent_on_button = QtWidgets.QPushButton(self.centralwidget)
        self.fluorsecent_on_button.setGeometry(QtCore.QRect(70, 480, 93, 28))
        self.fluorsecent_on_button.setObjectName("fluorsecent_on_button")
        self.Brightfield_on_button = QtWidgets.QPushButton(self.centralwidget)
        self.Brightfield_on_button.setGeometry(QtCore.QRect(200, 480, 93, 28))
        self.Brightfield_on_button.setObjectName("Brightfield_on_button")
        self.fluorsecent_off_button = QtWidgets.QPushButton(self.centralwidget)
        self.fluorsecent_off_button.setGeometry(QtCore.QRect(70, 520, 93, 28))
        self.fluorsecent_off_button.setObjectName("fluorsecent_off_button")
        self.Brightfield_off_button = QtWidgets.QPushButton(self.centralwidget)
        self.Brightfield_off_button.setGeometry(QtCore.QRect(200, 520, 93, 28))
        self.Brightfield_off_button.setObjectName("Brightfield_off_button")
        self.label_flur = QtWidgets.QLabel(self.centralwidget)
        self.label_flur.setGeometry(QtCore.QRect(90, 400, 72, 20))
        self.label_flur.setObjectName("label_flur")
        self.label_Bright = QtWidgets.QLabel(self.centralwidget)
        self.label_Bright.setGeometry(QtCore.QRect(220, 400, 72, 20))
        self.label_Bright.setObjectName("label_Bright")
        self.label_wdi = QtWidgets.QLabel(self.centralwidget)
        self.label_wdi.setGeometry(QtCore.QRect(20, 300, 72, 20))
        self.label_wdi.setObjectName("label_wdi")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(610, 20, 900, 900))
        self.graphicsView.setObjectName("graphicsView")
        self.bright_capture_button = QtWidgets.QPushButton(self.centralwidget)
        self.bright_capture_button.setGeometry(QtCore.QRect(60, 570, 101, 31))
        self.bright_capture_button.setObjectName("bright_capture_button")
        self.fouce_off_buttion = QtWidgets.QPushButton(self.centralwidget)
        self.fouce_off_buttion.setGeometry(QtCore.QRect(70, 340, 93, 28))
        self.fouce_off_buttion.setObjectName("fouce_off_buttion")
        self.fluor_capture_button = QtWidgets.QPushButton(self.centralwidget)
        self.fluor_capture_button.setGeometry(QtCore.QRect(200, 570, 101, 31))
        self.fluor_capture_button.setObjectName("fluor_capture_button")
        self.zscan_button = QtWidgets.QPushButton(self.centralwidget)
        self.zscan_button.setGeometry(QtCore.QRect(210, 340, 93, 28))
        self.zscan_button.setObjectName("zscan_button")
        self.scan_up_limit = QtWidgets.QLineEdit(self.centralwidget)
        self.scan_up_limit.setGeometry(QtCore.QRect(450, 350, 91, 21))
        self.scan_up_limit.setObjectName("scan_up_limit")
        self.scan_down_limit = QtWidgets.QLineEdit(self.centralwidget)
        self.scan_down_limit.setGeometry(QtCore.QRect(450, 380, 91, 21))
        self.scan_down_limit.setObjectName("scan_down_limit")
        self.label_wdi_up = QtWidgets.QLabel(self.centralwidget)
        self.label_wdi_up.setGeometry(QtCore.QRect(410, 350, 72, 20))
        self.label_wdi_up.setObjectName("label_wdi_up")
        self.label_wdi_down = QtWidgets.QLabel(self.centralwidget)
        self.label_wdi_down.setGeometry(QtCore.QRect(410, 380, 72, 20))
        self.label_wdi_down.setObjectName("label_wdi_down")
        self.scan_step_value = QtWidgets.QLineEdit(self.centralwidget)
        self.scan_step_value.setGeometry(QtCore.QRect(450, 410, 91, 21))
        self.scan_step_value.setObjectName("scan_step_value")
        self.label_wdi_step = QtWidgets.QLabel(self.centralwidget)
        self.label_wdi_step.setGeometry(QtCore.QRect(410, 410, 72, 20))
        self.label_wdi_step.setObjectName("label_wdi_step")
        self.z_setp_value = QtWidgets.QLineEdit(self.centralwidget)
        self.z_setp_value.setGeometry(QtCore.QRect(220, 190, 91, 21))
        self.z_setp_value.setObjectName("z_setp_value")
        self.y_setp_value = QtWidgets.QLineEdit(self.centralwidget)
        self.y_setp_value.setGeometry(QtCore.QRect(450, 190, 91, 21))
        self.y_setp_value.setObjectName("y_setp_value")
        self.x_setp_value = QtWidgets.QLineEdit(self.centralwidget)
        self.x_setp_value.setGeometry(QtCore.QRect(340, 190, 91, 21))
        self.x_setp_value.setObjectName("x_setp_value")
        self.z_display = QtWidgets.QLineEdit(self.centralwidget)
        self.z_display.setGeometry(QtCore.QRect(220, 30, 91, 21))
        self.z_display.setDragEnabled(False)
        self.z_display.setObjectName("z_display")
        self.continuous_capture_button_on = QtWidgets.QPushButton(self.centralwidget)
        self.continuous_capture_button_on.setGeometry(QtCore.QRect(60, 620, 101, 31))
        self.continuous_capture_button_on.setObjectName("continuous_capture_button_on")
        self.x_display = QtWidgets.QLineEdit(self.centralwidget)
        self.x_display.setGeometry(QtCore.QRect(340, 30, 91, 21))
        self.x_display.setDragEnabled(False)
        self.x_display.setObjectName("x_display")
        self.y_display = QtWidgets.QLineEdit(self.centralwidget)
        self.y_display.setGeometry(QtCore.QRect(450, 30, 91, 21))
        self.y_display.setDragEnabled(False)
        self.y_display.setObjectName("y_display")
        self.continuous_capture_button_off = QtWidgets.QPushButton(self.centralwidget)
        self.continuous_capture_button_off.setGeometry(QtCore.QRect(200, 620, 101, 31))
        self.continuous_capture_button_off.setObjectName("continuous_capture_button_off")
        self.zscan_fcouse_value = QtWidgets.QLineEdit(self.centralwidget)
        self.zscan_fcouse_value.setGeometry(QtCore.QRect(330, 350, 61, 21))
        self.zscan_fcouse_value.setObjectName("zscan_fcouse_value")
        self.fluorsecent_on_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.fluorsecent_on_button_2.setGeometry(QtCore.QRect(60, 680, 101, 31))
        self.fluorsecent_on_button_2.setObjectName("fluorsecent_on_button_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1545, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.close_button.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.incang_button.setText(_translate("MainWindow", "进仓"))
        self.out_button.setText(_translate("MainWindow", "出仓"))
        self.z_move_button.setText(_translate("MainWindow", "Z"))
        self.x_move_button.setText(_translate("MainWindow", "X"))
        self.y_move_button.setText(_translate("MainWindow", "Y"))
        self.close_button.setText(_translate("MainWindow", "关闭"))
        self.x_reset_button.setText(_translate("MainWindow", "X复位"))
        self.y_reset_button.setText(_translate("MainWindow", "Y复位"))
        self.fouce_on_button.setText(_translate("MainWindow", "开启WDI对焦"))
        self.make_0_button.setText(_translate("MainWindow", "make 0"))
        self.y_positive_button.setText(_translate("MainWindow", "+"))
        self.y_negative_button.setText(_translate("MainWindow", "-"))
        self.x_negative_button.setText(_translate("MainWindow", "-"))
        self.x_positive_button.setText(_translate("MainWindow", "+"))
        self.z_up_button.setText(_translate("MainWindow", "+"))
        self.z_down_button.setText(_translate("MainWindow", "-"))
        self.fluorsecent_on_button.setText(_translate("MainWindow", "开启"))
        self.Brightfield_on_button.setText(_translate("MainWindow", "开启"))
        self.fluorsecent_off_button.setText(_translate("MainWindow", "关闭"))
        self.Brightfield_off_button.setText(_translate("MainWindow", "关闭"))
        self.label_flur.setText(_translate("MainWindow", "荧光"))
        self.label_Bright.setText(_translate("MainWindow", "明场"))
        self.label_wdi.setText(_translate("MainWindow", "WDI"))
        self.bright_capture_button.setText(_translate("MainWindow", "明场单帧采集"))
        self.fouce_off_buttion.setText(_translate("MainWindow", "关闭WDI对焦"))
        self.fluor_capture_button.setText(_translate("MainWindow", "荧光单帧采集"))
        self.zscan_button.setText(_translate("MainWindow", "z_scan"))
        self.label_wdi_up.setText(_translate("MainWindow", "上"))
        self.label_wdi_down.setText(_translate("MainWindow", "下"))
        self.label_wdi_step.setText(_translate("MainWindow", "步长"))
        self.continuous_capture_button_on.setText(_translate("MainWindow", "连续采集开启"))
        self.continuous_capture_button_off.setText(_translate("MainWindow", "连续采集关闭"))
        self.fluorsecent_on_button_2.setText(_translate("MainWindow", "测试1"))
