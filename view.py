from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys, os
from datetime import date
import interm
import queue
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from pprint import pprint
import datetime 
import threading
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QTableWidget,
                               QTableWidgetItem)
import config
import time

class Main(Ui_MainWindow):

    def __init__(self, MainWindow):
        """MainWindow constructor"""
        super().setupUi(MainWindow) 
        ## show weather data
        self.pushButton_enter.clicked.connect(self.start_thread)
        ## download weather data
        self.pushButton_export.clicked.connect(self.write_weather)
        ## Cancel Showing data
        self.pushButton_cancel.clicked.connect(self.stop_downloading)
        #### try
        self.progressBar.setValue(0)

        self.tableWidget_data.show()

    def stop_downloading(self):
        config.cancel = True
        config.p_bar = 0
        config.n_days = 1
        self.populate_table()
        self.tableWidget_data.clear()
        self.dateEdit_from.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit_to.setDate(QtCore.QDate(2000, 1, 1))

    def populate_table(self):
        # self.tableWidget_data.clear()
        # self.dateEdit_from.setDate(QtCore.QDate(2020, 1, 1))
        # self.dateEdit_to.setDate(QtCore.QDate(2020, 1, 1))
        self.tableWidget_data.setRowCount(0)
        self.progressBar.setValue(0)
        config.p_bar = 0


    # def populate_form(self):
    #     pass

    def read_weather(self):

        config.cancel = False
        # global d

        # w_data = queue.Queue()
        city = self.comboBox_city.currentText()
        start_date = self.dateEdit_from.date()
        end_date = self.dateEdit_to.date()
        # (w_data) = interm.read_weather(city, start_date.toString('yyyy-MM-d'), end_date.toString('yyyy-MM-d'))
        interm.read_weather(city, start_date.toString('yyyy-MM-d'), end_date.toString('yyyy-MM-d'))
        # config.w_data
        # self.timer.timeout.connect(self.progressbar)
        # self.timer.start(100)

        # self.populate_table()
        # self.show_data(w_data)

        # self.timer.timeout.connect(self.progressbar)
        # self.timer.start(1000)
        # self.timer.stop()
        

    def write_weather(self):
        interm.write_weather()
        # print("test1")
        # self.timer = QtCore.QTimer()
        # self.timer.setInterval(10)
        # print("test2")
        # self.timer.timeout.connect(interm.writ e_weather)
        # self.timer.timeout.connect(self.progressbar)
        # self.timer.start(1000)
        # self.progressbar()
        # self.timer.stop()



    def progressbar(self):
        # self.progressBar.setValue(0)
        # self.progressBar.setMinimum(0)
        # self.progressBar.setMaximum(100)
        total_items = 100
        p = (config.p_bar*100)/config.n_days
        self.progressBar.setValue(p)
        print("config.p_bar")
        print(config.p_bar)
        print("config.n_days")
        print(config.n_days)
        ##### could be controlled by var within config
        if config.p_bar == config.n_days:
            self.timer.stop()

        

    def show_data(self):
        # data_q = list(w_data)
        t_day = config.n_days
        # print(data_q.get())
        print("show_data function is running")
        self.tableWidget_data.setRowCount(t_day)
        self.tableWidget_data.setColumnCount(4)
        self.tableWidget_data.setHorizontalHeaderLabels(["temperature", "humidity", "precip", "wind"])

        
        for i in range(t_day):
            # config.p_bar = 0
            # config.p_bar += 1
            # print(config.p_bar)
            flag = 0
            flagt = 0
            
            if config.cancel:
                self.populate_table()
            # print("Download Cancelled")
            # populate form will be called
                break 
            if config.w_data.empty():
                break
            else:
                if not config.w_data.empty():

                    data = config.w_data.get()
                    config.p_bar += 1
                    flagt += 1
                    

                    temperature = data["temperature"]
                    humidity = data["humidity"]
                    precip = data["precip"]
                    wind = data["wind"]
                    item_t = QTableWidgetItem(temperature)
                    item_h = QTableWidgetItem(humidity)
                    item_p = QTableWidgetItem(precip)
                    item_w = QTableWidgetItem(wind)
                    self.tableWidget_data.setItem(config.j, 0, item_t)
                    self.tableWidget_data.setItem(config.j, 1, item_h)
                    self.tableWidget_data.setItem(config.j, 2, item_p)
                    self.tableWidget_data.setItem(config.j, 3, item_w)
                    # QApplication.processEvents()
                    config.j += 1
                    self.tableWidget_data.resizeColumnToContents(0)
                    self.tableWidget_data.resizeColumnToContents(3)


                    if  config.w_data.empty():
                        flag = 1

                if flagt % 2 == 0:
                    break

                else:
                    break
        if flag == 1:
            config.j = 0
            self.timer.stop()                
        # self.tableWidget_data.repaint()

    def start_thread(self):
        self.populate_table()
        self.day_cal()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progressbar)
        self.timer.start(1000)
        self.timer.timeout.connect(self.show_data)
        self.timer.start(100)
        read_w_thread = threading.Thread(target=self.read_weather,daemon=True, args=[])
        # self.populate_table()
        read_w_thread.start()

    def day_cal(self):
        start_date = self.dateEdit_from.date()
        end_date = self.dateEdit_to.date() 
        s_date = start_date.toString('yyyy-MM-d')
        e_date = end_date.toString('yyyy-MM-d')
        date1 = datetime.strptime(e_date, '%Y-%m-%d')
        date2 = datetime.strptime(s_date, '%Y-%m-%d')
        time_difference = date1 - date2
        number_of_days = time_difference.days
        config.n_days = number_of_days + 1        

    # def stop_thread(self):
    #     self.read_w_thread.downloading = False
    #     print("downloading cancel")

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()

    ui = Main(MainWindow)

    MainWindow.show()

    sys.exit(app.exec())