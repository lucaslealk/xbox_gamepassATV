import customtkinter
import tkinter as tk
import re
import sys
import main

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

def mostrar_erro(mensagem):
    alerta = customtkinter.CTkToplevel()
    alerta.title("Erro")
    alerta.geometry("300x150")
    centralizar_janela(alerta, 300, 150)
    alerta.grab_set()
    mensagem_erro = customtkinter.CTkLabel(alerta, text=mensagem)
    mensagem_erro.pack(pady=20)
    
    def fechar_e_mostrar_login():
        alerta.destroy()
        main.janela.deiconify()

def limpar_erro():
    """Limpa a mensagem de erro e reseta o timer"""
    global erro_timer
    main.erro_label.configure(text="")
    erro_timer = None

def mostrar_erro_temporario(mensagem):
    """Exibe uma mensagem de erro que desaparece após 5 segundos"""
    global erro_timer
    
    # Se já existe um timer ativo, cancela ele
    if erro_timer is not None:
        main.janela.after_cancel(erro_timer)
        erro_timer = None
    
    # Exibe a nova mensagem de erro
    main.erro_label.configure(text=mensagem)
    
    # Agenda a limpeza da mensagem para daqui 5 segundos (5000 milissegundos)
    erro_timer = main.janela.after(5000, limpar_erro)