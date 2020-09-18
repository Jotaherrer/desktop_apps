"""
App de escritorio - Pedidos
Comando para convertir en ejecutable: pyinstaller --windowed --onedir --icon=./images.ico viejo_caballito.py
"""
import ttkthemes as themes
import tkinter as tk
from tkinter import messagebox, ttk
import os, time
import xlwings as xw
from openpyxl import Workbook, load_workbook

lista_venta = []
empanadas_de_carne = []
empanadas_de_pollo = []
empanadas_de_jq = []
empanadas_de_verduda = []
empanadas_de_cq = []
lista_tarta_jq = []
lista_tarta_puerro = []
lista_tarta_beren = []
lista_tarta_acelga = []
lista_tarta_cala = []
lista_tarta_zapa = []
lista_menu_sin = []
lista_menu = []
lista_tortilla = []
list_fruta =[]
lista_cafe = []
lista_alfajor = []
lista_medialuna = []
lista_ensa_fruta = []
lista_gaseosa = []
lista_gaseosa_grande = []
lista_por_papas = []
lista_pure = []
lista_cerveza = []

def comprobar_archivo():
    existe = os.path.exists('Ventas.xlsx')
    if existe:
        wb = load_workbook(filename='Ventas.xlsx')
        ws = wb.active
        print('Apertura exitosa del archivo.')
    else:
        wb = Workbook()
        ws = wb.active
        titulo = ('Hora transacción',"Emp. Carne", 'Emp. Pollo', 'Emp. JQ', 'Emp. Verdura', 'Emp. CQ', 'Tar. JQ', 'Tar. Puerro', 'Tar. Beren.', 'Tar. Acelga', 'Tar. Calab.', 'Tar. Zapa.','Plato S/ Guarn.','Platos','Tortilla','Ensalada','Cafe','Alfajores','Medialunas','Ensa. Fruta','Gaseosa chica','Gaseosa grande','Porción papas','Porción puré','Cerveza','Descuentos','Tarjeta D.','Total')
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
    

def cambiar_tarjeta_valor():
    if tarjeta_valor.get() == int(1):
        tarjeta_valor.set(0)
        print('Borrado boton tarjeta_valor')
    else:
        print('Boton no tildado..')
        print(tarjeta_valor.get())
        print(type(tarjeta_valor.get()))
        pass


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
        texto_menu_sin.delete(0,tk.END)
        texto_menu.delete(0,tk.END)
        texto_tortilla.delete(0,tk.END)
        texto_fruta.delete(0,tk.END)
        texto_cafe.delete(0,tk.END)
        texto_alfa.delete(0,tk.END)
        texto_media.delete(0,tk.END)
        texto_ensa_fru.delete(0,tk.END)
        texto_gaseosa.delete(0,tk.END)
        texto_gaseosa_grande.delete(0,tk.END)
        texto_papas.delete(0,tk.END)
        texto_pure.delete(0,tk.END)
        texto_cerveza.delete(0,tk.END)
        cambiar_tarjeta_valor()

        facturacion.delete(0,tk.END)
        paga_con.delete(0,tk.END)
        vuelto.delete(0,tk.END)
        descuento.delete(0,tk.END)
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
        texto_menu_sin.delete(0,tk.END)
        texto_menu.delete(0,tk.END)
        texto_tortilla.delete(0,tk.END)
        texto_fruta.delete(0,tk.END)
        texto_cafe.delete(0,tk.END)
        texto_alfa.delete(0,tk.END)
        texto_media.delete(0,tk.END)
        texto_ensa_fru.delete(0,tk.END)
        texto_gaseosa.delete(0,tk.END)
        texto_gaseosa_grande.delete(0,tk.END)        
        texto_papas.delete(0,tk.END)
        texto_pure.delete(0,tk.END)
        texto_cerveza.delete(0,tk.END)
        cambiar_tarjeta_valor()

        facturacion.delete(0,tk.END)
        paga_con.delete(0,tk.END)
        vuelto.delete(0,tk.END)
        descuento.delete(0,tk.END)
    else:
        pass


def contenido(texto):
    try:
        gusto = float(texto.get())
    except:
        if texto.get() == '':
            gusto = float(0)
        else:
            messagebox.showinfo(title='Error', message='Ingrese un número válido.')
    return gusto


def suma():
    hora = time.asctime()        
    if facturacion.get() == '':
        precio_empanada,precio_tarta,precio_menu_sin,precio_menu,precio_tortilla,precio_fruta,precio_cafe,precio_alfa,precio_media,precio_ensa_fruta,precio_gaseosa,precio_gaseosa_grande,precio_papas,precio_pure,precio_cerveza = 60, 100, 150,250, 120,50,70,50,25,100,100,200,125,125,150

        carne = contenido(texto_carne)
        pollo = contenido(texto_pollo)
        jq = contenido(texto_jq)
        ver = contenido(texto_verdura)
        cq = contenido(texto_cq)
        tarta_jq = contenido(texto_tar_jq)
        tarta_puerro = contenido(texto_tar_puerro)
        tarta_beren = contenido(texto_tar_beren)
        tarta_acelga = contenido(texto_tar_acelga)
        tarta_cala = contenido(texto_tar_cala)
        tarta_zapa = contenido(texto_tar_zapa)
        menu_sin = contenido(texto_menu_sin)
        menu = contenido(texto_menu)
        tortilla = contenido(texto_tortilla)
        fruta = contenido(texto_fruta)
        cafe = contenido(texto_cafe)
        alfa = contenido(texto_alfa)
        medialuna = contenido(texto_media)
        ensa_fruta = contenido(texto_ensa_fru)
        gaseosa = contenido(texto_gaseosa)
        gaseosa_grande = contenido(texto_gaseosa_grande)
        papas = contenido(texto_papas)
        pure = contenido(texto_pure)
        cerveza = contenido(texto_cerveza)

    else:
        facturacion.delete(0,tk.END)
        precio_empanada,precio_tarta,precio_menu_sin,precio_menu,precio_tortilla,precio_fruta,precio_cafe,precio_alfa,precio_media,precio_ensa_fruta,precio_gaseosa,precio_gaseosa_grande,precio_papas,precio_pure,precio_cerveza = 60, 100, 150,250, 120,50,70,50,25,100,100,200,125,125,150
        
        carne = contenido(texto_carne)
        pollo = contenido(texto_pollo)
        jq = contenido(texto_jq)
        ver = contenido(texto_verdura)
        cq = contenido(texto_cq)
        tarta_jq = contenido(texto_tar_jq)
        tarta_puerro = contenido(texto_tar_puerro)
        tarta_beren = contenido(texto_tar_beren)
        tarta_acelga = contenido(texto_tar_acelga)
        tarta_cala = contenido(texto_tar_cala)
        tarta_zapa = contenido(texto_tar_zapa)
        menu_sin = contenido(texto_menu_sin)        
        menu = contenido(texto_menu)
        tortilla = contenido(texto_tortilla)
        fruta = contenido(texto_fruta)
        cafe = contenido(texto_cafe)
        alfa = contenido(texto_alfa)
        medialuna = contenido(texto_media)
        ensa_fruta = contenido(texto_ensa_fru)
        gaseosa = contenido(texto_gaseosa)
        gaseosa_grande = contenido(texto_gaseosa_grande)
        papas = contenido(texto_papas)
        pure = contenido(texto_pure)
        cerveza = contenido(texto_cerveza)

    descuento_clientes = contenido(descuento)
    total_empa = (carne+pollo+jq+ver+cq) * precio_empanada
    total_tarta = (tarta_jq +tarta_puerro+tarta_beren+tarta_acelga+tarta_cala+tarta_zapa) * precio_tarta
    total_otros = (menu_sin*precio_menu_sin+menu*precio_menu+tortilla*precio_tortilla+fruta*precio_fruta+cafe*precio_cafe+alfa*precio_alfa+medialuna*precio_media+ensa_fruta*precio_ensa_fruta+gaseosa*precio_gaseosa+precio_gaseosa_grande*gaseosa_grande+papas*precio_papas+precio_pure*pure+cerveza*precio_cerveza) 
    total_productos = total_empa + total_tarta + total_otros - descuento_clientes
    facturacion.insert("0", total_productos)

    pago_tarjeta = checkbox_clicked()
    lista_venta.append(total_productos)
    empanadas_de_carne.append(carne)
    empanadas_de_jq.append(jq)
    empanadas_de_pollo.append(pollo)
    empanadas_de_verduda.append(ver)
    empanadas_de_cq.append(cq)
    lista_tarta_jq.append(tarta_jq)
    lista_tarta_puerro.append(tarta_puerro)
    lista_tarta_beren.append(tarta_beren)
    lista_tarta_acelga.append(tarta_acelga)
    lista_tarta_cala.append(tarta_cala)
    lista_tarta_zapa.append(tarta_zapa)
    lista_menu_sin.append(menu_sin)
    lista_menu.append(menu)
    lista_tortilla.append(tortilla)
    list_fruta.append(fruta)
    lista_cafe.append(cafe)
    lista_alfajor.append(alfa)
    lista_medialuna.append(medialuna)
    lista_ensa_fruta.append(ensa_fruta)
    lista_gaseosa.append(gaseosa)
    lista_gaseosa_grande.append(gaseosa_grande)
    lista_por_papas.append(papas)
    lista_pure.append(pure)
    lista_cerveza.append(cerveza)

    al_excel = [hora, carne, jq, pollo, ver, cq, tarta_jq, tarta_puerro, tarta_beren, tarta_acelga, tarta_cala, tarta_zapa,menu_sin,menu, tortilla,fruta,cafe,alfa,medialuna,ensa_fruta,gaseosa,gaseosa_grande,papas,pure,cerveza,descuento_clientes, pago_tarjeta,total_productos]
    guardar_datos(al_excel)
    lista_productos()
    total_dia.delete(0,tk.END)

def venta_acumulada():
    venta = sum(lista_venta)
    total_dia.insert('0',venta)


def funcion_conjunta():
    confirmar()
    venta_acumulada()


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


def borrar_datos():
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
    texto_menu.delete(0,tk.END)
    texto_tortilla.delete(0,tk.END)
    texto_fruta.delete(0,tk.END)
    texto_cafe.delete(0,tk.END)
    texto_alfa.delete(0,tk.END)
    texto_media.delete(0,tk.END)
    texto_ensa_fru.delete(0,tk.END)
    texto_gaseosa.delete(0,tk.END)
    texto_gaseosa_grande.delete(0,tk.END)  
    texto_papas.delete(0,tk.END) 
    texto_pure.delete(0,tk.END) 
    texto_cerveza.delete(0,tk.END) 

    cambiar_tarjeta_valor()

    facturacion.delete(0,tk.END)
    paga_con.delete(0,tk.END)
    vuelto.delete(0,tk.END)
    descuento.delete(0,tk.END)


def checkbox_clicked():
    rta = tarjeta_valor.get()
    return rta


### EXCEL INICIAL
comprobar_archivo()

### APP DE ESCRITORIO
ventana = themes.ThemedTk()
ventana.set_theme('winxpblue') # Other 'plastik'
ventana.config(height=540, width=870)
ventana.title("Aplicación de ventas - Viejo Caballito Bar")
#ventana.iconbitmap(default='./images.ico')
### CHECKBOX
tarjeta_valor = tk.IntVar()
tarjeta = ttk.Checkbutton(text='Pago con tarjeta?', variable=tarjeta_valor, command=checkbox_clicked)
tarjeta.place(x=450, y=410)

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
texto_menu_sin = ttk.Entry()
texto_menu_sin.place(x=300, y=350)
texto_menu_sin.insert(tk.END,"")
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
texto_gaseosa_grande = ttk.Entry()
texto_gaseosa_grande.place(x=700, y=275)
texto_gaseosa_grande.insert(tk.END,"")
texto_papas = ttk.Entry()
texto_papas.place(x=700, y=300)
texto_papas.insert(tk.END,"")
texto_pure = ttk.Entry()
texto_pure.place(x=700, y=325)
texto_pure.insert(tk.END,"")
texto_cerveza = ttk.Entry()
texto_cerveza.place(x=700, y=350)
texto_cerveza.insert(tk.END,"")

# CAJAS FACTURACION/VUELTO/PAGO
facturacion = ttk.Entry()
facturacion.place(x=300, y=440)
facturacion.insert(tk.END,'')
paga_con = ttk.Entry()
paga_con.place(x=300, y=470)
paga_con.insert(tk.END, '')
vuelto = ttk.Entry()
vuelto.place(x=300, y=500)
vuelto.insert(tk.END, '')
descuento = ttk.Entry()
descuento.place(x=300, y=415)
descuento.insert(tk.END,'')
total_dia = ttk.Entry()
total_dia.place(x=625, y=10,width=90)
total_dia.insert(tk.END,'')

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
lab_menu_sin = ttk.Label(text='Cantidad de PLATOS DEL DIA SIN GUARNICION: ')
lab_menu_sin.place(x=25, y=350)
lab_menu=ttk.Label(text='Cantidad de PLATOS DEL DIA: ')
lab_menu.place(x=500, y=75)
lab_tortilla=ttk.Label(text='Cantidad de TORTILLAS: ')
lab_tortilla.place(x=500, y=100)
lab_fruta=ttk.Label(text='Cantidad de ENSALADAS: ')
lab_fruta.place(x=500, y=125)
lab_cafe=ttk.Label(text='Cantidad de CAFES: ')
lab_cafe.place(x=500, y=150)
lab_alfajores=ttk.Label(text='Cantidad de ALFAJORES: ')
lab_alfajores.place(x=500, y=175)
lab_medialunas=ttk.Label(text='Cantidad de MEDIALUNAS: ')
lab_medialunas.place(x=500, y=200)
lab_ensalada_fruta=ttk.Label(text='Cantidad de ENSALADAS DE FRUTA: ')
lab_ensalada_fruta.place(x=500, y=225)
lab_gaseosa=ttk.Label(text='Cantidad de GASEOSAS CHICAS: ')
lab_gaseosa.place(x=500, y=250)
lab_gaseosa_grande=ttk.Label(text='Cantidad de GASEOSAS GRANDES: ')
lab_gaseosa_grande.place(x=500, y=275)
lab_papas=ttk.Label(text='Cantidad de PORCIONES DE PAPAS: ')
lab_papas.place(x=500, y=300)
lab_pure=ttk.Label(text='Cantidad de PORCIONES DE PURE: ')
lab_pure.place(x=500, y=325)
lab_cerveza=ttk.Label(text='Cantidad de CERVEZAS: ')
lab_cerveza.place(x=500, y=350)

# ETIQUETAS FACTURACION/VUELTO/PAGO
lab_fact = ttk.Label(text='Total a pagar: ')
lab_fact.place(x=25, y=440)
lab_paga = ttk.Label(text='Cliente paga con: ')
lab_paga.place(x=25, y=470)
lab_vuelto = ttk.Label(text='Vuelto a dar: ')
lab_vuelto.place(x=25, y=500)
lab_desc = ttk.Label(text='Descuento a clientes: ')
lab_desc.place(x=25, y=415)
lab_total = ttk.Label(text='VENTA ACUMULADA: ')
lab_total.place(x=500, y=10)


## BOTONES - MESSAGE BOX
ingresar = ttk.Button(text='Aceptar', command=funcion_conjunta)
cancelar = ttk.Button(text='Cancelar', command=cancelar)
ingresar.place(x=550, y=480)
cancelar.place(x=625, y=480)
boton_calcular = ttk.Button(text='Calcular venta', command=suma)
boton_calcular.place(x=450,y=440)
boton_vuelto = ttk.Button(text='Calcular vuelto', command=fun_vuelto)
boton_vuelto.place(x=450, y=470)
boton_borrar = ttk.Button(text='Borrar datos', command=borrar_datos)
boton_borrar.place(x=700, y=480)

ventana.mainloop()

