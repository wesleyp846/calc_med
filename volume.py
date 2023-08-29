from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

co1 = "#feffff" #white
co2 = "#111212" #black
co3 = "#38576b" #value
fundo = "#38576b" #cor de fundo

janela = Tk()
janela.title("")
janela.geometry("400x200")
janela.configure(bg=fundo)

style = ttk.Style(janela)
style.theme_use("clam")

# PRIMEIRA LINHA
frame_logo = Frame(janela, width=400, height=56, bg=fundo, pady=0, padx=0, relief="flat")
frame_logo.grid(row=0, column=0, sticky="nw")

#SEGUNDA LINHA
frame_resultado = Frame(janela, width=400, height=150, bg=fundo, pady=0, padx=0, relief="flat")
frame_resultado.grid(row=1, column=0, sticky="nw")

# (PRIMEIRA LINHA)LINHA DO TÍTULO E LOGOTIPO
app_lg = Image.open("bandeiraBrasil.png")
app_lg = app_lg.resize((40,40))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Calculadora de Medidas", width=850, compound="left", anchor="nw", font=("Verdana 15"), bg=fundo, fg=co2)
app_logo.place(x=5, y=0)

# (SEGUNDA LINHA) CAIXA DE INPUT NA INTERFACE GRÁFICA
value_text = StringVar
############ Entry pra input's
entry_raio = Entry(frame_resultado, textvariable=value_text, width=10, font=("Tahoma 25 bold"), justify="center")
entry_raio.place(x=10, y=0)

# RESULTADO
############## Label para print's na tela
label_esfera = Label(frame_resultado, text="1000", width=850, compound="left", anchor="nw", font=("Calibre 12"), bg=fundo, fg=co2)
label_esfera.place(x=10, y=70)

label_cubo = Label(frame_resultado, text="1000", width=850, compound="left", anchor="nw", font=("Calibre 12"), bg=fundo, fg=co2)
label_cubo.place(x=10, y=90)


janela.mainloop()