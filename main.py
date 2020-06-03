# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication

from mainwindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('Aqua.qss', 'r') as f:
        app.setStyleSheet(f.read())
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
