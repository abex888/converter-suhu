#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

#Deskripsi
deskripsi='''PROGRAM KONVERSI SUHU
Pembuat		: Aries Aprilian (abex888@gmail.com)
Versi		: 1.0.1
Lisensi		: GNU GPL versi 2
Program ini dibuat dengan python3 menggunakan modul Tkinter
untuk GUI

CARA KERJA:
Program ini menyimpan nilai suhu pada variable t. Kemudian
suhu tersebut dikonversikan ke masing-masing skala'''


#########################
###FUNGSI DAN CLASS######
#########################

class tentang():
	def __init__(self, event=None):
				
		self.jendela_tentang = Toplevel()
		self.jendela_tentang.title('About')
		self.jendela_tentang.resizable(0,0)
		
		self.frame_deskripsi=Frame(self.jendela_tentang, bd=3, bg='white', relief=SUNKEN)
		self.frame_deskripsi.pack()
		
		self.label_deskripsi = Label(self.frame_deskripsi, text='', bg='white', fg='black', justify=LEFT)
		self.label_deskripsi.config(text=deskripsi)
		self.label_deskripsi.pack()			
				
		self.q = Button(self.jendela_tentang, text='Tutup')
		self.q.pack()
		self.q.bind('<Button-1>', lambda kaluar: self.jendela_tentang.destroy())
		self.jendela_tentang.bind('<Button-3>',lambda kaluar: self.jendela_tentang.destroy())
		self.jendela_tentang.bind('<Escape>',lambda kaluar: self.jendela_tentang.destroy())

def etang(event):
	source = skala.get()
	t = awal.get()
	#print(h)
	
	#Perhitungan konversi dari skala asal ke celsius
	if source == 'Celsius':
		celsius = t
	elif source == 'Fahrenheit':
		celsius=(t-32)*(5/9)
	elif source == 'Kelvin':
		celsius=(t-273.15)
	elif source == 'Rankine':
		celsius=(t-491.67)*(5/9)
	elif source == 'Delisle':
		celsius=100-t*(2/3)
	elif source == 'Newton':
		celsius=t*(100/33)
	elif source == 'Reamur':
		celsius=t*(5/4)
	elif source == 'Romer':
		celsius=(t-7.5)*(40/21)

	#Perhitungan konversi dari celsius ke tiap-tiap skala
	celsius = celsius
	fahrenheit = celsius*(9/5)+32
	kelvin = celsius+273.15
	rankine = (celsius+273.15)*(9/5)
	delisle = (100-celsius)*(3/2)
	newton = celsius*(33/100)
	reamur = celsius*(4/5)
	romer = celsius*(21/40)+7.5
	
	
	hasil_celsius.set('{:.2f}'.format(celsius))
	hasil_fahrenheit.set('{:.2f}'.format(fahrenheit))
	hasil_kelvin.set('{:.2f}'.format(kelvin))
	hasil_rankine.set('{:.2f}'.format(rankine))
	hasil_delisle.set('{:.2f}'.format(delisle))
	hasil_newton.set('{:.2f}'.format(newton))
	hasil_reamur.set('{:.2f}'.format(reamur))
	hasil_romer.set('{:.2f}'.format(romer))
		
	

def kaluar(event):
	print('PROGRAM KELUAR')
	print('TERIMA KASIH')
	root.destroy()

def ulang(event):
	awal.set(0)
	skala.set('Celsius')
	hasil_celsius.set('')
	hasil_fahrenheit.set('')
	hasil_kelvin.set('')
	hasil_rankine.set('')
	hasil_delisle.set('')
	hasil_newton.set('')
	hasil_reamur.set('')
	hasil_romer.set('')




###########################################
###JENDELA UTAMA###########################
###########################################

root = Tk()
root.title('KONVERSI SUHU')
root.resizable(0,0)
nilai = Frame(root, bd=3, relief=RIDGE)
laporan = Frame(root, bd=3, relief=SUNKEN)


#DEKLARASI VARIABEL
awal = DoubleVar()
skala = StringVar()
hasil_celsius = StringVar()
hasil_fahrenheit = StringVar()
hasil_kelvin = StringVar()
hasil_rankine = StringVar()
hasil_delisle = StringVar()
hasil_newton = StringVar()
hasil_reamur = StringVar()
hasil_romer = StringVar()

#dictionary
pilihan = {'Celsius','Fahrenheit','Kelvin','Rankine','Delisle','Newton','Reamur','Romer'}
skala.set('Celsius')

#widget milik root
judul_utama = Label(root, text='KONVERSI SUHU')
judul_utama.configure(font='serif 23 bold')
judul_utama.grid(row=0, column=0, columnspan=3)
Label(root, text='F1 untuk deskripsi program').grid(row=4, column=0, sticky='w')
Label(root, text='F4 untuk keluar').grid(row=5, column=0, sticky='w')
reset = Button(root, text='Reset')
reset.grid(row=4, column=1, sticky='we', rowspan=2)
#tombol_tentang = Button(root, text='Tentang')
#tombol_tentang.grid(row=4, column=1, sticky='we')
keluar = Button(root, text='Keluar')
keluar.grid(row=4, column=2, sticky='we', rowspan=2)



#widget milik frame nilai
Label(nilai, text='Masukan Nilai Awal:').grid(row=0, column=0, columnspan=3, sticky='we')
nilai_awal = Entry(nilai, textvariable=awal, width=5, justify=RIGHT)
nilai_awal.grid(row=1, column=1, sticky='e')
nilai_awal.focus()
skala_awal = OptionMenu(nilai, skala, *pilihan)
skala_awal.focus
skala_awal.grid(row=1, column=0, sticky='e')
hitung = Button(nilai, text='Hitung')
hitung.grid(row=1, column=2, sticky='e')

#widget milik frame laporan
Label(laporan, text='1. Celsius').grid(row=0, column=0, sticky='w')
Label(laporan, text='2. Fahrenheit').grid(row=1, column=0, sticky='w')
Label(laporan, text='3. Kelvin').grid(row=2, column=0, sticky='w')
Label(laporan, text='4. Rankine').grid(row=3, column=0, sticky='w')

Label(laporan, text=':').grid(row=0, column=1, sticky='w')
Label(laporan, text=':').grid(row=1, column=1, sticky='w')
Label(laporan, text=':').grid(row=2, column=1, sticky='w')
Label(laporan, text=':').grid(row=3, column=1, sticky='w')

Label(laporan, text='5. Delisle').grid(row=0, column=3, sticky='w')
Label(laporan, text='6. Newton').grid(row=1, column=3, sticky='w')
Label(laporan, text='7. Reamur').grid(row=2, column=3, sticky='w')
Label(laporan, text='8. Romer').grid(row=3, column=3, sticky='w')

Label(laporan, text=':').grid(row=0, column=4, sticky='w')
Label(laporan, text=':').grid(row=1, column=4, sticky='w')
Label(laporan, text=':').grid(row=2, column=4, sticky='w')
Label(laporan, text=':').grid(row=3, column=4, sticky='w')

celsius = Label(laporan, textvariable=hasil_celsius, width=6, justify=LEFT, foreground='blue')
celsius.grid(row=0, column=2, sticky='w')
fahrenheit = Label(laporan, textvariable=hasil_fahrenheit, width=6, justify=LEFT, foreground='blue')
fahrenheit.grid(row=1, column=2, sticky='w')
kelvin = Label(laporan, textvariable=hasil_kelvin, width=6, justify=LEFT, foreground='blue')
kelvin.grid(row=2, column=2, sticky='w')
rankine = Label(laporan, textvariable=hasil_rankine, width=6, justify=LEFT, foreground='blue')
rankine.grid(row=3, column=2, sticky='w')

delisle = Label(laporan, textvariable=hasil_delisle, width=6, justify=LEFT, foreground='blue')
delisle.grid(row=0, column=5, sticky='w')
newton = Label(laporan, textvariable=hasil_newton, width=6, justify=LEFT, foreground='blue')
newton.grid(row=1, column=5, sticky='w')
reamur = Label(laporan, textvariable=hasil_reamur, width=6, justify=LEFT, foreground='blue')
reamur.grid(row=2, column=5, sticky='w')
romer = Label(laporan, textvariable=hasil_romer, width=6, justify=LEFT, foreground='blue')
romer.grid(row=3, column=5, sticky='w')

#BINDING
hitung.bind('<Button-1>', etang)
keluar.bind('<Button-1>', kaluar)
root.bind('<F4>', kaluar)
reset.bind('<Button-1>', ulang)
root.bind('<F1>', tentang)
root.bind('<Return>', etang)

#Layout frame
nilai.grid(row=1, column=0, columnspan=3)
laporan.grid(row=2, column=0, columnspan=3)

#Loop Utama
root.mainloop()
