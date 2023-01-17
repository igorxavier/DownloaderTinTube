import os
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QThread, Signal
from pytube import YouTube
from tiktok_downloader import TikDown
import time

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def baixarItemsTT():
    d=TikDown('https://www.tiktok.com/@igorlemoes/video/7183034697834958085')
    d[0].download('video.mp4')

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

class DownloaderYT(QThread):
    new_value = Signal(int)
    def __init__(self):
        super(DownloaderYT, self).__init__()

    def run(self):
        self.new_value.emit(0)
        yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo', on_progress_callback=self.yt_on_progress)
        # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        video = yt.streams.get_highest_resolution()
        video.download()

    def yt_on_progress(self, stream, chunk, bytes_remaining):
        """Callback function"""
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        pct_completed = bytes_downloaded / total_size * 100
        print(f"Status: {int(pct_completed)} %")
        self.new_value.emit(int(pct_completed))


def altera_barra(new_value):
    print(new_value)
    window.pro_bar.setValue(new_value)

def inicar_downloader_yt():
    yt.start()

def parar_downloader_yt():
    yt.terminate()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui_file_name = resource_path("main.ui")
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)


    # Abrir Menu
    window.btn_menu.clicked.connect(animarMenu)
    window.btn_menu.setIcon(QtGui.QIcon(os.path.join(resource_path('./icons/menu.svg'))))
    # Botões do Menu
    window.btn_colar.clicked.connect(colarItems)
    window.btn_excluir.clicked.connect(removeSelecionado)
    window.btn_limpar.clicked.connect(limparItems)

    window.btn_baixar.clicked.connect(inicar_downloader_yt)
    
    window.pro_bar.setValue(0)
    
    yt = DownloaderYT()
    yt.new_value.connect(altera_barra)
    
    window.show()

    sys.exit(app.exec())