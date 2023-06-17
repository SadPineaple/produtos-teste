from tkinter import *

def telaLoja():
    frame2.place_forget()
    frame3.place_forget()
    frame4.place_forget()
    frame1.place(relwidth=1, relheight=1)

def telaPiso():
    frame1.place_forget()
    frame3.place_forget()
    frame4.place_forget()
    frame2.place(relwidth=1, relheight=1)

def telaMadeira():
    frame1.place_forget()
    frame2.place_forget()
    frame4.place_forget()
    frame3.place(relwidth=1, relheight=1)

def telaPortasX():
    frame1.place_forget()
    frame2.place_forget()
    frame3.place_forget()
    frame4.place(relwidth=1, relheight=1)

def voltar():
    frame1.place_forget()
    frame2.place_forget()
    frame3.place_forget()
    frame4.place_forget()


# Tela Principal
Janela = Tk()
Janela.title("Produtos")
Janela.configure(background= "#e6e6e6")
Janela.state("zoomed")
Janela.resizable(True, True)
Janela.maxsize(width= 1366, height= 768)
Janela.minsize(width=1240, height=600)

# Estrutura da Tela Principal
Label(Janela, text="Tela Principal")
Button(font = ('calibri', 14), text="Loja", bd=0, bg="#07A0C3", fg="#fff", command=telaLoja,
        activebackground='#086788', activeforeground="white").pack()

Button(font = ('calibri', 14), text="Pisos", bd=0, bg="#07A0C3", fg="#fff", command=telaPiso,
       activebackground='#086788', activeforeground="white").pack()

Button(font = ('calibri', 14), text="Madeira", bd=0, bg="#07A0C3", fg="#fff", command=telaMadeira,
       activebackground='#086788', activeforeground="white").pack()

Button(font = ('calibri', 14), text="Portas especiais", bd=0, bg="#07A0C3", fg="#fff", command=telaPortasX,
       activebackground='#086788', activeforeground="white").pack()
       
# ----------------------------------------------------
# Criando As Telas

frame1 = Frame(Janela, bg="blue" )
Button(frame1, text="Voltar", command=voltar).pack()

frame2 = Frame(Janela, bg="black")
Button(frame2, text="Voltar", command=voltar).pack()

frame3 = Frame(Janela, bg="green")
Button(frame3, text="Voltar", command=voltar).pack()

frame4 = Frame(Janela, bg="red")
Button(frame4, text="Voltar", command=voltar).pack()

Janela.mainloop()