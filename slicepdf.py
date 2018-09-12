import os
import sys
import time
from wand.image import Image
from wand.exceptions import BlobError
from fpdf import FPDF


class SlicePDF(object):
    def __init__(self, caminho_arquivo, caminho_salvar,
                 capa=False, excluir_arquivo=False):
        self.arquivo_pdf = caminho_arquivo[caminho_arquivo.rfind('/') + 1:]
        self.diretorio = caminho_arquivo[:caminho_arquivo.rfind('/') + 1]
        self.salvar = caminho_salvar
        self.lista_de_imagens = []
        self.capa = capa
        self.excluir_arquivo_original = excluir_arquivo
        self.path = ".slicePDF/"
        self.detalhes = ["Iniciando ..."]
        os.chdir(self.diretorio)

    def abrir_arquivo(self):
        time.sleep(3)
        self.detalhes.append("Abrindo arquivo ...")

        try:
            self.arquivo = Image(filename=self.arquivo_pdf)
            self.detalhes.append("Arquivo aberto com sucesso.\n")
            time.sleep(1)
        except BlobError:
            self.detalhes.append("Erro ao abrir o arquivo !!!")
            self.detalhes.append("Fim.")

    def converter(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        numero_de_paginas = len(self.arquivo.sequence)
        self.detalhes.append("Iniciando importação ...")

        try:
            for pagina in range(numero_de_paginas):
                nome_arquivo = "%s[%d]" % (self.arquivo_pdf, pagina)
                img = Image(filename=nome_arquivo, resolution=150)
                img.compression_quality = 99
                nome_arquivo = "pagina%d.jpg" % (pagina + 1)
                self.detalhes.append("\tPágina %d importada" % (pagina + 1))
                img.save(filename=self.path + nome_arquivo)
                self.lista_de_imagens.append(nome_arquivo)
                img.close()

            self.detalhes.append("Importação concluída.\n")
            time.sleep(1)
            self.arquivo.close()

        except BlobError:
            self.detalhes.append("Erro na importação!!!")
            time.sleep(1)
            self.detalhes.append("Fim.")
            self.arquivo.close()
            os.rmdir(self.path)

    def fatiar(self):
        os.chdir(self.path)
        nova_lista = []
        pagina = 1
        self.detalhes.append("Fatiamento iniciado")
        time.sleep(1)

        if self.capa:
            nova_lista.append("page0.jpg")
            os.rename("pagina1.jpg", "page0.jpg")
            self.detalhes.append("\tCapa criada")
            del self.lista_de_imagens[0]

        try:
            for imagem in self.lista_de_imagens:
                img = Image(filename=imagem)
                meia_pagina = int(img.size[0] / 2)

                with img[0:meia_pagina, 0:img.size[1]] as fatia:
                    fatia.save(filename="page%d.jpg" % pagina)
                    nova_lista.append("page%d.jpg" % pagina)
                    self.detalhes.append("\tPágina %d criada" % (pagina))
                    pagina += 1

                with img[meia_pagina:img.size[0], 0:img.size[1]] as fatia:
                    fatia.save(filename="page%d.jpg" % pagina)
                    nova_lista.append("page%d.jpg" % pagina)
                    self.detalhes.append("\tPágina %d criada" % (pagina))
                    pagina += 1

                img.close()
                os.remove(imagem)

        except BlobError:
            self.detalhes.append("Erro na importação !!!")
            time.sleep(1)
            self.detalhes.append("Fim.")
            img.close()
            os.rmdir(self.path)

        self.detalhes.append("Fatiamento concluído.\n")
        time.sleep(1)

        self.lista_de_imagens = nova_lista

    def gera_pdf(self):
        pdf = FPDF()
        paginas = 1
        self.detalhes.append("Criando novo arquivo PDF")

        try:
            for imagem in self.lista_de_imagens:
                pdf.add_page()
                pdf.image(imagem, 0, 0, pdf.w, pdf.h)
                os.remove(imagem)
                paginas += 1

            os.chdir(self.salvar)

            arquivo = self.arquivo_pdf[:self.arquivo_pdf.rfind('.')]
            pdf.output(arquivo+"(novo).pdf", "F")
            pdf.close()

            self.detalhes.append("%d páginas criadas." % paginas)
            time.sleep(0.5)
            self.detalhes.append("PDF criado.")
            time.sleep(1)
            self.detalhes.append("Fim.")
            os.chdir(self.diretorio)
            os.rmdir(self.path)

            if self.excluir_arquivo_original:
                os.chdir(self.diretorio)
                os.remove(self.arquivo_pdf)

        except Exception:
            self.detalhes.append("Erro na criação do PDF")
            self.detalhes.append("Fim.")
            pdf.close()
