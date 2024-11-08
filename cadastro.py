import customtkinter
import tkinter as tk
import main
import defs

def cadastrar_usuario(email, senha, nome, janela_cadastro):
    if not main.validar_email(email):
        defs.mostrar_erro("E-mail inválido!")
        return

    if main.colecao.find_one({"email": email}):
        defs.mostrar_erro("E-mail já cadastrado!")
        return
    
    try:
        usuario = {
            "nome": nome,
            "email": email,
            "senha": senha
        }
        
        main.colecao.insert_one(usuario)
        
        # Primeiro destrua todas as janelas intermediárias
        for widget in main.janela.winfo_children():
            if isinstance(widget, customtkinter.CTkToplevel):
                widget.destroy()
        
        janela_cadastro.destroy()
        
        # Depois mostre a mensagem de sucesso
        alerta = customtkinter.CTkToplevel()
        alerta.title("Sucesso")
        alerta.geometry("300x150")
        defs.centralizar_janela(alerta, 300, 150)
        alerta.grab_set()
        
        mensagem_sucesso = customtkinter.CTkLabel(alerta, text="Cadastro realizado com sucesso!")
        mensagem_sucesso.pack(pady=20)

        def fechar_e_mostrar_login():
            alerta.destroy()
            main.janela.deiconify()
        
        botao_ok = customtkinter.CTkButton(alerta, text="OK", command=fechar_e_mostrar_login)
        botao_ok.pack(pady=10)
        
    except Exception as e:
        defs.mostrar_erro(f"Erro ao cadastrar: {str(e)}")

def abrir_tela_nome(email, senha, janela_senha):
    # Desativa a janela anterior sem destruí-la
    janela_senha.withdraw()
    
    janela_nome = customtkinter.CTkToplevel()
    janela_nome.title("Digite seu nome")
    defs.centralizar_janela(janela_nome, 400, 500)
    janela_nome.protocol("WM_DELETE_WINDOW", defs.fechar_app)
    
    frame_nome = customtkinter.CTkFrame(janela_nome, fg_color="white")
    frame_nome.pack(fill="both", expand=True)
    
    microsoft_label = customtkinter.CTkLabel(
        frame_nome,
        text="Microsoft",
        font=("Segoe UI", 18),
        text_color="black"
    )
    microsoft_label.pack(pady=(20, 5))
    
    titulo_nome = customtkinter.CTkLabel(
        frame_nome,
        text="Como devemos chamar você?",
        font=("Segoe UI", 24, "bold"),
        text_color="black"
    )
    titulo_nome.pack(pady=(5, 20))
    
    campo_nome = customtkinter.CTkEntry(
        frame_nome,
        width=300,
        height=40,
        placeholder_text="Digite seu nome",
        border_width=1,
        corner_radius=3
    )
    campo_nome.pack(pady=(0, 20))

    def finalizar_cadastro():
        nome = campo_nome.get()
        if nome.strip():  # Verifica se o nome não está vazio
            cadastrar_usuario(email, senha, nome, janela_nome)
        else:
            defs.mostrar_erro("Por favor, digite seu nome!")
    
    botao_finalizar = customtkinter.CTkButton(
        frame_nome,
        text="Finalizar cadastro",
        width=300,
        height=40,
        fg_color="#0078D4",
        hover_color="#006CBD",
        corner_radius=3,
        command=finalizar_cadastro
    )
    botao_finalizar.pack(pady=10)
    
    def voltar():
        janela_nome.destroy()
        janela_senha.deiconify()
    
    botao_voltar = customtkinter.CTkButton(
        frame_nome,
        text="Voltar",
        width=300,
        height=40,
        fg_color="transparent",
        text_color="black",
        hover_color="#f0f0f0",
        border_width=1,
        border_color="#e0e0e0",
        command=voltar
    )
    botao_voltar.pack(pady=10)

    # Foca no campo de nome após a janela ser criada
    janela_nome.after(100, lambda: campo_nome.focus())

def abrir_tela_senha_cadastro(email, janela_cadastro):
    janela_cadastro.withdraw()
    
    janela_senha = customtkinter.CTkToplevel()
    janela_senha.title("Crie sua senha")
    defs.centralizar_janela(janela_senha, 400, 500)
    janela_senha.protocol("WM_DELETE_WINDOW", defs.fechar_app)
    
    frame_senha = customtkinter.CTkFrame(janela_senha, fg_color="white")
    frame_senha.pack(fill="both", expand=True)
    
    microsoft_label = customtkinter.CTkLabel(
        frame_senha,
        text="Microsoft",
        font=("Segoe UI", 18),
        text_color="black"
    )
    microsoft_label.pack(pady=(20, 5))
    
    titulo_senha = customtkinter.CTkLabel(
        frame_senha,
        text="Crie uma senha",
        font=("Segoe UI", 24, "bold"),
        text_color="black"
    )
    titulo_senha.pack(pady=(5, 10))
    
    email_label = customtkinter.CTkLabel(
        frame_senha,
        text=email,
        font=("Segoe UI", 14),
        text_color="black"
    )
    email_label.pack(pady=(0, 20))
    
    campo_senha = customtkinter.CTkEntry(
        frame_senha,
        width=300,
        height=40,
        placeholder_text="Crie uma senha",
        border_width=1,
        corner_radius=3,
        show="*"
    )
    campo_senha.pack(pady=(0, 20))
    
    botao_proximo = customtkinter.CTkButton(
        frame_senha,
        text="Próximo",
        width=300,
        height=40,
        fg_color="#0078D4",
        hover_color="#006CBD",
        corner_radius=3,
        command=lambda: abrir_tela_nome(email, campo_senha.get(), janela_senha)
    )
    botao_proximo.pack(pady=10)
    
    botao_voltar = customtkinter.CTkButton(
        frame_senha,
        text="Voltar",
        width=300,
        height=40,
        fg_color="transparent",
        text_color="black",
        hover_color="#f0f0f0",
        border_width=1,
        border_color="#e0e0e0",
        command=lambda: [janela_senha.destroy(), janela_cadastro.deiconify()]
    )
    botao_voltar.pack(pady=10)

def verificar_email_cadastro(email, janela_cadastro):
    if not defs.validar_email(email):
        defs.mostrar_erro("Email inválido")
        return
    
    usuario = defs.colecao.find_one({"email": email})
    if usuario:
        defs.mostrar_erro("Email já cadastrado")
        return
    
    abrir_tela_senha_cadastro(email, janela_cadastro)

def abrir_janela_cadastro():
    main.janela.withdraw()
    janela_cadastro = customtkinter.CTkToplevel()
    janela_cadastro.title("Criar conta")
    defs.centralizar_janela(janela_cadastro, 400, 500)
    janela_cadastro.protocol("WM_DELETE_WINDOW", defs.fechar_app)
    
    frame_cadastro = customtkinter.CTkFrame(janela_cadastro, fg_color="white")
    frame_cadastro.pack(fill="both", expand=True)
    
    microsoft_label = customtkinter.CTkLabel(
        frame_cadastro,
        text="Microsoft",
        font=("Segoe UI", 18),
        text_color="black"
    )
    microsoft_label.pack(pady=(20, 5))
    
    titulo = customtkinter.CTkLabel(
        frame_cadastro,
        text="Criar conta",
        font=("Segoe UI", 24, "bold"),
        text_color="black"
    )
    titulo.pack(pady=(5, 20))
    
    email_entry = customtkinter.CTkEntry(
        frame_cadastro,
        width=300,
        height=40,
        placeholder_text="nome@example.com",
        border_width=1,
        corner_radius=3
    )
    email_entry.pack(pady=(0, 10))
    
    obter_email = customtkinter.CTkLabel(
        frame_cadastro,
        text="Obter novo endereço de email",
        text_color="#0078D4",
        font=("Segoe UI", 12, "underline"),
        cursor="hand2"
    )
    obter_email.pack(pady=(0, 20))
    
    botao_proximo = customtkinter.CTkButton(
        frame_cadastro,
        text="Próximo",
        width=300,
        height=40,
        fg_color="#0078D4",
        hover_color="#006CBD",
        corner_radius=3,
        command=lambda: verificar_email_cadastro(email_entry.get(), janela_cadastro)
    )
    botao_proximo.pack(pady=10)
    
    botao_voltar = customtkinter.CTkButton(
        frame_cadastro,
        text="Voltar",
        width=300,
        height=40,
        fg_color="transparent",
        text_color="black",
        hover_color="#f0f0f0",
        border_width=1,
        border_color="#e0e0e0",
        command=lambda: [janela_cadastro.destroy(), main.janela.deiconify()]
    )
    botao_voltar.pack(pady=10)