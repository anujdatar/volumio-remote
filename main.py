# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QUrl
from source import MainWindow


if __name__ == '__main__':
    url = 'http://volumio.local/'

    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    browser = MainWindow()
    browser.page.load(QUrl(url))

    sys.exit(app.exec_())
