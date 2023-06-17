from tkinter import *

Janela = Tk()

class Telas():
    def telaLoja(self):
        self.frame2.place_forget()
        self.frame3.place_forget()
        self.frame4.place_forget()
        self.frame1.place(relwidth=1, relheight=1)

    def telaPiso(self):
        self.frame1.place_forget()
        self.frame3.place_forget()
        self.frame4.place_forget()
        self.frame2.place(relwidth=1, relheight=1)

    def telaMadeira(self):
        self.frame1.place_forget()
        self.frame2.place_forget()
        self.frame4.place_forget()
        self.frame3.place(relwidth=1, relheight=1)

    def telaPortasX(self):
        self.frame1.place_forget()
        self.frame2.place_forget()
        self.frame3.place_forget()
        self.frame4.place(relwidth=1, relheight=1)

    def voltar(self):
        self.frame1.place_forget()
        self.frame2.place_forget()
        self.frame3.place_forget()
        self.frame4.place_forget()

class Application(Telas):
    def __init__(self):
        print("rodei")
        self.Janela = Janela
        self.telaPrincipal()
        self.telasAdc()
        Janela.mainloop()
       
    def telaPrincipal(self):
        # Tela Principal
        self.Janela.title("Produtos")
        self.Janela.configure(background= "#e6e6e6")
        self.Janela.state("zoomed")
        self.Janela.resizable(True, True)
        self.Janela.maxsize(width= 1366, height= 768)
        self.Janela.minsize(width=1240, height=600)

    def telasAdc(self):
        # Estrutura da Tela Principal
        self.lbl = Label(Janela, text="Tela Principal")
        self.btnLoja = Button(font = ('calibri', 14), text="Loja", bd=0, bg="#07A0C3", fg="#fff", command=self.telaLoja,
                activebackground='#086788', activeforeground="white").pack()

        self.btnPisos = Button(font = ('calibri', 14), text="Pisos", bd=0, bg="#07A0C3", fg="#fff", command=self.telaPiso,
            activebackground='#086788', activeforeground="white").pack()

        self.btnMadeira = Button(font = ('calibri', 14), text="Madeira", bd=0, bg="#07A0C3", fg="#fff", command=self.telaMadeira,
            activebackground='#086788', activeforeground="white").pack()

        self.btnPortasX = Button(font = ('calibri', 14), text="Portas especiais", bd=0, bg="#07A0C3", fg="#fff", command=self.telaPortasX,
            activebackground='#086788', activeforeground="white").pack()
            
        # ----------------------------------------------------
        # Criando As Telas

        self.frame1 = Frame(Janela, bg="blue" )
        self.btnBack1 = Button(self.frame1, text="Voltar", command=self.voltar).pack()

        self.frame2 = Frame(Janela, bg="black")
        self.btnBack2 = Button(self.frame2, text="Voltar", command=self.voltar).pack()

        self.frame3 = Frame(Janela, bg="green")
        self.btnBack3 = Button(self.frame3, text="Voltar", command=self.voltar).pack()

        self.frame4 = Frame(Janela, bg="red")
        self.btnBack4 = Button(self.frame4, text="Voltar", command=self.voltar).pack()

Application()