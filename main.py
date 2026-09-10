import tkinter as tk
janela = tk.Tk()
janela.title('Calculadora')
janela.geometry('400x400')
janela.configure(bg="#202020")

textvisor = tk.StringVar()
visor = tk.Entry(janela, textvariable=textvisor)
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
contaatual = ""

botoes = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3), ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('0', 4, 1), ('*', 4, 2)]

def pressbt(crt):
    global contaatual

    contaatual = contaatual + str(crt)

    textvisor.set(contaatual)

def calc():
    global contaatual
    try:
        resultado = str(eval(contaatual))
        textvisor.set(resultado)

        contaatual = resultado

    except:
        textvisor.set('Erro.')
        contaatual = ""

def clear():
    global contaatual

    contaatual = ""
    textvisor.set("")

for texto, linha, coluna in botoes:
    btn = tk.Button(janela, text=texto, command= lambda x=texto: pressbt(x), bg="#202020", fg="#00F7FF", font=("Arial", 24))
    btn.grid(row=linha, column=coluna, sticky="nsew")

bcalc = tk.Button(janela, text='=', command=calc, bg="#202020", fg="#7471FF", font=("Arial", 24))
bcalc.grid(row=4, column=0, sticky="nsew")
bclear = tk.Button(janela, text='C', command=clear, bg="#202020", fg="#3B3B3B", font=("Arial", 24))
bclear.grid(row=4, column=3, sticky="nsew")

for i in range(5):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()