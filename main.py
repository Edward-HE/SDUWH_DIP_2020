"""
Time    : 2020/12/9 上午12:24
Author  : Edward-du
Contact : duchenhe@outlook.com
Project : DIP
File    : main.py
Software: PyCharm
Desc    :
"""
import sys
from func_center import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    DIP_lab = QApplication(sys.argv)
    MainWin = DipLabFunc()
    MainWin.show()
    sys.exit(DIP_lab.exec_())
