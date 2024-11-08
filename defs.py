import customtkinter
import tkinter as tk
import re
import sys

def validar_email(email):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email)



def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

def fechar_app():
    sys.exit()
