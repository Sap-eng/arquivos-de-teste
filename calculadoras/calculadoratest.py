# calculadora

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
operacao = input("Digite a operacao (+, -, *, /): ")

match operacao:
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        res = num1 / num2
    case _:
        print("Operacao invalida!")
        res = None

if res is not None:
    print(f"Resultado é igual a {res}")

    
    
    import tkinter as tk

    janela = tk.Tk ()
    janela.title("minha calcluladora")
    janela.geometry("300x200")

    texto = tk.Label(janela,text="A resposta esta ai no codigo: analise.")
    texto.pack()
    janela.mainloop()
