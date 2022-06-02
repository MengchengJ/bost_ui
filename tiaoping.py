# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tiaoping.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import time
import pyqtgraph as pg
import traceback
import psutil
import numpy as np
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QGridLayout
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import common2 as com
import DDS2 as DDS
from PyQt5 import QtCore, QtGui, QtWidgets
import calculation_module
import bost_UI
global C



# class for plotting a specific figure static or dynamic

class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=10,height=10, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        super(Figure_Canvas, self).__init__(self.fig)
       # self.ax = self.fig.add_subplot(111)

    def mat_plot_drow(self, zz,zrange,Zs,I_LR,I_DU):
        """
        用清除画布刷新的方法绘图
        :return:
        """
        self.fig.clf()  # 清理画布，这里是clf()
        self.axes = self.fig.add_subplot(111)  # 清理画布后必须重新添加绘图区
        self.axes.set_xticks([])
        self.axes.set_yticks([])
        h=self.axes.imshow(zz,plt.get_cmap('jet'),vmin=-zrange, vmax=zrange)
        self.fig.colorbar(h)
        self.axes.set_title('Zmax=%.3f, Zmin=%.3f\nLeft-Right: %.2fum\nDown-Up: %.2fum' % (
         np.amax(Zs), np.amin(Zs), I_LR, I_DU))

        self.fig.canvas.draw()  # 这里注意是画布重绘，self.figs.canvas
        self.fig.canvas.flush_events()  # 画布刷新self.figs.canvas




class Ui_Tiaoping(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1318, 915)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_pushButton.setGeometry(QtCore.QRect(10, 50, 93, 28))
        self.start_pushButton.setObjectName("start_pushButton")
        self.end_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.end_pushButton.setGeometry(QtCore.QRect(10, 80, 93, 28))
        self.end_pushButton.setObjectName("end_pushButton")


        self.setp_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.setp_lineEdit.setGeometry(QtCore.QRect(120, 50, 71, 31))
        self.setp_lineEdit.setObjectName("setp_lineEdit")
        self.setp_lineEdit.setText(str(0.2))
        self.rang_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rang_lineEdit.setGeometry(QtCore.QRect(220, 50, 71, 31))
        self.rang_lineEdit.setObjectName("rang_lineEdit")
        self.rang_lineEdit.setText(str(3))



        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 120, 250, 200))
        self.textBrowser.setObjectName("textBrowser")

        self.plot_curve = QtWidgets.QGroupBox(self.centralwidget)
        self.plot_curve.setGeometry(QtCore.QRect(400, 400, 550, 400))
        self.plot_curve.setObjectName("groupBox")
        self.gridlayout2 = QGridLayout(self.plot_curve)
        self.plot_plt = pg.PlotWidget()  # 实例化一个绘图部件
        self.plot_plt.showGrid(x=True, y=True)  # 显示图形网格
        self.gridlayout2.addWidget(self.plot_plt)
        self.plot_plt.setYRange(max=0.9, min=0)
        self.plot_plt.setXRange(max=0, min=150)




        self.graphicsView_1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_1.setGeometry(QtCore.QRect(400, 70, 300, 300))
        self.graphicsView_1.setObjectName("graphicsView_1")

        self.step_label = QtWidgets.QLabel(self.centralwidget)
        self.step_label.setGeometry(QtCore.QRect(140, 30, 72, 15))
        self.step_label.setObjectName("step_label")
        self.rang_label = QtWidgets.QLabel(self.centralwidget)
        self.rang_label.setGeometry(QtCore.QRect(230, 30, 72, 15))
        self.rang_label.setObjectName("rang_label")

        self.Plot_static = QtWidgets.QGroupBox(self.centralwidget)
        self.Plot_static.setGeometry(QtCore.QRect(10, 400, 350, 350))
        self.Plot_static.setObjectName("groupBox")
        self.fig1 = Figure_Canvas(width=10, height=10, dpi=200)
        #self.fig1.compute_initial_figure(Zs,zfocus_wdi,zrange,I_LR,I_DU)
        #QGridLayout.removeWidget(self.Plot_static)
        self.gridlayout1 = QGridLayout(self.Plot_static)
        self.gridlayout1.addWidget(self.fig1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.start_pushButton.clicked.connect(self.timer_start)
        self.end_pushButton.clicked.connect(self.timer_stop)
        self.data_list=[]
        global C
        C=bost_UI.C

    def timer_start(self):
        D=self.tiaoping_init()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(lambda :self.tiaoping(C))
        self.timer.start(1000)

    def timer_stop(self):
        self.timer.stop()


    # 获取CPU使用率
    def get_fv(self,fv):
        try:
            if len(self.data_list)>120:
                self.data_list=[]
                self.plot_plt.clear()
            #cpu = "%0.2f" % psutil.cpu_percent(interval=1)
            self.data_list.append(float(fv))
            #print(float(fv))
            self.plot_plt.plot().setData(self.data_list, pen='g')
        except Exception as e:
            print(traceback.print_exc())

    def show_image(self,image,graphicsView_n):

        min_16bit = np.min(image)
        max_16bit = np.max(image)
        x = image.shape[1]  # 获取图像大小
        y = image.shape[0]
        # image_8bit = np.array(np.rint((255.0 * (image_16bit - min_16bit)) / float(max_16bit - min_16bit)), dtype=np.uint8)
        # 或者下面一种写法
        image_8bit = np.array(np.rint(255 * ((image - min_16bit) / (max_16bit - min_16bit))), dtype=np.uint8)
        frame = QImage(image_8bit, x, y, QImage.Format_Grayscale8)
        self.pix = QPixmap.fromImage(frame)
        #graphicsView_n=self.graphicsView_1
        self.item = QGraphicsPixmapItem(self.pix)  # 创建像素图元
        self.item.setScale(1.4)
        self.item.setFlags(QGraphicsPixmapItem.ItemIsFocusable |
                           QGraphicsPixmapItem.ItemIsMovable)
        # self.fitInView(QRectF(self.item.pos(), QSizeF(self.pix.size())), Qt.KeepAspectRatio)
        # self.item.update()
        graphicsView_n.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing |
                                         QPainter.SmoothPixmapTransform)
        graphicsView_n.setViewportUpdateMode(graphicsView_n.SmartViewportUpdate)
        self.scene = QGraphicsScene()  # 创建场景s
        self.scene.addItem(self.item)
        graphicsView_n.setScene(self.scene)




    def tiaoping_init(self):


        localtime0 = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        move_localfolder = com.setOutputFolder('output\BOST_FOR_tiaoping\\' + localtime0)
        file = os.path.join(move_localfolder, 'tiaoping.txt')
        f = open(file, 'w')
        #C = DDS.NSDS()
        Xoffset = 3.0
        Yoffset = 1.0
        x = Xoffset + 17.98 / 2   # x方向调节距离[-9,9],step>0.67
        y = Yoffset + 48.6 / 2  # y方向调节距离[-24,24],step>0.67
        C.sendandrecv({"CCP": "WDI AUTOFOCUSCONTROL 0 TIMEOUT 1000"})  # WDI
        C.sendandrecv({"CCP": "SERVO01 MOV 0 %.2f 0" % (x)})
        C.sendandrecv({"CCP": "SERVO02 MOV 0 %.2f 0" % (y)})
        localtime0 = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        move_localfolder = com.setOutputFolder('output\BOST_FOR_tiaoping/' + localtime0)
        file = os.path.join(move_localfolder, 'tiaoping.txt')
        # f = open(file, 'w')
        #return C

        C.sendandrecv({"msgID": 1, "CCP": "LED_G SET 1 %.3f" % 0.3})
        C.sendandrecv({"CCP": "CAM SET 2 %.3f" % 0.002})

    def tiaoping(self,C):
        C.sendandrecv({"CCP": "LED_G OPEN"})
        C.sendandrecv({"CCP": "WDI AUTOFOCUSCONTROL 1 TIMEOUT 1000"})
        zData = C.sendandrecv({"CCP": "WDI GET 5 TIMEOUT 1000"})
        zfocus_wdi = zData[b'data'][0]
        expTime = 0.02

        #output_img = os.path.join(move_localfolder, 'WDI_focus.tiff')
        C.sendandrecv({"CCP": "WDI_CAPTURER TRIGGERPHOTO 0 0 0"})
        data = C.sendandrecv({"CCP": "CAM GETIMAGE"})
        wdi_img = com.data2image(data)
        self.show_image(wdi_img[924:1124, 924:1124], self.graphicsView_1)
        C.sendandrecv({"CCP": "WDI AUTOFOCUSCONTROL 0 TIMEOUT 1000"})
        zrange = float(self.rang_lineEdit.text())
        step = float(self.setp_lineEdit.text())
        a = zfocus_wdi - zrange
        b = zfocus_wdi + zrange
        z_sanlist = np.arange(a, b, step)

        zscan_fv_mid_np = []

        fvs = np.zeros((len(z_sanlist), 16, 16))
        count=0
        for z in z_sanlist:
            C.sendandrecv({"CCP": "WDI SET 4 %f TIMEOUT 1000" % z})
            # C.sendandrecv({"CCP": "WDI_CAPTURER TRIGGERPHOTO 0 0 0"})
            # data = C.sendandrecv({"CCP": "CAM GETIMAGE"})
            # zscan_img = com.data2image(data)
            # cv2.imwrite(output_img, zscan_img)

            data = C.sendandrecv({"CCP": "WDI_CAPTURER TRIGGERPHOTO 0 0 0"})
            data = C.sendandrecv({"CCP": "CAM GETIMAGE"})
            zscan_img = com.data2image(data)

            for j in range(16):
                for k in range(16):
                    subimg = zscan_img[j * 128:j * 128 + 128, k * 128:k * 128 + 128]
                    fv = calculation_module.SML(subimg)
                    fvs[count, j, k] = fv
            center_fv = fvs[count, 7, 8]
            count = count + 1
            #center_fv=cpu = "%0.2f" % psutil.cpu_percent(interval=1)
            self.get_fv(center_fv)

        Zs = np.zeros((16, 16))
        for j in range(16):
            for k in range(16):
                fv_z = fvs[:, j, k]
                idx = np.where(fv_z == np.amax(fv_z))
                Zs[j, k] = z_sanlist[idx]
        C.sendandrecv({"CCP": "LED_G CLOSE"})
        dataz = Zs - zfocus_wdi
        #self.fig1.mat_plot_drow(dataz, zrange)
        # f.write(
        #    'Delta_z_upleft=%.2f\tDelta_z_midup=%.2f \tDelta_z_upright=%.2f \nDelta_z_midleft=%.2f\tDelta_z_mid=%.2f \tDelta_z_midright=%.2f \n'
        #    'Delta_z_downleft = % .2f\tDelta_z_middown=%.2f \tDelta_z_downright=%.2f \n' % (
        #    Delta_z_upleft, Delta_z_midup, Delta_z_upright,
        #    Delta_z_midleft, Delta_z_mid, Delta_z_midright, Delta_z_downleft, Delta_z_middown, Delta_z_downright))

        # f.close()

        #
        I_left = Zs[range(2, 15), 0]
        I_right = Zs[15, range(2, 15)]
        I_up = Zs[0, range(2, 15)]
        I_down = Zs[15, range(2, 15)]
        I_DU = -np.mean(I_left) + np.mean(I_right)
        I_LR = -np.mean(I_down) + np.mean(I_up)
        line = ('Zpv=%.3f, Zmax=%.3f, Zmin=%.3f\nLeft-Right: %.2fum    Down-Up: %.2fum' % (
        np.amax(Zs) - np.amin(Zs), np.amax(Zs), np.amin(Zs), I_LR, I_DU))
        self.textBrowser.setText(line)
        C.sendandrecv({"CCP": "LED_G CLOSE"})
        #folder = os.path.join(move_localfolder, 'tiaoping_%4d.png')
        self.fig1.mat_plot_drow( dataz, zrange, Zs, I_LR, I_DU)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_pushButton.setText(_translate("MainWindow", "开始"))
        self.end_pushButton.setText(_translate("MainWindow", "结束"))
        self.step_label.setText(_translate("MainWindow", "步长"))
        self.rang_label.setText(_translate("MainWindow", "范围"))
        self.Plot_static.setTitle(_translate("Dialog", "GroupBox_Matplotlib的图形显示："))