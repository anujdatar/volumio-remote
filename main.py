# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QUrl
from source import MainWindow
# from PyQt5.QtWebEngineWidgets import QWebEngineView


if __name__ == '__main__':
    # url = 'https://www.google.com'
    # url = 'https://web.whatsapp.com'
    url = 'http://volumio.local/'

    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    # ex = MainWindow()

    browser = MainWindow()
    browser.page.load(QUrl(url))

    sys.exit(app.exec_())
