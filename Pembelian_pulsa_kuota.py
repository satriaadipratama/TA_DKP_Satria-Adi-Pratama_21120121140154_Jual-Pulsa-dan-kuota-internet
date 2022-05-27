from ctypes import resize
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.messagebox import showerror
from abc import ABC
from turtle import bgcolor


class P(ABC):
    ask = None
class Pertanyaan(P):

    def __init__(self,ask):
        self.ask = ask

    def setAsk(self, ask):
        self.ask = ask
        pass

    def getAsk(self):
        return self.ask

p1=Pertanyaan("Apakah ingin membeli?")

def on_click():
    nomor = entry.get()
    try:
       nomor = int(nomor)
    except ValueError:
        showerror('Error', 'Bukan Angka')
    else:
        if nomor == 1:
            telkomsel = Button(window, text = "1 GB/7 Hari Rp20.000  " , command = on_dblclick)
            telkomsel2 = Button(window, text = "2 GB/7 Hari Rp25.000  " , command = on_dblclick)
            telkomsel3 = Button(window, text = "4 GB/7 Hari Rp40.000  " , command = on_dblclick)
            telkomsel4 = Button(window, text = "5 GB/30 Hari Rp60.000" , command = on_dblclick)
            telkomsel5 = Button(window, text = "6 GB/30 Hari Rp70.000" , command = on_dblclick)
            telkomsel6 = Button(window, text = "Pulsa 20000 Rp22.000" , command = on_dblclick)
            telkomsel7 = Button(window, text = "Pulsa 30000 Rp32.000" , command = on_dblclick)
            telkomsel8 = Button(window, text = "Pulsa 40000 Rp42.000" , command = on_dblclick)
            telkomsel9 = Button(window, text = "Pulsa 50000 Rp52.000" , command = on_dblclick)
            telkomsel10 = Button(window, text = "Pulsa 60000 Rp62.000" , command = on_dblclick)
            telkomsel.place(x=90,y=380)
            telkomsel2.place(x=90,y=407)
            telkomsel3.place(x=90,y=434)
            telkomsel4.place(x=90,y=461)
            telkomsel5.place(x=90,y=488)
            telkomsel6.place(x=262,y=380)
            telkomsel7.place(x=262,y=407)
            telkomsel8.place(x=262,y=434)
            telkomsel9.place(x=262,y=461)
            telkomsel10.place(x=262,y=488)
        elif nomor == 2:
            indosat = Button(window, text = "2 GB/7 Hari Rp15.000  " , command = on_dblclick)
            indosat2 = Button(window, text = "3 GB/7 Hari Rp20.000  " , command = on_dblclick)
            indosat3 = Button(window, text = "4 GB/7 Hari Rp25.000  " , command = on_dblclick)
            indosat4 = Button(window, text = "5 GB/30 Hari Rp40.000" , command = on_dblclick)
            indosat5 = Button(window, text = "6 GB/30 Hari Rp60.000" , command = on_dblclick)
            indosat6 = Button(window, text = "Pulsa 20000 Rp22.000" , command = on_dblclick)
            indosat7 = Button(window, text = "Pulsa 30000 Rp32.000" , command = on_dblclick)
            indosat8 = Button(window, text = "Pulsa 40000 Rp42.000" , command = on_dblclick)
            indosat9 = Button(window, text = "Pulsa 50000 Rp52.000" , command = on_dblclick)
            indosat10 = Button(window, text = "Pulsa 60000 Rp62.000" , command = on_dblclick)
            indosat.place(x=90,y=380)
            indosat2.place(x=90,y=407)
            indosat3.place(x=90,y=434)
            indosat4.place(x=90,y=461)
            indosat5.place(x=90,y=488)
            indosat6.place(x=262,y=380)
            indosat7.place(x=262,y=407)
            indosat8.place(x=262,y=434)
            indosat9.place(x=262,y=461)
            indosat10.place(x=262,y=488)
        elif nomor == 3:
            XL = Button(window, text = "2 GB/7 Hari Rp10.000  " , command = on_dblclick)
            XL2 = Button(window, text = "3 GB/7 Hari Rp15.000  " , command = on_dblclick)
            XL3 = Button(window, text = "4 GB/7 Hari Rp20.000  " , command = on_dblclick)
            XL4 = Button(window, text = "5 GB/30 Hari Rp40.000" , command = on_dblclick)
            XL5 = Button(window, text = "6 GB/30 Hari Rp60.000" , command = on_dblclick)
            XL6 = Button(window, text = "Pulsa 20000 Rp22.000" , command = on_dblclick)
            XL7 = Button(window, text = "Pulsa 30000 Rp32.000" , command = on_dblclick)
            XL8 = Button(window, text = "Pulsa 40000 Rp42.000" , command = on_dblclick)
            XL9 = Button(window, text = "Pulsa 50000 Rp52.000" , command = on_dblclick)
            XL10 = Button(window, text = "Pulsa 60000 Rp62.000" , command = on_dblclick)
            XL.place(x=90,y=380)
            XL2.place(x=90,y=407)
            XL3.place(x=90,y=434)
            XL4.place(x=90,y=461)
            XL5.place(x=90,y=488)
            XL6.place(x=262,y=380)
            XL7.place(x=262,y=407)
            XL8.place(x=262,y=434)
            XL9.place(x=262,y=461)
            XL10.place(x=262,y=488)
        elif nomor == 4: 
            Tri = Button(window, text = "2 GB/7 Hari Rp5.000  " , command = on_dblclick)
            Tri2 = Button(window, text = "3 GB/7 Hari Rp10.000  " , command = on_dblclick)
            Tri3 = Button(window, text = "4 GB/7 Hari Rp15.000  " , command = on_dblclick)
            Tri4 = Button(window, text = "5 GB/30 Hari Rp35.000" , command = on_dblclick)
            Tri5 = Button(window, text = "6 GB/30 Hari Rp55.000" , command = on_dblclick)
            Tri6 = Button(window, text = "Pulsa 20000 Rp22.000" , command = on_dblclick)
            Tri7 = Button(window, text = "Pulsa 30000 Rp32.000" , command = on_dblclick)
            Tri8 = Button(window, text = "Pulsa 40000 Rp42.000" , command = on_dblclick)
            Tri9 = Button(window, text = "Pulsa 50000 Rp52.000" , command = on_dblclick)
            Tri10 = Button(window, text = "Pulsa 60000 Rp62.000" , command = on_dblclick)
            Tri.place(x=90,y=380)
            Tri2.place(x=90,y=407)
            Tri3.place(x=90,y=434)
            Tri4.place(x=90,y=461)
            Tri5.place(x=90,y=488)
            Tri6.place(x=262,y=380)
            Tri7.place(x=262,y=407)
            Tri8.place(x=262,y=434)
            Tri9.place(x=262,y=461)
            Tri10.place(x=262,y=488)
        
def on_dblclick():
    print(askquestion("Menu", (p1.getAsk())))

window = Tk()

window.geometry("480x540")
window.title("Toko Internet")
window.resizable(width = 0, height = 0)
window.configure(bg="blue")
Label(window,text="Tekkom.net",font="impack 13 bold",bg="yellow").pack(fill=X)

labelnama = Label(window,
                  text = "Nama\t:",
                  font = ("times new roman", 13, )).place(x=50, y=30)

labelnomor = Label(window,
                  text = "Nomor\t:",
                  font = ("times new roman", 13)).place(x=50, y=60)


labelprovider = Label(window, 
                    text = "Provider Yang Tersedia\n1.Telkomsel\n2.Indosat\n3.XL\n4.Tri",
                    font = ("times new roman", 13))
labelprovider.pack(pady=100)   

labelpilihan = Label(window, 
                    text = "Provider\t:",
                    font = ("times new roman", 13))
labelpilihan.place(x=50,y=325)   

strnama = StringVar()
entrynama = Entry(window,
                  textvariable = strnama,
                  font = ("times new roman", 11)).place(x=150, y=32)

strnomor = StringVar()
entrynomor = Entry(window,
                  textvariable = strnomor,
                  font = ("times new roman", 11)).place(x=150, y=65)           

entry = Entry(window)
entry.pack(pady=3)

btn = Button(window, text = "Pilih", bg= "yellow", font= "impack 10 bold", command = on_click)
btn.pack(pady=5)

window.mainloop()








