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

    def stop_downloading(self):
        config.cancel = True

    def populate_table(self):
        # self.tableWidget_data.clear()
        # self.dateEdit_from.setDate(QtCore.QDate(2020, 1, 1))
        # self.dateEdit_to.setDate(QtCore.QDate(2020, 1, 1))
        table = self.tableWidget_data
        table.setRowCount(0)


    # def populate_form(self):
    #     pass

    def read_weather(self):

        config.cancel = False
        global d

        w_data = queue.Queue()
        city = self.comboBox_city.currentText()
        start_date = self.dateEdit_from.date()
        end_date = self.dateEdit_to.date()
        (w_data, d ) = interm.read_weather(city, start_date.toString('yyyy-MM-d'), end_date.toString('yyyy-MM-d'))
        print("test")
        # self.timer.timeout.connect(self.progressbar)
        # self.timer.start(100)
        print("test1")
        # self.populate_table()
        self.show_data(w_data, d)
        print("test2")
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
        time.sleep(10)
        print("test3")
        total_items = 100
        p = (config.p_bar*100)/n_days
        self.progressBar.setValue(p)
        print("config.p_bar")
        print(config.p_bar)
        print("n_days")
        print(n_days)
        if config.p_bar == n_days:
            self.timer.stop()

        

    def show_data(self,w_data, d):
        # data_q = list(w_data)
        t_day = d
        # print(data_q.get())
        table = self.tableWidget_data
        table.setRowCount(t_day)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["temperature", "humidity", "precip", "wind"])

   
        for i in range(t_day):
            config.p_bar += 1
            print(config.p_bar)
            if config.cancel:
                self.populate_table()
            # print("Download Cancelled")
            # populate form will be called
                break 
            else:
                if not w_data.empty():
                    data = w_data.get()
                    temperature = data["temperature"]
                    humidity = data["humidity"]
                    precip = data["precip"]
                    wind = data["wind"]
                    item_t = QTableWidgetItem(temperature)
                    item_h = QTableWidgetItem(humidity)
                    item_p = QTableWidgetItem(precip)
                    item_w = QTableWidgetItem(wind)

                    table.setItem(i, 0, item_t)
                    table.setItem(i, 1, item_h)
                    table.setItem(i, 2, item_p)
                    table.setItem(i, 3, item_w)

                else:
                    break

    def start_thread(self):
        self.populate_table()
        self.day_cal()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progressbar)
        self.timer.start(10)
        read_w_thread = threading.Thread(target=self.read_weather,daemon=True, args=[])

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
        global n_days
        n_days = number_of_days + 1        

    # def stop_thread(self):
    #     self.read_w_thread.downloading = False
    #     print("downloading cancel")

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()

    ui = Main(MainWindow)

    MainWindow.show()

    sys.exit(app.exec())