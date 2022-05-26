from ctypes import resize
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.messagebox import showerror
from abc import ABC

#modul 1 ada(variabel)
#modul 2 ada (if)
#modul 3 belum ada (while)
#modul 4 ada (function = def)
#modul 5 ada (class & inheritance)
#modul 6 ada (getter setter)
#modul 7 belum ada (stack & queue)
#modul 8 ada (GUI)

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
            telkomsel.place(x=90,y=325)
            telkomsel2.place(x=90,y=352)
            telkomsel3.place(x=90,y=379)
            telkomsel4.place(x=90,y=406)
            telkomsel5.place(x=90,y=433)
            telkomsel6.place(x=233,y=325)
            telkomsel7.place(x=233,y=352)
            telkomsel8.place(x=233,y=379)
            telkomsel9.place(x=233,y=406)
            telkomsel10.place(x=233,y=433)
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
            indosat.place(x=105,y=325)
            indosat2.place(x=105,y=352)
            indosat3.place(x=105,y=379)
            indosat4.place(x=105,y=406)
            indosat5.place(x=105,y=433)
            indosat6.place(x=250,y=325)
            indosat7.place(x=250,y=352)
            indosat8.place(x=250,y=379)
            indosat9.place(x=250,y=406)
            indosat10.place(x=250,y=433)
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
            XL.place(x=105,y=325)
            XL2.place(x=105,y=352)
            XL3.place(x=105,y=379)
            XL4.place(x=105,y=406)
            XL5.place(x=105,y=433)
            XL6.place(x=250,y=325)
            XL7.place(x=250,y=352)
            XL8.place(x=250,y=379)
            XL9.place(x=250,y=406)
            XL10.place(x=250,y=433)

        
def on_dblclick():
    print(askquestion("Menu", (p1.getAsk())))

window = Tk()

window.geometry("450x480")
window.title("Toko Internet")
window.resizable(width = 0, height = 0)

labelnama = Label(window,
                  text = "Nama\t:",
                  font = ("times new roman", 13)).place(x=50, y=20)

labelnomor = Label(window,
                  text = "Nomor\t:",
                  font = ("times new roman", 13)).place(x=50, y=50)


labelprovider = Label(window, 
                    text = "Provider Yang Tersedia\n1.Telkomsel\n2.Indosat\n3.XL",
                    font = ("times new roman", 13))
labelprovider.pack(pady=90)   

labelpilihan = Label(window, 
                    text = "Provider\t:",
                    font = ("times new roman", 13))
labelpilihan.place(x=60,y=260)   

strnama = StringVar()
entrynama = Entry(window,
                  textvariable = strnama,
                  font = ("times new roman", 11)).place(x=150, y=22)

strnomor = StringVar()
entrynomor = Entry(window,
                  textvariable = strnomor,
                  font = ("times new roman", 11)).place(x=150, y=55)           

entry = Entry(window)
entry.pack(pady=3)

btn = Button(window, text = "Pilih", command = on_click)
btn.pack(pady=5)

window.mainloop()