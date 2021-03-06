#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 9:51
# @Author  : 柠檬菠萝
# @Email   : yzpmihome@vip.qq.com
# @File    : Module-Test.py

import _thread
import os

class RunModule:
    def __init__(self, tmp_dict):
        self.log = tmp_dict.get("log")
        pass

    def _log(self,threadName):
        print(os.getpid())
        print(self.log)
        print(threadName)

    def run(self):
        _thread.start_new_thread(self._log,("Thread-1",))

    def update(self):
        self.run()
        return self.log
        pass