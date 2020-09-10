"""
App de escritorio - Pedidos
Comando para convertir en ejecutable: pyinstaller --windowed --onedir --icon=./images.ico viejo_caballito.py
"""
import tkinter as tk
from tkinter import messagebox, ttk
import os, time
import xlwings as xw
from openpyxl import Workbook, load_workbook

empanadas_de_carne = []
empanadas_de_pollo = []
empanadas_de_jq = []
empanadas_de_verduda = []


def comprobar_archivo():
    existe = os.path.exists('Ventas.xlsx')
    if existe:
        wb = load_workbook(filename='Ventas.xlsx')
        ws = wb.active
        print('Apertura exitosa del archivo.')
    else:
        wb = Workbook()
        ws = wb.active
        titulo = ('Hora transacción',"Emp. Carne", 'Emp. Pollo', 'Emp. JQ', 'Emp. Verdura', 'Emp. CQ', 'Tar. JQ', 'Tar. Puerro', 'Tar. Beren.', 'Tar. Acelga', 'Tar. Calab.', 'Tar. Zapa.','Platos','Tortilla','Fruta','Cafe','Alfajores','Medialunas','Ensa. Fruta','Gaseosa','Total')
        ws.append(titulo)
        wb.save(filename='Ventas.xlsx')
        print('Creación exitosa del archivo')


def guardar_datos(pedido):
    wb = load_workbook(filename='Ventas.xlsx')
    wb.active.append(pedido)
    wb.save('Ventas.xlsx')    
    print("Carga exitosa de la venta!!")


def lista_productos():
    pedido.delete(0, tk.END)
    c = len(empanadas_de_carne)
    pedido.insert('0',c)
    

def confirmar():
    m = messagebox.askokcancel(title='Confirmación', message='Desea confirmar el pedido?')
    if m:
        texto_carne.delete(0,tk.END)
        texto_pollo.delete(0,tk.END)
        texto_jq.delete(0,tk.END)
        texto_verdura.delete(0,tk.END)
        texto_cq.delete(0,tk.END)
        texto_tar_jq.delete(0,tk.END)
        texto_tar_puerro.delete(0,tk.END)
        texto_tar_beren.delete(0,tk.END)
        texto_tar_acelga.delete(0,tk.END)
        texto_tar_cala.delete(0,tk.END)
        texto_tar_zapa.delete(0,tk.END)

        facturacion.delete(0,tk.END)
        paga_con.delete(0,tk.END)
        vuelto.delete(0,tk.END)
    else:
        pass


def cancelar():
    m = messagebox.askokcancel(title='Cancelación', message='Desea cancelar el pedido?')
    if m:
        texto_carne.delete(0,tk.END)
        texto_pollo.delete(0,tk.END)
        texto_jq.delete(0,tk.END)
        texto_verdura.delete(0,tk.END)
        texto_cq.delete(0,tk.END)
        texto_tar_jq.delete(0,tk.END)
        texto_tar_puerro.delete(0,tk.END)
        texto_tar_beren.delete(0,tk.END)
        texto_tar_acelga.delete(0,tk.END)
        texto_tar_cala.delete(0,tk.END)
        texto_tar_zapa.delete(0,tk.END)

        facturacion.delete(0,tk.END)
        paga_con.delete(0,tk.END)
        vuelto.delete(0,tk.END)
    else:
        pass


def suma():
    hora = time.asctime()        
    if facturacion.get() == '':
        precio_empanada = float(60)
        try:
            carne = int(texto_carne.get())
        except:
            if texto_carne.get() == '':
                carne = int(0)
            else: 
                messagebox.showinfo(title='Error', message='Ingrese un numero valido.')
        try:
            pollo = int(texto_pollo.get())
        except:
            if texto_pollo.get() == '':
                pollo = int(0)
            else: 
                messagebox.showinfo(title='Error', message='Ingrese un numero valido.')
        try:
            jq = int(texto_jq.get())
        except:
            if texto_jq.get() == '':
                jq = int(0)
            else: 
                messagebox.showinfo(title='Error', message='Ingrese un numero valido.')
        try:
            ver = int(texto_verdura.get())
        except:
            if texto_verdura.get() == '':
                ver = int(0)
            else: 
                messagebox.showinfo(title='Error', message='Ingrese un numero valido.')
        
        total_empa = (carne+pollo+jq+ver) * precio_empanada
        facturacion.insert("0", total_empa)
    else:
        facturacion.delete(0,tk.END)
        precio_empanada = float(60)
        try:
            carne = int(texto_carne.get())
        except:
            if texto_carne.get() == '':
                carne = int(0)
            else: 
                messagebox.showinfo(title='Error', message='Ingrese un numero valido.')
        try:
            pollo = int(texto_pollo.get())
        except:
            if texto_pollo.get() == '':
                pollo = int(0)
            else: 
                messagebox.showinfo(title='Error', message='Ingrese un numero valido.')
        try:
            jq = int(texto_jq.get())
        except:
            if texto_jq.get() == '':
                jq = int(0)
            else: 
                messagebox.showinfo(title='Error', message='Ingrese un numero valido.')
        try:
            ver = int(texto_verdura.get())
        except:
            if texto_verdura.get() == '':
                ver = int(0)
            else: 
                messagebox.showinfo(title='Error', message='Ingrese un numero valido.')
        
        total_empa = (carne+pollo+jq+ver) * precio_empanada
        facturacion.insert("0", total_empa)

    empanadas_de_carne.append(carne)
    empanadas_de_jq.append(jq)
    empanadas_de_pollo.append(pollo)
    empanadas_de_verduda.append(ver)
    al_excel = [hora, carne, jq, pollo, ver, total_empa]
    guardar_datos(al_excel)
    lista_productos()

def fun_vuelto():    
    if vuelto.get() == '':
        if (float(facturacion.get()) > 0) & (float(paga_con.get()) >0):
            v = float(paga_con.get()) - float(facturacion.get())
            vuelto.insert('0', v)
        else:
            if float(paga_con.get() == '') | float(paga_con.get() == '0'):
                vuelto.insert('0', 0)
            else:
                messagebox.showinfo(title='Error', message='Ingrese montos de vuelto o facturación válidos.')
    else:
        vuelto.delete(0,tk.END)
        if (float(facturacion.get()) > 0) & (float(paga_con.get()) >0):
            v = float(paga_con.get()) - float(facturacion.get())
            vuelto.insert('0', v)
        else:
            if float(paga_con.get() == '') | float(paga_con.get() == '0'):
                vuelto.insert('0', 0)
            else:
                messagebox.showinfo(title='Error', message='Ingrese montos de vuelto o facturación válidos.')

### EXCEL INICIAL
comprobar_archivo()

### APP DE ESCRITORIO
ventana = tk.Tk()
ventana.config(height=540, width=870)
ventana.title("Aplicación de ventas - Viejo Caballito Bar")

## CAJAS
# CAJAS EMPANADAS Y TARTAS
pedido = ttk.Entry()
pedido.place(x=150, y=10,width=40)
pedido.insert(tk.END, '1')
texto_carne = ttk.Entry()
texto_carne.place(x=300, y=75)
texto_carne.insert(tk.END,"")
texto_pollo = ttk.Entry()
texto_pollo.place(x=300, y=100)
texto_pollo.insert(tk.END,"")
texto_jq = ttk.Entry()
texto_jq.place(x=300, y=125)
texto_jq.insert(tk.END,"")
texto_verdura = ttk.Entry()
texto_verdura.place(x=300, y=150)
texto_verdura.insert(tk.END,"")
texto_cq = ttk.Entry()
texto_cq.place(x=300, y=175)
texto_cq.insert(tk.END,"")
texto_tar_jq = ttk.Entry()
texto_tar_jq.place(x=300, y=200)
texto_tar_jq.insert(tk.END,"")
texto_tar_puerro = ttk.Entry()
texto_tar_puerro.place(x=300, y=225)
texto_tar_puerro.insert(tk.END,"")
texto_tar_beren = ttk.Entry()
texto_tar_beren.place(x=300, y=250)
texto_tar_beren.insert(tk.END,"")
texto_tar_acelga = ttk.Entry()
texto_tar_acelga.place(x=300, y=275)
texto_tar_acelga.insert(tk.END,"")
texto_tar_cala = ttk.Entry()
texto_tar_cala.place(x=300, y=300)
texto_tar_cala.insert(tk.END,"")
texto_tar_zapa = ttk.Entry()
texto_tar_zapa.place(x=300, y=325)
texto_tar_zapa.insert(tk.END,"")
# CAJAS OTROS
texto_menu = ttk.Entry()
texto_menu.place(x=700, y=75)
texto_menu.insert(tk.END,"")
texto_tortilla = ttk.Entry()
texto_tortilla.place(x=700, y=100)
texto_tortilla.insert(tk.END,"")
texto_fruta = ttk.Entry()
texto_fruta.place(x=700, y=125)
texto_fruta.insert(tk.END,"")
texto_cafe = ttk.Entry()
texto_cafe.place(x=700, y=150)
texto_cafe.insert(tk.END,"")
texto_alfa = ttk.Entry()
texto_alfa.place(x=700, y=175)
texto_alfa.insert(tk.END,"")
texto_media = ttk.Entry()
texto_media.place(x=700, y=200)
texto_media.insert(tk.END,"")
texto_ensa_fru = ttk.Entry()
texto_ensa_fru.place(x=700, y=225)
texto_ensa_fru.insert(tk.END,"")
texto_gaseosa = ttk.Entry()
texto_gaseosa.place(x=700, y=250)
texto_gaseosa.insert(tk.END,"")

# CAJAS FACTURACION/VUELTO/PAGO
facturacion = ttk.Entry()
facturacion.place(x=300, y=380)
facturacion.insert(tk.END,'')
paga_con = ttk.Entry()
paga_con.place(x=300, y=410)
paga_con.insert(tk.END, '')
vuelto = ttk.Entry()
vuelto.place(x=300, y=440)
vuelto.insert(tk.END, '')

## ETIQUETAS
# ETIQUETAS EMPANADAS Y TARTAS
ttk.Label(text=f'Numero de pedido:').place(x=28, y=10)
ttk.Label(text=" Ingrese un nuevo pedido: ").place(x=25, y=40)
lab_carne=ttk.Label(text='Cantidad de empanadas de CARNE: ')
lab_carne.place(x=25, y=75)
lab_pollo = ttk.Label(text='Cantidad de empanadas de POLLO: ')
lab_pollo.place(x=25, y=100)
lab_jq = ttk.Label(text='Cantidad de empanadas de JAMON Y QUESO: ')
lab_jq.place(x=25, y=125)
lab_ver = ttk.Label(text='Cantidad de empanadas de VERDURA: ')
lab_ver.place(x=25, y=150)
lab_cq = ttk.Label(text='Cantidad de empanadas de CEBOLLA Y QUESO: ')
lab_cq.place(x=25, y=175)
lab_tar_jq = ttk.Label(text='Cantidad de tartas de JAMON Y QUESO: ')
lab_tar_jq.place(x=25, y=200)
lab_tar_puerro = ttk.Label(text='Cantidad de tartas de PUERRO: ')
lab_tar_puerro.place(x=25, y=225)
lab_tar_beren = ttk.Label(text='Cantidad de tartas de BERENJENA: ')
lab_tar_beren.place(x=25, y=250)
lab_tar_acelga = ttk.Label(text='Cantidad de tartas de ACELGA: ')
lab_tar_acelga.place(x=25, y=275)
lab_tar_calabaza = ttk.Label(text='Cantidad de tartas de CALABAZA: ')
lab_tar_calabaza.place(x=25, y=300)
lab_tar_zapa = ttk.Label(text='Cantidad de tartas de ZAPALLITO: ')
lab_tar_zapa.place(x=25, y=325)
# ETIQUETAS OTROS
lab_menu=ttk.Label(text='Cantidad de PLATOS DEL DIA: ')
lab_menu.place(x=500, y=75)
lab_tortilla=ttk.Label(text='Cantidad de TORTILLAS: ')
lab_tortilla.place(x=500, y=100)
lab_fruta=ttk.Label(text='Cantidad de FRUTAS: ')
lab_fruta.place(x=500, y=125)
lab_cafe=ttk.Label(text='Cantidad de CAFES: ')
lab_cafe.place(x=500, y=150)
lab_alfajores=ttk.Label(text='Cantidad de ALFAJORES: ')
lab_alfajores.place(x=500, y=175)
lab_medialunas=ttk.Label(text='Cantidad de MEDIALUNAS: ')
lab_medialunas.place(x=500, y=200)
lab_ensalada_fruta=ttk.Label(text='Cantidad de ENSALADAS DE FRUTA: ')
lab_ensalada_fruta.place(x=500, y=225)
lab_gaseosa=ttk.Label(text='Cantidad de GASEOSAS: ')
lab_gaseosa.place(x=500, y=250)


# ETIQUETAS FACTURACION/VUELTO/PAGO
lab_fact = ttk.Label(text='Total a pagar: ')
lab_fact.place(x=25, y=380)
lab_paga = ttk.Label(text='Cliente paga con: ')
lab_paga.place(x=25, y=410)
lab_vuelto = ttk.Label(text='Vuelto a dar: ')
lab_vuelto.place(x=25, y=440)


## BOTONES - MESSAGE BOX
ingresar = ttk.Button(text='Aceptar', command=confirmar)
cancelar = ttk.Button(text='Cancelar', command=cancelar)
ingresar.place(x=600, y=480)
cancelar.place(x=700, y=480)
boton_calcular = ttk.Button(text='Calcular venta', command=suma)
boton_calcular.place(x=450,y=380)
boton_vuelto = ttk.Button(text='Calcular vuelto', command=fun_vuelto)
boton_vuelto.place(x=450, y=410)

ventana.mainloop()

