# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JanelaPrincipal(object):
    def setupUi(self, JanelaPrincipal):
        JanelaPrincipal.setObjectName("JanelaPrincipal")
        JanelaPrincipal.resize(393, 369)
        self.centralWidget = QtWidgets.QWidget(JanelaPrincipal)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.checkCapa = QtWidgets.QCheckBox(self.centralWidget)
        self.checkCapa.setObjectName("checkCapa")
        self.gridLayout.addWidget(self.checkCapa, 3, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 6, 0, 1, 4)
        self.labelSalvar = QtWidgets.QLabel(self.centralWidget)
        self.labelSalvar.setObjectName("labelSalvar")
        self.gridLayout.addWidget(self.labelSalvar, 2, 0, 1, 1)
        self.lineSalvar = QtWidgets.QLineEdit(self.centralWidget)
        self.lineSalvar.setObjectName("lineSalvar")
        self.gridLayout.addWidget(self.lineSalvar, 2, 1, 1, 2)
        self.lineArquivo = QtWidgets.QLineEdit(self.centralWidget)
        self.lineArquivo.setObjectName("lineArquivo")
        self.gridLayout.addWidget(self.lineArquivo, 0, 1, 1, 2)
        self.buttonAbrirArquivo = QtWidgets.QPushButton(self.centralWidget)
        self.buttonAbrirArquivo.setObjectName("buttonAbrirArquivo")
        self.gridLayout.addWidget(self.buttonAbrirArquivo, 0, 3, 1, 1)
        self.buttonAbrirSalvar = QtWidgets.QPushButton(self.centralWidget)
        self.buttonAbrirSalvar.setObjectName("buttonAbrirSalvar")
        self.gridLayout.addWidget(self.buttonAbrirSalvar, 2, 3, 1, 1)
        self.labelArquivo = QtWidgets.QLabel(self.centralWidget)
        self.labelArquivo.setObjectName("labelArquivo")
        self.gridLayout.addWidget(self.labelArquivo, 0, 0, 1, 1)
        self.buttonConverter = QtWidgets.QPushButton(self.centralWidget)
        self.buttonConverter.setObjectName("buttonConverter")
        self.gridLayout.addWidget(self.buttonConverter, 4, 1, 1, 2)
        self.checkExcluir = QtWidgets.QCheckBox(self.centralWidget)
        self.checkExcluir.setObjectName("checkExcluir")
        self.gridLayout.addWidget(self.checkExcluir, 3, 2, 1, 1)
        JanelaPrincipal.setCentralWidget(self.centralWidget)

        self.retranslateUi(JanelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(JanelaPrincipal)

    def retranslateUi(self, JanelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        JanelaPrincipal.setWindowTitle(_translate("JanelaPrincipal", "SlicePDF"))
        self.checkCapa.setText(_translate("JanelaPrincipal", "Capa"))
        self.labelSalvar.setText(_translate("JanelaPrincipal", "   Salvar em:"))
        self.buttonAbrirArquivo.setText(_translate("JanelaPrincipal", "Abrir"))
        self.buttonAbrirSalvar.setText(_translate("JanelaPrincipal", "Abrir"))
        self.labelArquivo.setText(_translate("JanelaPrincipal", "   Arquivo:"))
        self.buttonConverter.setText(_translate("JanelaPrincipal", "Converter"))
        self.checkExcluir.setText(_translate("JanelaPrincipal", "Excluir arquivo original"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JanelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_JanelaPrincipal()
    ui.setupUi(JanelaPrincipal)
    JanelaPrincipal.show()
    sys.exit(app.exec_())
