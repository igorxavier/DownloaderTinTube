import os
import sys
import time
import pathlib

import getmac
import instaloader
import requests
import youtube_dl
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QFile, QIODevice, QThread, Signal
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QFileDialog, QMessageBox

from configs import *
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

# if not os.path.exists(resource_path('baixados')):
#     os.makedirs(resource_path('baixados'))

# salvar_como = resource_path('baixados')

salvar_como = str(pathlib.Path.home() / 'Desktop')

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
            'https://www.instagram.com/p/',
            'http://www.instagram.com/p/',
            'https://instagram.com/reel/',
            'http://instagram.com/reel/',            
            'https://www.instagram.com/reel/',
            'http://www.instagram.com/reel/',
            'https://instagram.com/p/',
            'http://instagram.com/p/',
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

        try:

            obj = instaloader.Instaloader()

            if (self.url.find('/reel/') != -1):
                post = instaloader.Post.from_shortcode(obj.context, self.url.split('reel/')[1].strip('/ '))
            else:
                post = instaloader.Post.from_shortcode(obj.context, self.url.split('p/')[1].strip('/ '))

            photo_url = post.url
            video_url = post.video_url

            if not os.path.exists(salvar_como+'/instagram'):
                os.makedirs(salvar_como+'/instagram')

            if not os.path.exists(salvar_como+'/instagram/'+post.owner_username):
                os.makedirs(salvar_como+'/instagram/'+post.owner_username)

            timestr = time.strftime("%Y%m%d-%H%M%S")
            
            if video_url:
                self.new_value.emit(0)
                
                response = requests.get(video_url, stream=True,)            
                total_length = response.headers.get('content-length')
                
                # download started 
                with open(salvar_como+'/instagram/'+post.owner_username+'/'+timestr+'.mp4', 'wb') as f:
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
                with open(salvar_como+'/instagram/'+post.owner_username+'/'+timestr+'.png', "wb") as f:
                    f.write(response.content)
                    
                self.new_value.emit(100)
            
                window.list_links.takeItem(0)

        except:
            print('Não foi possível realizar o download')
            window.list_links.takeItem(0)
            return
            
            
class DownloaderTT(QThread):
    new_value = Signal(int)
    url = ''
    def __init__(self):
        super(DownloaderTT, self).__init__()

    def tt_on_progress(self, x):
        self.new_value.emit(int(x))

    def run(self):
        self.new_value.emit(0)

        try:

            d=TikDown(self.url)

            nome = self.url.partition(".com/@")[2].partition("/video/")[0]

            timestr = time.strftime("%Y%m%d-%H%M%S")

            if not os.path.exists(salvar_como+'/tiktok'):
                os.makedirs(salvar_como+'/tiktok')

            if not os.path.exists(salvar_como+'/tiktok/'+nome):
                os.makedirs(salvar_como+'/tiktok/'+nome)

            d[0].download(salvar_como+'/tiktok/'+nome+'/'+timestr+'.mp4', bar=self.tt_on_progress)
            
            self.new_value.emit(100)
            
            window.list_links.takeItem(0)

        except:
            print('Não foi possível realizar o download')
            window.list_links.takeItem(0)
            return

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

class DownloaderYT(QThread):
    new_value = Signal(int)
    url = ''
    def __init__(self):
        super(DownloaderYT, self).__init__()

    def run(self):
        self.new_value.emit(0)

        if not os.path.exists(salvar_como+'/youtube'):
            os.makedirs(salvar_como+'/youtube')
        
        try:
            
            ydl_opts = {
                'format': 'best[ext=mp4][height>480]',
                'outtmpl': salvar_como+'/youtube/'+ '%(title)s' + '.mp4',
                'progress_hooks': [self.yt_on_progress],
                'logger': MyLogger(),
            }
            
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
                
                window.list_links.takeItem(0)
                
        except:
            print('Não foi possível realizar o download')
            window.list_links.takeItem(0)
            return

    def yt_on_progress(self, d):
        if d['status'] == 'downloading':
            p = d['_percent_str']
            p = p.replace('%','').split('.')[0]
            # print(d['filename'], d['_percent_str'], d['_eta_str'])
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
                    'http://youtube.com/shorts/',
                    'https://youtube.com/shorts/',
                    'http://youtu.be/shorts/',
                    'https://youtu.be/shorts/',
                    'http://www.youtu.be/shorts/',
                    'https://www.youtu.be/shorts/',
                    'http://www.youtube.com/shorts/',
                    'https://www.youtube.com/shorts/',
                )):
                    url = window.list_links.item(0).text()
                    
                    if url.startswith((
                        'http://youtube.com/shorts/',
                        'https://youtube.com/shorts/',
                        'http://youtu.be/shorts/',
                        'https://youtu.be/shorts/',
                        'http://www.youtu.be/shorts/',
                        'https://www.youtu.be/shorts/',
                        'http://www.youtube.com/shorts/',
                        'https://www.youtube.com/shorts/',
                    )):
                        url = 'https://youtu.be/' + url.split('shorts/')[1].strip('/ ')

                    yt.url = url
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
                    'https://instagram.com/p/',
                    'http://instagram.com/p/',
                    'https://www.instagram.com/p/',
                    'http://www.instagram.com/p/',
                )):        
                    it.url = window.list_links.item(0).text()
                    it.start()
                    
        else:
            print('Esta vazio')


def altera_barra(new_value):
    # print(new_value)
    window.pro_bar.setValue(new_value)

def iniciar_lista():
    iniciar.start()

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
        
        
def func_verifica_mac():
    try:
        # print(getmac.get_mac_address())
        dados = {
                'id_produto': id_produto,
                'mac': getmac.get_mac_address()
            }
        retorno_verifica_registro = requests.post(url=url_verifica_mac, json=dados)
    except:
        exibir_mbox(
            'Verifique sua conexão com a internet, não foi possível validar sua licença de uso do software!')
        sys.exit(0)


    if retorno_verifica_registro.status_code >= 200 and retorno_verifica_registro.status_code <= 299:
        registro.close()
        
        response_update = retorno_verifica_registro.json()
        if response_update['version'] > versao_robo:
            # print(response_update['version'])
            # window_download(response_update['version'], response_update['url'])
            avisos.lbl_msg.setText(response_update['mensagem'])
            
            # urlLink="<a href="+response_update['url']+">"+response_update['url']+"</a>"
            urlLink="<a href="+response_update['url']+"><span style='text-decoration: underline; color:#55ff7f;'>"+response_update['url']+"</span></a>"
            avisos.lbl_link.setText(urlLink)
            window.show()
            avisos.show()
        window.show()
    else:
        exibir_mbox('Seu registro não foi encontrado, Preencha o Nome e o e-mail utilizados na compra')
        registro.show()

def func_cadastra_mac_email_nome():
    nome=registro.edit_nome.text()
    email=registro.edit_email.text()
    try:
        # window.show()
        dados = {
                    'nome': nome,
                    'email': email,
                    'id_produto': id_produto,
                    'mac': getmac.get_mac_address()
                }
        cadastro_response = requests.post(url=url_cadastra_mac_email_nome, json=dados)
    except:
        exibir_mbox(
            'Verifique sua conexão com a internet, não foi possível validar sua licença de uso do software!')
        sys.exit(0)

    if cadastro_response.status_code >= 200 and cadastro_response.status_code <= 299:
        registro.close()
        window.show()
    else:
        func_verifica_mac()


def exibir_mbox(mensagem):

    dlg = QMessageBox()
    dlg.setWindowTitle("Atenção!")
    dlg.setText(mensagem)
    button = dlg.exec_()

    if button == QMessageBox.Ok:
        print("OK!")

##############################################################################
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui_main = resource_path("main.ui")
    ui_registro = resource_path("registro.ui")
    ui_avisos = resource_path("avisos.ui")

    ui_file_main = QFile(ui_main)
    ui_file_registro = QFile(ui_registro)
    ui_file_avisos = QFile(ui_avisos)

    if not ui_file_main.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_main}: {ui_file_main.errorString()}")
        sys.exit(-1)
        
    if not ui_file_registro.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_registro}: {ui_file_registro.errorString()}")
        sys.exit(-1)
        
    if not ui_file_avisos.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_avisos}: {ui_file_avisos.errorString()}")
        sys.exit(-1)

    loader = QUiLoader()

    window = loader.load(ui_file_main)
    registro = loader.load(ui_file_registro)
    avisos = loader.load(ui_file_avisos)

    ui_file_main.close()
    ui_file_registro.close()
    ui_file_avisos.close()

    if not window:
        print(loader.errorString())
        sys.exit(-1)
    
    if not registro:
        print(loader.errorString())
        sys.exit(-1)
        
    if not avisos:
        print(loader.errorString())
        sys.exit(-1)



    func_verifica_mac()

    registro.btn_registrar.clicked.connect(func_cadastra_mac_email_nome)

    
    # Abrir Menu
    window.btn_menu.clicked.connect(animarMenu)
    window.btn_menu.setIcon(QtGui.QIcon(os.path.join(resource_path('./icons/menu.svg'))))
    # Botões do Menu
    window.btn_colar.clicked.connect(colarItems)
    window.btn_excluir.clicked.connect(removeSelecionado)
    window.btn_limpar.clicked.connect(limparItems)

    window.btn_baixar.clicked.connect(iniciar_lista)

    window.btn_pasta.clicked.connect(onde_salvar)
    
    window.edit_local.setText(salvar_como)
    
    
    window.pro_bar.setValue(0)

    iniciar = IniciarLista()
    
    yt = DownloaderYT()
    yt.new_value.connect(altera_barra)

    tt = DownloaderTT()
    tt.new_value.connect(altera_barra)
    
    it = DownloaderIT()
    it.new_value.connect(altera_barra)
    
    
    sys.exit(app.exec())