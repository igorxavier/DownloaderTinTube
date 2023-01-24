import os
import re
import sys
import time

import instaloader
import requests
import youtube_dl
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QFile, QIODevice, QThread, Signal
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QFileDialog

from tikdown import TikDown

##############################################################################
### Código que resolve os problemas para encontrar arquivos no pyinstaller ###

def resource_path(relative_path = ''):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

###############################################################################

salvar_como = resource_path('baixados')

def colarItems():
    clipboard = QtGui.QGuiApplication.clipboard()
    originalText = clipboard.text()
    lines = originalText.split(os.linesep)

    for line in lines:
        
        line = ''.join(line.split())
        
        if not line.startswith((
            'http://youtube.com/',
            'https://youtube.com/',
            'http://youtu.be/',
            'https://youtu.be/',
            'http://www.youtu.be/',
            'https://www.youtu.be/',
            'http://www.youtube.com/',
            'https://www.youtube.com/',
            # 'https://www.instagram.com/p/',
            # 'http://www.instagram.com/p/',
            'https://instagram.com/reel/',
            'http://instagram.com/reel/',            
            'https://www.instagram.com/reel/',
            'http://www.instagram.com/reel/',
            # 'https://instagram.com/p/',
            # 'http://instagram.com/p/',
            'http://tiktok.com/@',
            'https://tiktok.com/@',
            'http://www.tiktok.com/@',
            'https://www.tiktok.com/@',

            )):
            continue
        
        if window.list_links.findItems(line, QtCore.Qt.MatchExactly):
            continue
        
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
        
class DownloaderIT(QThread):
    new_value = Signal(int)
    url = ''
    def __init__(self):
        super(DownloaderIT, self).__init__()

    def run(self):

        obj = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(obj.context, self.url.split('reel/')[1].strip('/ '))
        photo_url = post.url
        video_url = post.video_url
        
        if video_url:
            self.new_value.emit(0)
            
            response = requests.get(video_url, stream=True,)            
            total_length = response.headers.get('content-length')
            
            timestr = time.strftime("%Y%m%d-%H%M%S")
            
            # download started 
            with open(salvar_como+'/'+timestr+'.mp4', 'wb') as f:
                total_length  = response.headers.get('content-length')
                done = 0
                if total_length :
                    dl = 0
                    total_length = int(total_length )
                    for data in response.iter_content(1024*20):
                        dl += len(data)
                        f.write(data)
                        done = int(100 * dl / total_length)
                        # print(done)
                        # print("\r[%s%s]" % ('=' * done, ' ' * (100-done)))
                        self.new_value.emit(int(done))
                else:
                    f.write(response.content)
                
            self.new_value.emit(100)
        
            window.list_links.takeItem(0)
            
        elif photo_url:
            self.new_value.emit(0)
            
            response = requests.get(photo_url)
            with open("insta.jpg", "wb") as f:
                f.write(response.content)
                
            self.new_value.emit(100)
        
            window.list_links.takeItem(0)
            
            
class DownloaderTT(QThread):
    new_value = Signal(int)
    url = ''
    def __init__(self):
        super(DownloaderTT, self).__init__()

    def tt_on_progress(self, x):
        self.new_value.emit(int(x))

    def run(self):
        self.new_value.emit(0)

        d=TikDown(self.url)

        timestr = time.strftime("%Y%m%d-%H%M%S")

        d[0].download(salvar_como+'/'+timestr+'.mp4', bar=self.tt_on_progress)
        
        self.new_value.emit(100)
        
        window.list_links.takeItem(0)

class DownloaderYT(QThread):
    new_value = Signal(int)
    url = ''
    def __init__(self):
        super(DownloaderYT, self).__init__()

    def run(self):
        self.new_value.emit(0)
        
        try:
            
            ydl_opts = {
                'format': 'best[ext=mp4][height>720]',
                'outtmpl': salvar_como +'/'+ '%(title)s' + '.mp4',
                'progress_hooks': [self.yt_on_progress],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt.url])
                
                window.list_links.takeItem(0)
                
        except:
            print('Não foi possível realizar o download')
            window.list_links.takeItem(0)
            return

    def yt_on_progress(self, d):
        if d['status'] == 'downloading':
            p = d['_percent_str']
            p = p.replace('%','').split('.')[0]
            print(d['filename'], d['_percent_str'], d['_eta_str'])
            self.new_value.emit(int(p))

class IniciarLista(QThread):
    def __init__(self):
        super(IniciarLista, self).__init__()

    def run(self):
        if window.list_links.item(0) != None:
            for x in range(window.list_links.count()):
                print((window.list_links.item(x).text()))

            while window.list_links.item(0) != None:
                
                if window.list_links.item(0).text().startswith((
                    'http://youtube.com/',
                    'https://youtube.com/',
                    'http://youtu.be/',
                    'https://youtu.be/',
                    'http://www.youtu.be/',
                    'https://www.youtu.be/',
                    'http://www.youtube.com/',
                    'https://www.youtube.com/',
                )):        
                    yt.url = window.list_links.item(0).text()
                    yt.start()
                    
                elif window.list_links.item(0).text().startswith((
                    'http://tiktok.com/@',
                    'https://tiktok.com/@',
                    'http://www.tiktok.com/@',
                    'https://www.tiktok.com/@',
                )):        
                    tt.url = window.list_links.item(0).text()
                    tt.start()
                    
                elif window.list_links.item(0).text().startswith((
                    'https://instagram.com/reel/',
                    'http://instagram.com/reel/',
                    'https://www.instagram.com/reel/',
                    'http://www.instagram.com/reel/',
                    # 'https://instagram.com/p/',
                    # 'http://instagram.com/p/',
                    # 'https://www.instagram.com/p/',
                    # 'http://www.instagram.com/p/',
                )):        
                    it.url = window.list_links.item(0).text()
                    it.start()
                    
                    
                    
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
    
def inicar_downloader_it():
    it.start()

def parar_downloader_it():
    it.terminate()

##############################################################################
###  Código para selecionar local para salvar arquivos, salvar como pasta  ###

def onde_salvar():
    global salvar_como
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.Directory)

    if dialog.exec_():
        # fileNames = dialog.selectedFiles()
        fileNames = dialog.directory()
        print(fileNames.path())
        salvar_como = fileNames.path()
        print(salvar_como)
        window.edit_local.setText(salvar_como)

def exibir_window():
    valor_registro=registro.edit_registro.text()
    if valor_registro == '12345':
        window.show()
        registro.close()
        
    print(valor_registro)
    # window.show()

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

    window.btn_pasta.clicked.connect(onde_salvar)
    
    window.edit_local.setText(salvar_como)
    
    registro.btn_registrar.clicked.connect(exibir_window)
    
    window.pro_bar.setValue(0)

    iniciar = IniciarLista()
    
    yt = DownloaderYT()
    yt.new_value.connect(altera_barra)

    tt = DownloaderTT()
    tt.new_value.connect(altera_barra)
    
    it = DownloaderIT()
    it.new_value.connect(altera_barra)
    
    registro.show()
    
    sys.exit(app.exec())