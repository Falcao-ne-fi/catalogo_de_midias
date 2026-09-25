import tkinter as tk
from tkinter import ttk, messagebox

import dados
import validacoes


class Aplicativo:
    def __init__(self, janela):
        self.janela = janela

        self.id_selecionado = None
        self.alteracoes_pendentes = False

        self.configurar_janela()
        self.criar_estilo()
        self.criar_interface()

        self.atualizar_lista()
        self.atualizar_resumo()

    # ========================================================
    # CONFIGURAÇÃO
    # ========================================================

    def configurar_janela(self):
        self.janela.title("Catálogo de Mídias")
        self.janela.geometry("950x650")
        self.janela.minsize(850, 600)

        self.janela.protocol(
            "WM_DELETE_WINDOW",
            self.fechar_programa
        )

    def criar_estilo(self):
        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        estilo.configure(
            "Titulo.TLabel",
            font=("Arial", 20, "bold")
        )

        estilo.configure(
            "Subtitulo.TLabel",
            font=("Arial", 11)
        )

        estilo.configure(
            "Treeview",
            rowheight=28
        )

    # ========================================================
    # INTERFACE PRINCIPAL
    # ========================================================

    def criar_interface(self):

        cabecalho = ttk.Frame(
            self.janela,
            padding=15
        )

        cabecalho.pack(fill="x")

        ttk.Label(
            cabecalho,
            text="Catálogo de Mídias",
            style="Titulo.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            cabecalho,
            text="Organize filmes, séries, livros e jogos.",
            style="Subtitulo.TLabel"
        ).pack(anchor="w")

        self.notebook = ttk.Notebook(self.janela)
        self.notebook.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        self.aba_cadastro = ttk.Frame(
            self.notebook,
            padding=20
        )

        self.aba_catalogo = ttk.Frame(
            self.notebook,
            padding=20
        )

        self.aba_resumo = ttk.Frame(
            self.notebook,
            padding=20
        )

        self.notebook.add(
            self.aba_cadastro,
            text="Cadastro"
        )

        self.notebook.add(
            self.aba_catalogo,
            text="Catálogo"
        )

        self.notebook.add(
            self.aba_resumo,
            text="Resumo"
        )

        self.criar_aba_cadastro()
        self.criar_aba_catalogo()
        self.criar_aba_resumo()

    # ========================================================
    # ABA CADASTRO
    # ========================================================

    def criar_aba_cadastro(self):

        aba = self.aba_cadastro

        aba.columnconfigure(1, weight=1)
        aba.rowconfigure(6, weight=1)

        self.label_modo = ttk.Label(
            aba,
            text="Novo cadastro",
            font=("Arial", 12, "bold")
        )

        self.label_modo.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(0, 20)
        )

        # Título

        ttk.Label(
            aba,
            text="Título *"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=8
        )

        self.entrada_titulo = ttk.Entry(aba)

        self.entrada_titulo.grid(
            row=1,
            column=1,
            sticky="ew",
            pady=8
        )

        # Categoria

        ttk.Label(
            aba,
            text="Categoria *"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=8
        )

        self.categoria_var = tk.StringVar()

        self.combo_categoria = ttk.Combobox(
            aba,
            textvariable=self.categoria_var,
            state="readonly",
            values=[
                "Filme",
                "Série",
                "Livro",
                "Jogo"
            ]
        )

        self.combo_categoria.grid(
            row=2,
            column=1,
            sticky="ew",
            pady=8
        )

        # Tipo

        ttk.Label(
            aba,
            text="Gênero / Tipo *"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=8
        )

        self.tipo_var = tk.StringVar()

        self.combo_tipo = ttk.Combobox(
            aba,
            textvariable=self.tipo_var,
            values=[
                "Ação",
                "Aventura",
                "Comédia",
                "Drama",
                "Fantasia",
                "Ficção científica",
                "Horror",
                "Romance",
                "RPG",
                "Estratégia",
                "Outro"
            ]
        )

        self.combo_tipo.grid(
            row=3,
            column=1,
            sticky="ew",
            pady=8
        )

        # Nota

        ttk.Label(
            aba,
            text="Nota (0–10) *"
        ).grid(
            row=4,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=8
        )

        self.nota_var = tk.StringVar()

        self.entrada_nota = ttk.Entry(
            aba,
            textvariable=self.nota_var
        )

        self.entrada_nota.grid(
            row=4,
            column=1,
            sticky="ew",
            pady=8
        )

        # Status

        ttk.Label(
            aba,
            text="Status *"
        ).grid(
            row=5,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=8
        )

        self.status_var = tk.StringVar()

        self.combo_status = ttk.Combobox(
            aba,
            textvariable=self.status_var,
            state="readonly",
            values=[
                "Quero consumir",
                "Em andamento",
                "Concluído"
            ]
        )

        self.combo_status.grid(
            row=5,
            column=1,
            sticky="ew",
            pady=8
        )

        # Observação

        ttk.Label(
            aba,
            text="Observação"
        ).grid(
            row=6,
            column=0,
            sticky="nw",
            padx=(0, 10),
            pady=8
        )

        self.texto_observacao = tk.Text(
            aba,
            height=8,
            wrap="word"
        )

        self.texto_observacao.grid(
            row=6,
            column=1,
            sticky="nsew",
            pady=8
        )

        # Botões

        frame_botoes = ttk.Frame(aba)

        frame_botoes.grid(
            row=7,
            column=0,
            columnspan=2,
            sticky="e",
            pady=(20, 0)
        )

        ttk.Button(
            frame_botoes,
            text="Limpar",
            command=self.limpar_formulario
        ).pack(side="left", padx=5)

        ttk.Button(
            frame_botoes,
            text="Cadastrar",
            command=self.cadastrar
        ).pack(side="left", padx=5)

        ttk.Button(
            frame_botoes,
            text="Salvar edição",
            command=self.editar
        ).pack(side="left", padx=5)

    # ========================================================
    # ABA CATÁLOGO
    # ========================================================

    def criar_aba_catalogo(self):

        aba = self.aba_catalogo

        aba.columnconfigure(0, weight=1)
        aba.rowconfigure(2, weight=1)

        frame_pesquisa = ttk.Frame(aba)

        frame_pesquisa.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, 15)
        )

        frame_pesquisa.columnconfigure(
            1,
            weight=1
        )

        ttk.Label(
            frame_pesquisa,
            text="Pesquisar:"
        ).grid(
            row=0,
            column=0,
            padx=(0, 10)
        )

        self.entrada_pesquisa = ttk.Entry(
            frame_pesquisa
        )

        self.entrada_pesquisa.grid(
            row=0,
            column=1,
            sticky="ew"
        )

        ttk.Button(
            frame_pesquisa,
            text="Pesquisar",
            command=self.pesquisar
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        ttk.Button(
            frame_pesquisa,
            text="Limpar busca",
            command=self.atualizar_lista
        ).grid(
            row=0,
            column=3
        )

        self.label_resultado = ttk.Label(
            aba,
            text="0 registro(s)"
        )

        self.label_resultado.grid(
            row=1,
            column=0,
            sticky="w",
            pady=(0, 5)
        )

        # Tabela

        frame_tabela = ttk.Frame(aba)

        frame_tabela.grid(
            row=2,
            column=0,
            sticky="nsew"
        )

        frame_tabela.columnconfigure(0, weight=1)
        frame_tabela.rowconfigure(0, weight=1)

        colunas = (
            "id",
            "titulo",
            "categoria",
            "tipo",
            "nota",
            "status"
        )

        self.tabela = ttk.Treeview(
            frame_tabela,
            columns=colunas,
            show="headings",
            selectmode="browse"
        )

        nomes = {
            "id": "ID",
            "titulo": "Título",
            "categoria": "Categoria",
            "tipo": "Gênero / Tipo",
            "nota": "Nota",
            "status": "Status"
        }

        for coluna in colunas:
            self.tabela.heading(
                coluna,
                text=nomes[coluna]
            )

        self.tabela.column("id", width=50)
        self.tabela.column("titulo", width=250)
        self.tabela.column("categoria", width=100)
        self.tabela.column("tipo", width=150)
        self.tabela.column("nota", width=70)
        self.tabela.column("status", width=150)

        self.tabela.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        barra = ttk.Scrollbar(
            frame_tabela,
            orient="vertical",
            command=self.tabela.yview
        )

        barra.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.tabela.configure(
            yscrollcommand=barra.set
        )

        self.tabela.bind(
            "<Double-1>",
            self.carregar_selecionado
        )

        # Ações

        frame_acoes = ttk.Frame(aba)

        frame_acoes.grid(
            row=3,
            column=0,
            sticky="e",
            pady=(15, 0)
        )

        ttk.Button(
            frame_acoes,
            text="Editar selecionado",
            command=self.carregar_selecionado
        ).pack(side="left", padx=5)

        ttk.Button(
            frame_acoes,
            text="Excluir selecionado",
            command=self.excluir
        ).pack(side="left")

    # ========================================================
    # ABA RESUMO
    # ========================================================

    def criar_aba_resumo(self):

        aba = self.aba_resumo

        ttk.Label(
            aba,
            text="Resumo do catálogo",
            style="Titulo.TLabel"
        ).pack(
            anchor="w",
            pady=(0, 20)
        )

        frame = ttk.Frame(aba)

        frame.pack(
            fill="both",
            expand=True
        )

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        self.label_total = self.criar_indicador(
            frame,
            "Total de mídias",
            0,
            0
        )

        self.label_concluidos = self.criar_indicador(
            frame,
            "Concluídos",
            0,
            1
        )

        self.label_andamento = self.criar_indicador(
            frame,
            "Em andamento",
            1,
            0
        )

        self.label_quero = self.criar_indicador(
            frame,
            "Quero consumir",
            1,
            1
        )

        self.label_media = self.criar_indicador(
            frame,
            "Nota média",
            2,
            0
        )

    def criar_indicador(
        self,
        parent,
        titulo,
        linha,
        coluna
    ):
        frame = ttk.LabelFrame(
            parent,
            text=titulo,
            padding=20
        )

        frame.grid(
            row=linha,
            column=coluna,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        valor = ttk.Label(
            frame,
            text="0",
            font=("Arial", 24, "bold")
        )

        valor.pack()

        return valor

    # ========================================================
    # OPERAÇÕES
    # ========================================================

    def obter_dados_formulario(self):
        titulo = self.entrada_titulo.get().strip()
        categoria = self.categoria_var.get()
        tipo = self.tipo_var.get()
        nota = self.nota_var.get().strip()
        status = self.status_var.get()

        observacao = self.texto_observacao.get(
            "1.0",
            tk.END
        ).strip()

        return (
            titulo,
            categoria,
            tipo,
            nota,
            status,
            observacao
        )

    def cadastrar(self):

        dados = self.obter_dados_formulario()

        titulo, categoria, tipo, nota, status, observacao = dados

        valido, mensagem = validacoes.validar_midia(
            titulo,
            categoria,
            tipo,
            nota,
            status
        )

        if not valido:
            messagebox.showwarning(
                "Dados inválidos",
                mensagem
            )
            return

        try:
            dados.cadastrar_midia(
                titulo,
                categoria,
                tipo,
                float(nota),
                status,
                observacao
            )

            messagebox.showinfo(
                "Sucesso",
                "Mídia cadastrada com sucesso."
            )

            self.limpar_formulario()
            self.atualizar_lista()
            self.atualizar_resumo()

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível cadastrar a mídia.\n\n{erro}"
            )

    def carregar_selecionado(self, event=None):

        selecao = self.tabela.selection()

        if not selecao:
            messagebox.showwarning(
                "Nenhum registro",
                "Selecione uma mídia."
            )
            return

        valores = self.tabela.item(
            selecao[0],
            "values"
        )

        id_midia = valores[0]

        registro = dados.buscar_midia(
            id_midia
        )

        if registro is None:
            return

        (
            id_midia,
            titulo,
            categoria,
            tipo,
            nota,
            status,
            observacao
        ) = registro

        self.id_selecionado = id_midia

        self.entrada_titulo.delete(0, tk.END)
        self.entrada_titulo.insert(0, titulo)

        self.categoria_var.set(categoria)
        self.tipo_var.set(tipo)
        self.nota_var.set(str(nota))
        self.status_var.set(status)

        self.texto_observacao.delete(
            "1.0",
            tk.END
        )

        self.texto_observacao.insert(
            "1.0",
            observacao or ""
        )

        self.label_modo.config(
            text=f"Editando registro #{id_midia}"
        )

        self.notebook.select(
            self.aba_cadastro
        )

    def editar(self):

        if self.id_selecionado is None:
            messagebox.showwarning(
                "Nenhum registro",
                "Selecione uma mídia para editar."
            )
            return

        dados = self.obter_dados_formulario()

        titulo, categoria, tipo, nota, status, observacao = dados

        valido, mensagem = validacoes.validar_midia(
            titulo,
            categoria,
            tipo,
            nota,
            status
        )

        if not valido:
            messagebox.showwarning(
                "Dados inválidos",
                mensagem
            )
            return

        try:
            dados.editar_midia(
                self.id_selecionado,
                titulo,
                categoria,
                tipo,
                float(nota),
                status,
                observacao
            )

            messagebox.showinfo(
                "Sucesso",
                "Mídia atualizada com sucesso."
            )

            self.limpar_formulario()
            self.atualizar_lista()
            self.atualizar_resumo()

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível editar a mídia.\n\n{erro}"
            )

    def excluir(self):

        selecao = self.tabela.selection()

        if not selecao:
            messagebox.showwarning(
                "Nenhum registro",
                "Selecione uma mídia para excluir."
            )
            return

        valores = self.tabela.item(
            selecao[0],
            "values"
        )

        id_midia = valores[0]
        titulo = valores[1]

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Deseja realmente excluir:\n\n{titulo}?"
        )

        if not confirmar:
            return

        try:
            dados.excluir_midia(
                id_midia
            )

            messagebox.showinfo(
                "Sucesso",
                "Mídia excluída."
            )

            self.limpar_formulario()
            self.atualizar_lista()
            self.atualizar_resumo()

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível excluir.\n\n{erro}"
            )

    def pesquisar(self):

        termo = self.entrada_pesquisa.get().strip()

        if termo:
            registros = dados.pesquisar_midias(
                termo
            )
        else:
            registros = dados.listar_midias()

        self.preencher_tabela(registros)

    def atualizar_lista(self):

        self.entrada_pesquisa.delete(
            0,
            tk.END
        )

        registros = dados.listar_midias()

        self.preencher_tabela(registros)

    def preencher_tabela(self, registros):

        self.tabela.delete(
            *self.tabela.get_children()
        )

        for registro in registros:

            id_midia = registro[0]
            titulo = registro[1]
            categoria = registro[2]
            tipo = registro[3]
            nota = registro[4]
            status = registro[5]

            self.tabela.insert(
                "",
                tk.END,
                values=(
                    id_midia,
                    titulo,
                    categoria,
                    tipo,
                    nota,
                    status
                )
            )

        self.label_resultado.config(
            text=f"{len(registros)} registro(s) encontrado(s)"
        )

    def atualizar_resumo(self):

        resumo = dados.obter_resumo()

        self.label_total.config(
            text=str(resumo["total"])
        )

        self.label_concluidos.config(
            text=str(resumo["concluidos"])
        )

        self.label_andamento.config(
            text=str(resumo["andamento"])
        )

        self.label_quero.config(
            text=str(resumo["quero"])
        )

        self.label_media.config(
            text=f"{resumo['media']:.1f}"
        )

    def limpar_formulario(self):

        self.entrada_titulo.delete(
            0,
            tk.END
        )

        self.categoria_var.set("")
        self.tipo_var.set("")
        self.nota_var.set("")
        self.status_var.set("")

        self.texto_observacao.delete(
            "1.0",
            tk.END
        )

        self.id_selecionado = None

        self.label_modo.config(
            text="Novo cadastro"
        )

        self.entrada_titulo.focus()

    # ========================================================
    # SAÍDA
    # ========================================================

    def fechar_programa(self):

        confirmar = messagebox.askyesno(
            "Sair",
            "Deseja realmente sair do aplicativo?"
        )

        if confirmar:
            self.janela.destroy()