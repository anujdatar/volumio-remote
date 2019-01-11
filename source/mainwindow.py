# coding=utf-8

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile


class MainWindow(QMainWindow):

    def __init__(self, width=1280, height=720):
        super().__init__()
        self.setWindowTitle('Volumio Remote Control')
        self.logo = QIcon('./images/logo.png')
        self.setWindowIcon(self.logo)
        self.setGeometry(50, 50, width, height)

        self.page = BrowserWindow()
        self.setCentralWidget(self.page)

        self.page.loadStarted.connect(self.load_started_handler)
        self.page.loadFinished.connect(self.load_finished_handler)

        self.show()

    def load_started_handler(self):
        self.statusBar().showMessage('Loading...')

    def load_finished_handler(self):
        self.statusBar().showMessage('Welcome')


class BrowserWindow(QWebEngineView):
    def __init__(self):
        super().__init__()


class BrowserPage(QWebEnginePage):
    def __init__(self):
        super().__init__()


