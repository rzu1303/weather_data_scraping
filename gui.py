# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(270, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 150, 781, 441))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget_data = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidget_data.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"alternate-background-color: rgb(204, 204, 204);")
        self.tableWidget_data.setObjectName("tableWidget_data")
        self.tableWidget_data.setColumnCount(4)
        self.tableWidget_data.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.tableWidget_data)
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.pushButton_export = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_export.sizePolicy().hasHeightForWidth())
        self.pushButton_export.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_export.setFont(font)
        self.pushButton_export.setAutoRepeatDelay(300)
        self.pushButton_export.setObjectName("pushButton_export")
        self.verticalLayout_3.addWidget(self.pushButton_export, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 781, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_date_from = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date_from.sizePolicy().hasHeightForWidth())
        self.label_date_from.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_date_from.setFont(font)
        self.label_date_from.setObjectName("label_date_from")
        self.horizontalLayout_2.addWidget(self.label_date_from)
        self.dateEdit_from = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_from.setFont(font)
        self.dateEdit_from.setObjectName("dateEdit_from")
        self.horizontalLayout_2.addWidget(self.dateEdit_from)
        self.label_date_to = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date_to.sizePolicy().hasHeightForWidth())
        self.label_date_to.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_date_to.setFont(font)
        self.label_date_to.setObjectName("label_date_to")
        self.horizontalLayout_2.addWidget(self.label_date_to)
        self.dateEdit_to = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_to.setFont(font)
        self.dateEdit_to.setObjectName("dateEdit_to")
        self.horizontalLayout_2.addWidget(self.dateEdit_to)
        self.label_city = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_city.sizePolicy().hasHeightForWidth())
        self.label_city.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_city.setFont(font)
        self.label_city.setObjectName("label_city")
        self.horizontalLayout_2.addWidget(self.label_city)
        self.comboBox_city = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_city.setFont(font)
        self.comboBox_city.setObjectName("comboBox_city")
        self.comboBox_city.addItem("")
        self.comboBox_city.addItem("")
        self.comboBox_city.addItem("")
        self.comboBox_city.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_city)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_enter = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_enter.sizePolicy().hasHeightForWidth())
        self.label_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_enter.setFont(font)
        self.label_enter.setObjectName("label_enter")
        self.horizontalLayout_3.addWidget(self.label_enter)
        self.pushButton_enter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_enter.sizePolicy().hasHeightForWidth())
        self.pushButton_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_enter.setFont(font)
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.horizontalLayout_3.addWidget(self.pushButton_enter)
        self.label_cancel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cancel.sizePolicy().hasHeightForWidth())
        self.label_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cancel.setFont(font)
        self.label_cancel.setObjectName("label_cancel")
        self.horizontalLayout_3.addWidget(self.label_cancel)
        self.pushButton_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.label.setText(_translate("MainWindow", "Weather Scraping Project"))
        item = self.tableWidget_data.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.tableWidget_data.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Humidity"))
        item = self.tableWidget_data.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Precipitation"))
        item = self.tableWidget_data.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Wind"))
        self.pushButton_export.setText(_translate("MainWindow", "EXPORT DATA"))
        self.label_date_from.setText(_translate("MainWindow", "Date from:"))
        self.label_date_to.setText(_translate("MainWindow", "Date to:"))
        self.label_city.setText(_translate("MainWindow", "City:"))
        self.comboBox_city.setItemText(0, _translate("MainWindow", "Dhaka"))
        self.comboBox_city.setItemText(1, _translate("MainWindow", "New york"))
        self.comboBox_city.setItemText(2, _translate("MainWindow", "Singapore"))
        self.comboBox_city.setItemText(3, _translate("MainWindow", "Dubai"))
        self.label_enter.setText(_translate("MainWindow", "Press \'ENTER\' to see data"))
        self.pushButton_enter.setText(_translate("MainWindow", "ENTER"))
        self.label_cancel.setText(_translate("MainWindow", "Press \'CANCEL\' to stop process"))
        self.pushButton_cancel.setText(_translate("MainWindow", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
