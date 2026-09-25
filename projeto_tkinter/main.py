import tkinter as tk

import dados
from interface import Aplicativo


def main():
    dados.criar_banco()

    janela = tk.Tk()

    Aplicativo(janela)

    janela.mainloop()


if __name__ == "__main__":
    main()