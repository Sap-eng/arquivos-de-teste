import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys

arquivo = ""

def caminho_recurso(rel_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, rel_path)


def escolher_arquivo():
    global arquivo

    arquivo = filedialog.askopenfilename(
        title="Escolha um arquivo",
        filetypes=[
            ("Documentos", "*.pptx *.docx *.odt *.ppt *.doc"),
            ("Todos arquivos", "*.*")
        ]
    )

    label_arquivo.config(text=arquivo)


def converter():
    if arquivo == "":
        messagebox.showerror("Erro", "Escolha um arquivo primeiro!")
        return

    pasta_saida = os.path.dirname(arquivo)

    comando = [
        "libreoffice",
        "--headless",
        "--convert-to",
        "pdf",
        arquivo,
        "--outdir",
        pasta_saida
    ]

    try:
        subprocess.run(comando)

        messagebox.showinfo(
            "Sucesso",
            "Arquivo convertido!"
        )

    except Exception as erro:
        messagebox.showerror(
            "Erro",
            str(erro)
        )


janela = tk.Tk()
janela.title("Conversor Universal")
janela.geometry("500x300")

logo_path = caminho_recurso("assets/logo.png")

logo_img = tk.PhotoImage(file=logo_path)

logo = tk.Label(janela, image=logo_img)
logo.pack(pady=10)

titulo = tk.Label(
    janela,
    text="Conversor Universal",
    font=("Arial", 16)
)

titulo.pack()

botao_arquivo = tk.Button(
    janela,
    text="Escolher Arquivo",
    command=escolher_arquivo
)

botao_arquivo.pack(pady=10)

label_arquivo = tk.Label(
    janela,
    text="Nenhum arquivo selecionado",
    wraplength=450
)

label_arquivo.pack()

botao_converter = tk.Button(
    janela,
    text="Converter para PDF",
    command=converter
)

botao_converter.pack(pady=20)

janela.mainloop()