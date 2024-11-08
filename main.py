import cadastro
import customtkinter
import tkinter as tk
import defs


# Configurações iniciais
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

    
def abrir_janela_principal(nome_usuario):
    # Criar nova janela principal
    janela_principal = customtkinter.CTkToplevel()
    janela_principal.title("Xbox Game Pass")
    janela_principal.attributes('-fullscreen', True)
    
    # Frame principal com fundo escuro
    frame_principal = customtkinter.CTkFrame(janela_principal, fg_color="#1A1A1A")
    frame_principal.pack(fill="both", expand=True)
    
    # Frame lateral esquerdo
    frame_lateral = customtkinter.CTkFrame(frame_principal, fg_color="#2D2D2D", width=200)
    frame_lateral.pack(side="left", fill="y", padx=2, pady=2)
    
    # Frame superior para o nome do usuário e pesquisa
    frame_superior = customtkinter.CTkFrame(frame_principal, fg_color="#2D2D2D", height=50)
    frame_superior.pack(side="top", fill="x", padx=2, pady=2)
    
    # Nome do usuário
    label_usuario = customtkinter.CTkLabel(
        frame_superior,
        text=nome_usuario.upper(),
        font=("Segoe UI", 16, "bold"),
        text_color="white"
    )
    label_usuario.pack(side="left", padx=20)
    
    # Barra de pesquisa
    barra_pesquisa = customtkinter.CTkEntry(
        frame_superior,
        placeholder_text="Pesquisar jogos, complementos e muito mais",
        width=400,
        height=35
    )
    barra_pesquisa.pack(side="right", padx=20, pady=7)
    
    # Botões do menu lateral
    botoes_menu = [
        ("Início", "🏠"),
        ("Game Pass", "🎮"),
        ("Minha Biblioteca", "📚"),
        ("Cloud Gaming", "☁️"),
        ("Store", "🛍️")
    ]
    
    for texto, icone in botoes_menu:
        botao = customtkinter.CTkButton(
            frame_lateral,
            text=f"{icone} {texto}",
            font=("Segoe UI", 14),
            fg_color="transparent",
            text_color="white",
            hover_color="#3D3D3D",
            anchor="w",
            height=40
        )
        botao.pack(fill="x", padx=5, pady=2)
    
    # Frame para conteúdo principal
    frame_conteudo = customtkinter.CTkFrame(frame_principal, fg_color="#1A1A1A")
    frame_conteudo.pack(fill="both", expand=True, padx=2, pady=2)
    
    # Título da seção
    titulo_secao = customtkinter.CTkLabel(
        frame_conteudo,
        text="Adicionados recentemente ao Game Pass",
        font=("Segoe UI", 20, "bold"),
        text_color="white"
    )
    titulo_secao.pack(anchor="w", padx=20, pady=20)
    
    # Frame para grid de jogos
    frame_jogos = customtkinter.CTkFrame(frame_conteudo, fg_color="transparent")
    frame_jogos.pack(fill="both", expand=True, padx=20)
    
    # Lista de jogos com suas informações
    jogos = [
        {
            "nome": "Metal Slug Tactics",
            "desenvolvedora": "Dotemu",
            "imagem": "metal_slug.png"
        },
        {
            "nome": "StarCraft II",
            "desenvolvedora": "Blizzard Entertainment",
            "imagem": "starcraft.png"
        },
        {
            "nome": "Dead Island 2",
            "desenvolvedora": "Deep Silver",
            "imagem": "dead_island.png"
        },
        {
            "nome": "Call of Duty: Black Ops",
            "desenvolvedora": "Activision",
            "imagem": "cod.png"
        },
        {
            "nome": "Ashen",
            "desenvolvedora": "Annapurna Interactive",
            "imagem": "ashen.png"
        }
    ]
    
    for i, jogo in enumerate(jogos):
        # Criar card para cada jogo
        card = customtkinter.CTkFrame(frame_jogos, fg_color="#2D2D2D")
        card.grid(row=i//3, column=i%3, padx=10, pady=10, sticky="nsew")
        
        # Informações do jogo
        nome_jogo = customtkinter.CTkLabel(
            card,
            text=jogo["nome"],
            font=("Segoe UI", 14, "bold"),
            text_color="white"
        )
        nome_jogo.pack(pady=(20,5))
        
        desenvolvedora = customtkinter.CTkLabel(
            card,
            text=jogo["desenvolvedora"],
            font=("Segoe UI", 12),
            text_color="gray"
        )
        desenvolvedora.pack(pady=(0,20))
        
        # Botão de instalar
        botao_instalar = customtkinter.CTkButton(
            card,
            text="Instalar",
            width=100,
            height=30,
            fg_color="#107C10",
            hover_color="#0B5B0B"
        )
        botao_instalar.pack(pady=(0,20))
    
    # Configurar o grid
    frame_jogos.grid_columnconfigure((0,1,2), weight=1)
    
    # Botão de logout
    botao_logout = customtkinter.CTkButton(
        frame_lateral,
        text="Logout",
        font=("Segoe UI", 14),
        fg_color="#E1E1E1",
        text_color="black",
        hover_color="#D1D1D1",
        height=35,
        command=lambda: [janela_principal.destroy(), janela.deiconify()]
    )
    botao_logout.pack(side="bottom", padx=5, pady=20)

# Mantendo o resto das suas funções originais
def verificar_senha(email_text, janela_senha):
    senha_text = campo_senha.get()
    usuario = cadastro.colecao.find_one({"email": email_text, "senha": senha_text})
    if usuario:
        janela_senha.destroy()
        abrir_janela_principal(usuario["nome"])
    else:
        erro_label_senha.configure(text="Senha incorreta")

def abrir_tela_senha(email_text):
    # Esconde a janela principal
    janela.withdraw()
    
    # Cria nova janela para senha
    janela_senha = customtkinter.CTkToplevel()
    janela_senha.title("Digite sua senha")
    defs.centralizar_janela(janela_senha, 400, 500)
    janela_senha.protocol("WM_DELETE_WINDOW", defs.fechar_app)

    # Frame principal com fundo branco
    frame_senha = customtkinter.CTkFrame(janela_senha, fg_color="white")
    frame_senha.pack(fill="both", expand=True)

    # Logo Microsoft
    microsoft_label = customtkinter.CTkLabel(
        frame_senha,
        text="Microsoft",
        font=("Segoe UI", 18),
        text_color="black"
    )
    microsoft_label.pack(pady=(20, 5))

    # Título
    titulo_senha = customtkinter.CTkLabel(
        frame_senha,
        text="Digite sua senha",
        font=("Segoe UI", 24, "bold"),
        text_color="black"
    )
    titulo_senha.pack(pady=(5, 10))

    # Mostra o email
    email_label = customtkinter.CTkLabel(
        frame_senha,
        text=email_text,
        font=("Segoe UI", 14),
        text_color="black"
    )
    email_label.pack(pady=(0, 20))

    # Campo de senha
    global campo_senha, erro_label_senha
    campo_senha = customtkinter.CTkEntry(
        frame_senha,
        width=300,
        height=40,
        placeholder_text="Digite sua senha",
        border_width=1,
        corner_radius=3,
        show="*",
        fg_color="white",
        text_color="black"
    )
    campo_senha.pack(pady=(0, 10))

    # Botões
    botao_entrar = customtkinter.CTkButton(
        frame_senha,
        text="Entrar",
        width=300,
        height=40,
        fg_color="#0078D4",
        hover_color="#006CBD",
        corner_radius=3,
        command=lambda: verificar_senha(email_text, janela_senha)
    )
    botao_entrar.pack(pady=20)

    botao_voltar_senha = customtkinter.CTkButton(
        frame_senha,
        text="Voltar",
        width=300,
        height=40,
        fg_color="transparent",
        text_color="black",
        hover_color="#f0f0f0",
        border_width=1,
        border_color="#e0e0e0",
        command=lambda: [janela_senha.destroy(), janela.deiconify()]
    )
    botao_voltar_senha.pack(pady=(0, 20))

    # Label para mensagens de erro
    erro_label_senha = customtkinter.CTkLabel(
        frame_senha,
        text="",
        text_color="red",
        font=("Segoe UI", 12)
    )
    erro_label_senha.pack(pady=(10, 0))

def verificar_email():
    email_text = email.get()
    if not defs.validar_email(email_text):
        defs.mostrar_erro_temporario("Email inválido")
        return
    
    usuario = defs.colecao.find_one({"email": email_text})
    if usuario:
        abrir_tela_senha(email_text)
    else:
        defs.mostrar_erro_temporario("Email não encontrado")


# Janela principal
janela = customtkinter.CTk()
janela.title("Xbox Game Pass")
defs.centralizar_janela(janela, 400, 500)
janela.protocol("WM_DELETE_WINDOW", defs.fechar_app)

# Frame principal
frame = customtkinter.CTkFrame(janela, fg_color="white")
frame.pack(fill="both", expand=True)

# Logo Microsoft
microsoft_label = customtkinter.CTkLabel(
    frame,
    text="Microsoft",
    font=("Segoe UI", 18),
    text_color="black"
)
microsoft_label.pack(pady=(20, 5))

# Título
titulo = customtkinter.CTkLabel(
    frame,
    text="Entrar",
    font=("Segoe UI", 24, "bold"),
    text_color="black"
)
titulo.pack(pady=(5, 5))

# Subtítulo
subtitle = customtkinter.CTkLabel(
    frame,
    text="Continuar para Xbox Game Pass",
    font=("Segoe UI", 12),
    text_color="gray"
)
subtitle.pack(pady=(0, 20))

# Campo de email
email = customtkinter.CTkEntry(
    frame,
    width=300,
    height=40,
    placeholder_text="Email, telefone ou Skype",
    border_width=1,
    corner_radius=3,
    fg_color="white",
    text_color="black"
)
email.pack(pady=(10, 5))

# Frame para "Não tem uma conta?"
create_account_frame = customtkinter.CTkFrame(frame, fg_color="transparent")
create_account_frame.pack(fill="x", padx=20, pady=(5, 20))

no_account_label = customtkinter.CTkLabel(
    create_account_frame,
    text="Não tem uma conta?",
    font=("Segoe UI", 12),
    text_color="gray"
)
no_account_label.pack(side="left", padx=(50, 0))

create_account_link = customtkinter.CTkLabel(
    create_account_frame,
    text="Crie uma!",
    font=("Segoe UI", 12),
    text_color="#0078D4",
    cursor="hand2"
)
create_account_link.pack(side="left", padx=5)
create_account_link.bind("<Button-1>", lambda e: cadastro.abrir_janela_cadastro())

# Botão próximo
botao_proximo = customtkinter.CTkButton(
    frame,
    text="Próximo",
    width=300,
    height=40,
    fg_color="#0078D4",
    hover_color="#006CBD",
    corner_radius=3,
    command=verificar_email
)
botao_proximo.pack(pady=20)

# Label para mensagens de erro
erro_label = customtkinter.CTkLabel(
    frame,
    text="",
    text_color="red",
    font=("Segoe UI", 12)
)
erro_label.pack(pady=(10, 0))

janela.mainloop()