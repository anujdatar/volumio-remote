#include "mainwindow.h"
#include <QApplication>

#include <QtWebEngine/qtwebengineglobal.h>

int main(int argc, char *argv[])
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    QApplication a(argc, argv);

    QtWebEngine::initialize();

    MainWindow w;
    w.show();

    return a.exec();
}
