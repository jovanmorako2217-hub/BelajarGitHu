import tkinter as tk
from tkinter import ttk,messagebox

window = tk.Tk()
window.configure(bg = "mistyrose")
window.state("zoomed")
window.resizable(True,True)
window.title ("KALKULATOR PENGELUARAN BULANAN")

style = ttk.Style()
style.theme_use ("default")
style.configure("TFrame", background="mistyrose")

style.configure("TLabel", background="mistyrose", foreground="#1F2F3A", 
                font = ("Dejavu Sans Mono",13,"bold"),
                padding = 3)

style.configure("TButton",
                font = ("Dejavu Sans Mono", 13, "bold"),
                background="#6E8FA3", foreground="white", padding = 3)

style.configure("TEntry", fieldbackground="white", foreground="#1F2F3A", padding = 3)

judul = ttk.Label(window,
                  text = "KALKULATOR PENGELUARAN BULANAN",
                  font = ("Segoe UI", 15, "bold"), foreground="black")

style.map("TEntry",
          fieldbackground=[("readonly", "white")], #agar Tentry sisa uang & jumlah pengeluaran warnanya putih
          foreground=[("readonly", "#1F2F3A")])

judul.pack(pady = 20)

#DATA
listdata = []

#KOLOM
inputframe1 = ttk.Frame(window) #FRAME INPUT
inputframe1.pack(padx= 10, pady= 2, fill = "x")

jumlahuang_label = ttk.Label(inputframe1, text= "Masukan Jumlah Uang Anda Sekarang 💰")
jumlahuang_label.pack(padx=10, pady=2, fill = "x")

jumlahuang = tk.StringVar()
jumlahuang_entry = ttk.Entry (inputframe1, textvariable =jumlahuang)
jumlahuang_entry.pack(padx=10, pady= 2, fill = "x")

#KOLOM 2 INPUT PENGELUARAN
inputframe2 = ttk.Frame(window)
inputframe2.pack(padx=10, pady=10, fill = "x")

pengeluaran_label = ttk.Label(inputframe2, text= "Pengeluaran anda") #LABEL JUMLAH UANG
pengeluaran_label.pack(padx=10, pady=10, fill = "x")

jumlahpengeluaran = tk.StringVar()
inputframe2 = ttk.Entry (inputframe2, textvariable= jumlahpengeluaran)
inputframe2.pack(padx=10, pady=2, fill = "x")

inputframe3 = ttk.Frame(window) #FRAME INPUT
inputframe3.pack(padx=10,pady=10, fill = "x")

listbox = tk.Listbox (inputframe3, height= 8)
listbox.pack(side="left", fill="x", expand=True, padx=(10,0), pady=5)

scroll = ttk.Scrollbar(inputframe3, orient = "vertical", command= listbox.yview)
scroll.pack(side= "right", fill= "y", padx=(0,10), pady=5)

listbox.config(yscrollcommand= scroll.set)

inputframe6=ttk.Frame(window)
inputframe6.pack(padx=10, pady=10, fill = "x")

inputframe6_label = ttk.Label (inputframe6, text= "Sisa Uang Bulan Ini")
inputframe6_label.pack(padx=10, pady=5, fill = "x")

sisa= tk.StringVar()
inputframe6_entry= ttk.Entry(inputframe6, textvariable= sisa, state= "readonly")#readonly tidak bisa di ketik/ubah tapi bisa menampilkan
inputframe6_entry.pack(padx=10, pady=5, fill= "x")

inputframe5=ttk.Frame(window)
inputframe5.pack(padx=10, pady=10, fill = "x")

inputframe5_label=ttk.Label(inputframe5, text='Jumlah Pengeluaran Anda Bulan Ini')
inputframe5_label.pack(padx=10, pady=2, fill = "x")

hitung= tk.StringVar()
inputframe5_entry= ttk.Entry(inputframe5,textvariable=hitung, state= "readonly")
inputframe5_entry.pack(padx=10, pady=10, fill = "x")

#BUTTON
def tampildata():
    listbox.delete(0,tk.END)
    for i, data in enumerate(listdata):
        listbox.insert(tk.END, f"{i+1}. Rp {data}")
    

def tambahpengeluaran():
    try:
        nilai=int(jumlahpengeluaran.get())
        listdata.append(nilai)
        tampildata()
        jumlahpengeluaran.set("")
        sisauang()
    except:
        messagebox.showerror("PERINGATAN","\tMasukkan angka! \n----------------------------------------------- \nJangan masukkan input selain angka!")

def updatepengeluaran():
    try:
        index=listbox.curselection()[0]
        nilaiint=int(jumlahpengeluaran.get())
        listdata[index]=nilaiint
        tampildata()
        jumlahpengeluaran.set("")
        sisauang()
    except:
        messagebox.showwarning('PERINGATAN', 'Pilih data dan masukkan angka!')

def hapuspengeluaran():
    try:
        index=listbox.curselection()[0]
        listdata.pop(index)
        tampildata()
        sisauang()
    except:
        messagebox.showwarning('PERINGATAN','Anda belum memilih data! \nPilih data yang ingin dihapus')

def hitungtotal():
    total= sum(listdata)
    hitung.set(f"Rp{total:,}".replace(',','.'))

def sisauang():
    try:
        uangawal1= int(jumlahuang.get()) 
        totalpengeluaran= sum(listdata)
        uangakhir= uangawal1-totalpengeluaran
        sisa.set(f"Rp{uangakhir:,}".replace(',','.')) #tdk bs langsung titik, krn bawaan python adl koma
    except:
        messagebox.showwarning('Peringatan!','Masukkan Jumlah Uang Anda!')

inputframe4=ttk.Frame(window) #frame input
inputframe4.pack(padx=10,pady=10,fill='x')

tombol1=ttk.Button(inputframe4, text='Tambah Pengeluaran', command=tambahpengeluaran)
tombol1.pack(padx=10,pady=10,side='left')

tombol2=ttk.Button(inputframe4,text='Update Pengeluaran',command=updatepengeluaran)
tombol2.pack(padx=10,pady=10, side='left')

tombol3=ttk.Button(inputframe4, text='Hapus Pengeluaran', command=hapuspengeluaran)
tombol3.pack(padx=10,pady=10, side='left')

tombol4=ttk.Button(inputframe4, text='Hitung Total Pengeluaran',command=hitungtotal)
tombol4.pack(padx=10, pady=10, side="left")               
                  
window.mainloop()

















