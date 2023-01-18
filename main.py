import os
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QThread, Signal
from pytube import YouTube
from tiktok_downloader import TikDown


salvar_como = '.'

##############################################################################
### Código que resolve os problemas para encontrar arquivos no pyinstaller ###

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

###############################################################################


def colarItems():
    clipboard = QtGui.QGuiApplication.clipboard()
    originalText = clipboard.text()
    lines = originalText.split(os.linesep)

    for line in lines:
        window.list_links.addItem(line)
        
def limparItems():
    window.list_links.clear()
    
def removeSelecionado():
    listItems=window.list_links.selectedItems()
    if not listItems: return        
    for item in listItems:
       window.list_links.takeItem(window.list_links.row(item))
       
def animarMenu():
        width = window.frm_lateral.width()

        if width == 9:
            newWidth = 250
        else:
            newWidth = 9

        window.animation = QtCore.QPropertyAnimation(window.frm_lateral, b"minimumWidth")
        window.animation.setDuration(500)
        window.animation.setStartValue(width)
        window.animation.setEndValue(newWidth)
        window.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        window.animation.start()

class DownloaderTT(QThread):
    new_value = Signal(int)
    url = ''
    def __init__(self):
        super(DownloaderTT, self).__init__()

    def run(self):
        self.new_value.emit(0)

        d=TikDown(self.url)
        d[0].download(salvar_como)
        
        self.new_value.emit(100)

class DownloaderYT(QThread):
    new_value = Signal(int)
    url = ''
    def __init__(self):
        super(DownloaderYT, self).__init__()

    def run(self):
        self.new_value.emit(0)
        yt = YouTube(self.url, on_progress_callback=self.yt_on_progress)
        # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        video = yt.streams.get_highest_resolution()
        video.download(salvar_como)
        window.list_links.takeItem(0)

    def yt_on_progress(self, stream, chunk, bytes_remaining):
        """Callback function"""
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        pct_completed = bytes_downloaded / total_size * 100
        print(f"Status: {int(pct_completed)} %")
        self.new_value.emit(int(pct_completed))

class IniciarLista(QThread):
    def __init__(self):
        super(IniciarLista, self).__init__()

    def run(self):
        if window.list_links.item(0) != None:
            for x in range(window.list_links.count()):
                print((window.list_links.item(x).text()))

            while window.list_links.item(0) != None:
                yt.url = window.list_links.item(0).text()
                yt.start()
        else:
            print('esta vazio')


def altera_barra(new_value):
    print(new_value)
    window.pro_bar.setValue(new_value)

def iniciar_lista():
    iniciar.start()

def inicar_downloader_yt():
    yt.start()

def parar_downloader_yt():
    yt.terminate()

def inicar_downloader_tt():
    tt.start()

def parar_downloader_tt():
    tt.terminate()

##############################################################################
###  Código para selecionar local para salvar arquivos, salvar como pasta  ###

def onde_salvar():
    global salvar_como
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.Directory)

    if dialog.exec_():
        # fileNames = dialog.selectedFiles()
        fileNames = dialog.selectedUrls()
        salvar_como = fileNames[0].fileName()

def exibir_registro():
    registro.show()

##############################################################################
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui_main = resource_path("main.ui")
    ui_registro = resource_path("registro.ui")

    ui_file_main = QFile(ui_main)
    ui_file_registro = QFile(ui_registro)

    if not ui_file_main.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_main}: {ui_file_main.errorString()}")
        sys.exit(-1)
        
    if not ui_file_registro.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_registro}: {ui_file_registro.errorString()}")
        sys.exit(-1)

    loader = QUiLoader()

    window = loader.load(ui_file_main)
    registro = loader.load(ui_file_registro)

    ui_file_main.close()
    ui_file_registro.close()

    if not window:
        print(loader.errorString())
        sys.exit(-1)
    
    if not registro:
        print(loader.errorString())
        sys.exit(-1)


    # Abrir Menu
    window.btn_menu.clicked.connect(animarMenu)
    window.btn_menu.setIcon(QtGui.QIcon(os.path.join(resource_path('./icons/menu.svg'))))
    # Botões do Menu
    window.btn_colar.clicked.connect(colarItems)
    window.btn_excluir.clicked.connect(removeSelecionado)
    window.btn_limpar.clicked.connect(limparItems)

    window.btn_baixar.clicked.connect(iniciar_lista)
    # window.btn_baixar.clicked.connect(inicar_downloader_tt)
    # window.btn_baixar.clicked.connect(inicar_downloader_yt)

    # window.btn_pasta.clicked.connect(onde_salvar)
    window.btn_pasta.clicked.connect(exibir_registro)
    
    window.pro_bar.setValue(0)

    iniciar = IniciarLista()
    
    yt = DownloaderYT()
    yt.new_value.connect(altera_barra)

    tt = DownloaderTT()
    tt.new_value.connect(altera_barra)
    
    window.show()
    

    sys.exit(app.exec())