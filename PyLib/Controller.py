#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 9:41
# @Author  : 柠檬菠萝
# @Email   : yzpmihome@vip.qq.com
# @File    : Controller.py
from PyQt5.QtCore import pyqtSlot, QModelIndex, QMutex
from PyQt5.QtWidgets import QMainWindow
from PyLib.MainUi import Ui_Dialog
from PyLib.ProgramManagement import runCmd


class MainWin(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.q = QMutex()

    #@pyqtSlot(QModelIndex)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.q.lock()
        self.runCmd_ = runCmd(name="Module-Test", log=str("TEST LOG PRINT"))
        self.runCmd_.cmdsign.connect(self._lookTestsLog)
        self.runCmd_.start()
        self.runCmd_.wait()
        self.q.unlock()
    def _lookTestsLog(self, log):
        self.label.setText(log)


