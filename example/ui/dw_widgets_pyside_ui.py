# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dw_widgets.ui'
#
# Created: Fri Nov  9 18:42:56 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(269, 306)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_81 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.gridLayout.addWidget(self.label_81, 0, 1, 1, 1)
        self.label_82 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.gridLayout.addWidget(self.label_82, 0, 2, 1, 1)
        self.label_56 = QtGui.QLabel(self.dockWidgetContents)
        self.label_56.setMinimumSize(QtCore.QSize(0, 0))
        self.label_56.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.gridLayout.addWidget(self.label_56, 1, 0, 1, 1)
        self.listWidget = QtGui.QListWidget(self.dockWidgetContents)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setObjectName("listWidget")
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)
        self.listWidgetDis = QtGui.QListWidget(self.dockWidgetContents)
        self.listWidgetDis.setEnabled(False)
        self.listWidgetDis.setObjectName("listWidgetDis")
        QtGui.QListWidgetItem(self.listWidgetDis)
        QtGui.QListWidgetItem(self.listWidgetDis)
        QtGui.QListWidgetItem(self.listWidgetDis)
        QtGui.QListWidgetItem(self.listWidgetDis)
        self.gridLayout.addWidget(self.listWidgetDis, 1, 2, 1, 1)
        self.label_57 = QtGui.QLabel(self.dockWidgetContents)
        self.label_57.setMinimumSize(QtCore.QSize(0, 0))
        self.label_57.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.gridLayout.addWidget(self.label_57, 2, 0, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(self.dockWidgetContents)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.gridLayout.addWidget(self.treeWidget, 2, 1, 1, 1)
        self.treeWidgetDis = QtGui.QTreeWidget(self.dockWidgetContents)
        self.treeWidgetDis.setEnabled(False)
        self.treeWidgetDis.setObjectName("treeWidgetDis")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidgetDis)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidgetDis)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.gridLayout.addWidget(self.treeWidgetDis, 2, 2, 1, 1)
        self.label_58 = QtGui.QLabel(self.dockWidgetContents)
        self.label_58.setMinimumSize(QtCore.QSize(0, 0))
        self.label_58.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.gridLayout.addWidget(self.label_58, 3, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.dockWidgetContents)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 1, 1, 1)
        self.tableWidgetDis = QtGui.QTableWidget(self.dockWidgetContents)
        self.tableWidgetDis.setEnabled(False)
        self.tableWidgetDis.setObjectName("tableWidgetDis")
        self.tableWidgetDis.setColumnCount(2)
        self.tableWidgetDis.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDis.setItem(2, 1, item)
        self.gridLayout.addWidget(self.tableWidgetDis, 3, 2, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QtGui.QApplication.translate("DockWidget", "Widgets", None, QtGui.QApplication.UnicodeUTF8))
        self.label_81.setText(QtGui.QApplication.translate("DockWidget", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_82.setText(QtGui.QApplication.translate("DockWidget", "Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_56.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_56.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_56.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_56.setText(QtGui.QApplication.translate("DockWidget", "ListWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(1).setText(QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(2).setText(QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(3).setText(QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidgetDis.isSortingEnabled()
        self.listWidgetDis.setSortingEnabled(False)
        self.listWidgetDis.item(0).setText(QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetDis.item(1).setText(QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetDis.item(2).setText(QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetDis.item(3).setText(QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetDis.setSortingEnabled(__sortingEnabled)
        self.label_57.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_57.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_57.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_57.setText(QtGui.QApplication.translate("DockWidget", "TreeWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("DockWidget", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("DockWidget", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("DockWidget", "New Subitem", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).setText(1, QtGui.QApplication.translate("DockWidget", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, QtGui.QApplication.translate("DockWidget", "New Subitem", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("DockWidget", "New Subitem", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidgetDis.setSortingEnabled(True)
        self.treeWidgetDis.headerItem().setText(0, QtGui.QApplication.translate("DockWidget", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetDis.headerItem().setText(1, QtGui.QApplication.translate("DockWidget", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidgetDis.isSortingEnabled()
        self.treeWidgetDis.setSortingEnabled(False)
        self.treeWidgetDis.topLevelItem(0).setText(0, QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetDis.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("DockWidget", "New Subitem", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetDis.topLevelItem(0).child(0).setText(1, QtGui.QApplication.translate("DockWidget", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetDis.topLevelItem(0).child(0).child(0).setText(0, QtGui.QApplication.translate("DockWidget", "New Subitem", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetDis.topLevelItem(1).setText(0, QtGui.QApplication.translate("DockWidget", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetDis.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("DockWidget", "New Subitem", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetDis.setSortingEnabled(__sortingEnabled)
        self.label_58.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_58.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_58.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_58.setText(QtGui.QApplication.translate("DockWidget", "TableWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(0).setText(QtGui.QApplication.translate("DockWidget", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(1).setText(QtGui.QApplication.translate("DockWidget", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(2).setText(QtGui.QApplication.translate("DockWidget", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DockWidget", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DockWidget", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.item(0, 0).setText(QtGui.QApplication.translate("DockWidget", "1.23", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(0, 1).setText(QtGui.QApplication.translate("DockWidget", "Hello", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(1, 0).setText(QtGui.QApplication.translate("DockWidget", "1,45", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(1, 1).setText(QtGui.QApplication.translate("DockWidget", "Olá", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(2, 0).setText(QtGui.QApplication.translate("DockWidget", "12/12/2012", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.item(2, 1).setText(QtGui.QApplication.translate("DockWidget", "Oui", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidgetDis.verticalHeaderItem(0).setText(QtGui.QApplication.translate("DockWidget", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDis.verticalHeaderItem(1).setText(QtGui.QApplication.translate("DockWidget", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDis.verticalHeaderItem(2).setText(QtGui.QApplication.translate("DockWidget", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDis.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DockWidget", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDis.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DockWidget", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidgetDis.isSortingEnabled()
        self.tableWidgetDis.setSortingEnabled(False)
        self.tableWidgetDis.item(0, 0).setText(QtGui.QApplication.translate("DockWidget", "1.23", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDis.item(0, 1).setText(QtGui.QApplication.translate("DockWidget", "Hello", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDis.item(1, 0).setText(QtGui.QApplication.translate("DockWidget", "1,45", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDis.item(1, 1).setText(QtGui.QApplication.translate("DockWidget", "Olá", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDis.item(2, 0).setText(QtGui.QApplication.translate("DockWidget", "12/12/2012", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDis.item(2, 1).setText(QtGui.QApplication.translate("DockWidget", "Oui", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDis.setSortingEnabled(__sortingEnabled)

