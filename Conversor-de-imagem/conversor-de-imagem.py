from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import os

# Função de converter
def converter_imagem():
    arquivo = filedialog.askopenfilename(
        title="Escolha uma imagem",
        filetypes=[
            ("Imagens", "*.png *.jpg *.jpeg *.webp *.bmp")
        ]
    )

    if not arquivo:
        return

    formato = formato_var.get()

    try:
        img = Image.open(arquivo)

        # JPG precisa RGB
        if formato == "jpg":
            img = img.convert("RGB")

        nome_arquivo = os.path.splitext(arquivo)[0]

        novo_arquivo = f"{nome_arquivo}_convertido.{formato}"

        img.save(novo_arquivo)

        messagebox.showinfo(
            "Sucesso",
            f"Imagem convertida!\n\nSalva em:\n{novo_arquivo}"
        )

    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Erro ao converter:\n{erro}"
        )

    

# Janela
janela = Tk()
janela.title("Conversor de Imagem")
janela.geometry("400x250")
janela.resizable(False, False)
janela.configure(bg="#202020")

# Título
titulo = Label(
    janela,
    text="Conversor de Imagens",
    font=("Arial", 18, "bold"),
    bg="#202020",
    fg="white"
)
titulo.pack(pady=20)

# Texto
texto = Label(
    janela,
    text="Escolha o formato de saída:",
    font=("Arial", 12),
    bg="#202020",
    fg="white"
)
texto.pack()

# Lista de formatos
formato_var = StringVar()
formato_var.set("png")

opcoes = OptionMenu(
    janela,
    formato_var,
    "png",
    "jpg",
    "webp",
    "bmp"
)

opcoes.config(font=("Arial", 12))
opcoes.pack(pady=10)

# Botão
botao = Button(
    janela,
    text="Selecionar e Converter",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=10,
    command=converter_imagem
)

botao.pack(pady=20)

# Rodar programa
janela.mainloop()

