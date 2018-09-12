import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from slicepdf import SlicePDF
import design


class SlicePDFApp(QtWidgets.QMainWindow, design.Ui_JanelaPrincipal):
    def __init__(self, parent=None):
        super(SlicePDFApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img/logo.ico'))
        self.buttonAbrirArquivo.clicked.connect(self.abrir_arquivo)
        self.buttonAbrirSalvar.clicked.connect(self.abrir_diretorio)
        self.buttonConverter.clicked.connect(self.converter)

    def abrir_arquivo(self):
        options = QtWidgets.QFileDialog.Options()
        arquivo = QtWidgets.QFileDialog.getOpenFileName(self,
                                                        "Abrir arquivo",
                                                        "",
                                                        "Arquivos PDF (*.pdf)",
                                                        options=options)
        self.lineArquivo.setText(arquivo[0])

    def abrir_diretorio(self):
        options = QtWidgets.QFileDialog.Options()
        diretorio = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Salvar em:")
        self.lineSalvar.setText(diretorio)

    def converter(self):
        conversao = SlicePDF(self.lineArquivo.text(),
                             self.lineSalvar.text(),
                             self.checkCapa.isChecked(),
                             self.checkExcluir.isChecked()
                             )
        self.detalhes_thread = Detalhes(conversao.detalhes,
                                        self.listWidget)
        self.detalhes_thread.start()
        self.conversao_thread = Conversao(conversao)
        self.conversao_thread.start()


class Conversao(QtCore.QThread):
    def __init__(self, obj_conv, parent=None):
        super(Conversao, self).__init__(parent)
        self.conversao = obj_conv

    def run(self):
        self.conversao.abrir_arquivo()
        self.conversao.converter()
        self.conversao.fatiar()
        self.conversao.gera_pdf()


class Detalhes(QtCore.QThread):
    def __init__(self, lista, obj_list, parent=None):
        super(Detalhes, self).__init__(parent)
        self.lista_detalhes = lista
        self.list = obj_list

    def run(self):
        n = len(self.lista_detalhes)
        self.list.clear()
        while True:
            if len(self.lista_detalhes) > n:
                self.list.addItem(self.lista_detalhes[-1])
                self.list.show()
                self.list.scrollToBottom()
                n = len(self.lista_detalhes)
            elif self.lista_detalhes[-1] == "Fim.":
                break
            else:
                continue


app = QtWidgets.QApplication(sys.argv)
form = SlicePDFApp()
form.show()
app.exec_()
