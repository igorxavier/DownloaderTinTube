import os

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from pytube import YouTube

basedir = os.path.dirname(__file__)



def yt_on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {int(pct_completed)} %")
    window.pro_bar.setValue(int(pct_completed))
    QtGui.QGuiApplication.processEvents()
    
    
def baixarItems():
    yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo', on_progress_callback=yt_on_progress)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

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

loader = QUiLoader()
app = QtWidgets.QApplication()
window = loader.load("main.ui", None)


# Abrir Menu
window.btn_menu.clicked.connect(animarMenu)
window.btn_menu.setIcon(QtGui.QIcon(os.path.join(basedir, './icons/menu.svg')))
# Botões do Menu
window.btn_colar.clicked.connect(colarItems)
window.btn_excluir.clicked.connect(removeSelecionado)
window.btn_limpar.clicked.connect(limparItems)
window.btn_baixar.clicked.connect(baixarItems)

window.show()

app.exec()