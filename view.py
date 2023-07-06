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
from PyQt5.QtWidgets import (QApplication, QTableWidget,
                               QTableWidgetItem)
import config

class Main(Ui_MainWindow):

    def __init__(self, MainWindow):
        """MainWindow constructor"""
        super().setupUi(MainWindow) 
        ## show weather data
        self.pushButton_enter.clicked.connect(self.start_thread)
        ## Cancel Showing data
        # self.pushButton_cancel.clicked.connect(self.stop_thread)
        ## download weather data
        self.pushButton_export.clicked.connect(self.write_weather)

        self.pushButton_cancel.clicked.connect(self.stop_downloading)

    def stop_downloading(self):
        config.cancel = True

    def populate_table(self):
        # self.tableWidget_data.clear()
        self.dateEdit_from.setDate(QtCore.QDate(2020, 1, 1))
        self.dateEdit_to.setDate(QtCore.QDate(2020, 1, 1))

    def populate_form(self):
        pass

    def read_weather(self):
        config.cancel = False

        w_data = queue.Queue()
        city = self.comboBox_city.currentText()
        start_date = self.dateEdit_from.date()
        end_date = self.dateEdit_to.date()
        (w_data, d ) = interm.read_weather(city, start_date.toString('yyyy-MM-d'), end_date.toString('yyyy-MM-d'))
        # (temp, humidity, precip, wind) = interm.read_weather(city, start_date.toString('yyyy-MM-d'), end_date.toString('yyyy-MM-d'))

        # self.populate_table()
        self.show_data(w_data, d)


    def write_weather(self):
        interm.write_weather()

    ###### test qtable widget
    # def show_data(self):
    #     c_data = [("Red", "FF0000"),
    #               ("Green", "00FF00"),
    #               ("Blue", "0000FF"),
    #               ("Black", "000000"),
    #               ("White", "FFFFFF"),
    #               ("Yellow", "00FF00"),
    #               ("Green", "F9E56d"),
    #               ]
    #     print("test1")
    #     table = self.tableWidget_data
    #     table.setRowCount(len(c_data))
    #     table.setColumnCount(len(c_data[0])+ 1)
    #     table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])
    #     for i, (name, code) in enumerate(c_data):
    #         item_name = QTableWidgetItem(name)
    #         item_code = QTableWidgetItem(code)

    #         table.setItem(i, 0, item_name)
    #         table.setItem(i, 1, item_code)
    def show_data(self,w_data, d):
        # data_q = list(w_data)
        t_day = d
        # print(data_q.get())
        table = self.tableWidget_data
        table.setRowCount(t_day)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["temperature", "humidity", "precip", "wind"])

        # for i, (temperature, humidity, precip, wind) in enumerate(data_q):
        #     item_t = QTableWidgetItem(temperature)
        #     item_h = QTableWidgetItem(humidity)
        #     item_p = QTableWidgetItem(precip)
        #     item_w = QTableWidgetItem(wind)

        #     table.setItem(i, 0, item_t)
        #     table.setItem(i, 1, item_h)
        #     table.setItem(i, 2, item_p)
        #     table.setItem(i, 3, item_w)

        for i in range(t_day):
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
        read_w_thread = threading.Thread(target=self.read_weather,daemon=True, args=[])

        read_w_thread.start()


    # def stop_thread(self):
    #     self.read_w_thread.downloading = False
    #     print("downloading cancel")

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()

    ui = Main(MainWindow)

    MainWindow.show()

    sys.exit(app.exec())