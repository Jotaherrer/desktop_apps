"""
App de escritorio - Costos
Comando para convertir en ejecutable: pyinstaller --windowed --onedir --icon=./images.ico viejo_caballito.py
"""
import ttkthemes as themes
import tkinter as tk
from tkinter import messagebox, ttk
import os, time
import xlwings as xw
from openpyxl import Workbook, load_workbook


def comprobar_archivo():
    existe = os.path.exists('Costos.xlsx')
    if existe:
        wb = load_workbook(filename='Costos.xlsx')
        ws = wb.active
        print('Apertura exitosa del archivo.')
    else:
        wb = Workbook()
        ws = wb.active
        titulo = ('Hora transacción','Queso','Leche','Pollo','Carne P.','Tapa','Cebolla','Pan','Tomate','Lechuga','Yogur','Agua','Nalga','Empleados','Acelga','Alquiler','Luz','Agua','Telefono','ABL','Diario','Fumig.','Deterg.','Monotr.','Total')
        ws.append(titulo)
        wb.save(filename='Costos.xlsx')
        print('Creación exitosa del archivo')


def guardar_datos(pedido):
    wb = load_workbook(filename='Costos.xlsx')
    wb.active.append(pedido)
    wb.save('Costos.xlsx')    
    print("Carga exitosa del costo!!")


def contenido(caja_precio, caja_cantidad, total):
    try:
        variable = int(caja_precio.get()) * int(caja_cantidad.get())
        total.insert('0',variable)
    except:
        if (caja_precio.get() == '') | (caja_cantidad.get() == ''):
            variable = 0
        else:
            messagebox.showinfo(title='Error', message='Ingresar un número válido')
    return variable


def contenido_fijos(caja_precio, caja_obs):
    try:
        variable = int(caja_precio.get())
    except:    
        if caja_precio.get() == '':
            variable = 0
        else:
            messagebox.showinfo(title='Error', message='Ingresar un número válido')
    return variable


def mult():
    hora = time.asctime()    
    if caja_total.get() == '':
        ## COMPLETA VALORES CON FUNCION 'CONTENIDO'
        # COSTOS VARIABLES
        queso = contenido(caja_p_queso, caja_q_queso, caja_t_queso)
        leche = contenido(caja_p_leche, caja_q_leche, caja_t_leche)
        pollo = contenido(caja_p_pollo, caja_q_pollo, caja_t_pollo)
        carne_p = contenido(caja_p_carnep, caja_q_carnep, caja_t_carnep)
        tapa = contenido(caja_p_tapa, caja_q_tapa, caja_t_tapa)
        cebolla = contenido(caja_p_cebolla, caja_q_cebolla, caja_t_cebolla)
        pan = contenido(caja_p_pan, caja_q_pan, caja_t_pan)
        tomate = contenido(caja_p_tomate, caja_q_tomate, caja_t_tomate)
        lechuga = contenido(caja_p_lechuga, caja_q_lechuga, caja_t_lechuga)
        yogur = contenido(caja_p_yogur, caja_q_yogur, caja_t_yogur)
        agua = contenido(caja_p_agua, caja_q_agua, caja_t_agua)
        nalga = contenido(caja_p_nalga, caja_q_nalga, caja_t_nalga)
        empleados = contenido(caja_p_empleados, caja_q_empleados, caja_t_empleados)
        acelga = contenido(caja_p_acelga, caja_q_acelga, caja_t_acelga)

        # COSTOS FIJOS
        alquiler = contenido_fijos(caja_p_alquiler,caja_obs_alquiler)
        luz = contenido_fijos(caja_p_luz, caja_obs_luz)
        agua = contenido_fijos(caja_p_agua, caja_obs_agua)
        telefono = contenido_fijos(caja_p_telefono, caja_obs_telefono)
        abl = contenido_fijos(caja_p_abl, caja_obs_abl)
        diario = contenido_fijos(caja_p_diario, caja_obs_diario)
        fumigador = contenido_fijos(caja_p_fumigador, caja_obs_fumigador)
        detergente = contenido_fijos(caja_p_detergente, caja_obs_fumigador)
        monotributo = contenido_fijos(caja_p_monotributo, caja_obs_monotributo)
    else:
        # BORRA CASILLEROS COMPLETOS
        caja_total.delete(0,tk.END)
        caja_t_queso.delete(0,tk.END)
        caja_t_leche.delete(0,tk.END)
        caja_t_pollo.delete(0,tk.END)
        caja_t_carnep.delete(0,tk.END)
        caja_t_tapa.delete(0,tk.END)
        caja_t_cebolla.delete(0,tk.END)
        caja_t_pan.delete(0,tk.END)
        caja_t_tomate.delete(0,tk.END)
        caja_t_lechuga.delete(0,tk.END)
        caja_t_yogur.delete(0,tk.END)
        caja_t_agua.delete(0,tk.END)
        caja_t_nalga.delete(0,tk.END)
        caja_t_empleados.delete(0, tk.END)

        # COMPLETA NUEVAMENTE VALORES
        # COSTOS VARIABLES
        queso = contenido(caja_p_queso, caja_q_queso, caja_t_queso)
        leche = contenido(caja_p_leche, caja_q_leche, caja_t_leche)
        pollo = contenido(caja_p_pollo, caja_q_pollo, caja_t_pollo)
        carne_p = contenido(caja_p_carnep, caja_q_carnep, caja_t_carnep)
        tapa = contenido(caja_p_tapa, caja_q_tapa, caja_t_tapa)
        cebolla = contenido(caja_p_cebolla, caja_q_cebolla, caja_t_cebolla)
        pan = contenido(caja_p_pan, caja_q_pan, caja_t_pan)
        tomate = contenido(caja_p_tomate, caja_q_tomate, caja_t_tomate)
        lechuga = contenido(caja_p_lechuga, caja_q_lechuga, caja_t_lechuga)
        yogur = contenido(caja_p_yogur, caja_q_yogur, caja_t_yogur)
        agua = contenido(caja_p_agua, caja_q_agua, caja_t_agua)
        nalga = contenido(caja_p_nalga, caja_q_nalga, caja_t_nalga)
        empleados = contenido(caja_p_empleados, caja_q_empleados, caja_t_empleados)
        acelga = contenido(caja_p_acelga, caja_q_acelga, caja_t_acelga)

        # COSTOS FIJOS
        alquiler = contenido_fijos(caja_p_alquiler,caja_obs_alquiler)
        luz = contenido_fijos(caja_p_luz, caja_obs_luz)
        agua = contenido_fijos(caja_p_agua, caja_obs_agua)
        telefono = contenido_fijos(caja_p_telefono, caja_obs_telefono)
        abl = contenido_fijos(caja_p_abl, caja_obs_abl)
        diario = contenido_fijos(caja_p_diario, caja_obs_diario)
        fumigador = contenido_fijos(caja_p_fumigador, caja_obs_fumigador)
        detergente = contenido_fijos(caja_p_detergente, caja_obs_fumigador)
        monotributo = contenido_fijos(caja_p_monotributo, caja_obs_monotributo)

    costos_varios = queso + leche + pollo + carne_p + tapa + cebolla + pan + tomate + lechuga+yogur+agua+nalga+empleados + acelga
    costos_fijos = alquiler + luz + agua + telefono + abl + diario + fumigador + detergente + monotributo
    facturacion = costos_varios + costos_fijos
    caja_total.insert('0',facturacion)

    # PASAJE A EXCEL
    al_excel = [hora, queso,leche,pollo,carne_p,tapa,cebolla,pan,tomate,lechuga,yogur, agua,nalga,empleados,acelga,alquiler,luz,agua,telefono,abl,diario,fumigador,detergente,monotributo,facturacion]
    guardar_datos(al_excel)


def confirmar():
    if caja_total == '':
        messagebox.showinfo(title='Error', message='Ingresar datos numéricos en el registro.')
    else:
        # COSTOS VARIABLES
        caja_p_queso.delete(0,tk.END)
        caja_q_queso.delete(0,tk.END)
        caja_t_queso.delete(0,tk.END)
        caja_p_leche.delete(0,tk.END)
        caja_q_leche.delete(0,tk.END)
        caja_t_leche.delete(0,tk.END)
        caja_p_pollo.delete(0,tk.END)
        caja_q_pollo.delete(0,tk.END)
        caja_t_pollo.delete(0,tk.END)
        caja_p_carnep.delete(0,tk.END)
        caja_q_carnep.delete(0,tk.END)
        caja_t_carnep.delete(0,tk.END)
        caja_p_tapa.delete(0,tk.END)
        caja_q_tapa.delete(0,tk.END)
        caja_t_tapa.delete(0,tk.END)
        caja_p_cebolla.delete(0,tk.END)
        caja_q_cebolla.delete(0,tk.END)
        caja_t_cebolla.delete(0,tk.END)
        caja_p_pan.delete(0,tk.END)
        caja_q_pan.delete(0,tk.END)
        caja_t_pan.delete(0,tk.END)
        caja_p_tomate.delete(0,tk.END)
        caja_q_tomate.delete(0,tk.END)
        caja_t_tomate.delete(0,tk.END)
        caja_p_lechuga.delete(0,tk.END)
        caja_q_lechuga.delete(0,tk.END)
        caja_t_lechuga.delete(0,tk.END)
        caja_p_yogur.delete(0,tk.END)
        caja_q_yogur.delete(0,tk.END)
        caja_t_yogur.delete(0,tk.END)
        caja_p_agua.delete(0,tk.END)
        caja_q_agua.delete(0,tk.END)
        caja_t_agua.delete(0,tk.END)
        caja_p_nalga.delete(0,tk.END)
        caja_q_nalga.delete(0,tk.END)
        caja_t_nalga.delete(0,tk.END)
        caja_p_empleados.delete(0,tk.END)
        caja_q_empleados.delete(0,tk.END)
        caja_t_empleados.delete(0,tk.END)
        caja_p_acelga.delete(0,tk.END)
        caja_q_acelga.delete(0,tk.END)
        caja_t_acelga.delete(0,tk.END)
        # COSTOS FIJOS
        caja_p_alquiler.delete(0,tk.END)
        caja_obs_alquiler.delete(0, tk.END)
        caja_p_luz.delete(0,tk.END)
        caja_obs_luz.delete(0, tk.END)
        caja_p_agua.delete(0,tk.END)
        caja_obs_agua.delete(0, tk.END)
        caja_p_telefono.delete(0,tk.END)
        caja_obs_telefono.delete(0, tk.END)
        caja_p_abl.delete(0,tk.END)
        caja_obs_abl.delete(0, tk.END)
        caja_p_diario.delete(0,tk.END)
        caja_obs_diario.delete(0, tk.END)
        caja_p_fumigador.delete(0,tk.END)
        caja_obs_fumigador.delete(0, tk.END)
        caja_p_detergente.delete(0,tk.END)
        caja_obs_detergente.delete(0, tk.END)
        caja_p_monotributo.delete(0,tk.END)
        caja_obs_monotributo.delete(0, tk.END)
        
        caja_total.delete(0,tk.END)    
        
        # PASAJE A EXCEL
        
        


def borrar_datos():
    # COSTOS VARIABLES
    caja_p_queso.delete(0,tk.END)
    caja_q_queso.delete(0,tk.END)
    caja_t_queso.delete(0,tk.END)
    caja_p_leche.delete(0,tk.END)
    caja_q_leche.delete(0,tk.END)
    caja_t_leche.delete(0,tk.END)
    caja_p_pollo.delete(0,tk.END)
    caja_q_pollo.delete(0,tk.END)
    caja_t_pollo.delete(0,tk.END)
    caja_p_carnep.delete(0,tk.END)
    caja_q_carnep.delete(0,tk.END)
    caja_t_carnep.delete(0,tk.END)
    caja_p_tapa.delete(0,tk.END)
    caja_q_tapa.delete(0,tk.END)
    caja_t_tapa.delete(0,tk.END)
    caja_p_cebolla.delete(0,tk.END)
    caja_q_cebolla.delete(0,tk.END)
    caja_t_cebolla.delete(0,tk.END)
    caja_p_pan.delete(0,tk.END)
    caja_q_pan.delete(0,tk.END)
    caja_t_pan.delete(0,tk.END)
    caja_total.delete(0,tk.END) 
    caja_p_tomate.delete(0,tk.END)
    caja_q_tomate.delete(0,tk.END)
    caja_t_tomate.delete(0,tk.END)
    caja_p_lechuga.delete(0,tk.END)
    caja_q_lechuga.delete(0,tk.END)
    caja_t_lechuga.delete(0,tk.END)
    caja_p_yogur.delete(0,tk.END)
    caja_q_yogur.delete(0,tk.END)
    caja_t_yogur.delete(0,tk.END)
    caja_p_agua.delete(0,tk.END)
    caja_q_agua.delete(0,tk.END)
    caja_t_agua.delete(0,tk.END)
    caja_p_nalga.delete(0,tk.END)
    caja_q_nalga.delete(0,tk.END)
    caja_t_nalga.delete(0,tk.END)
    caja_p_empleados.delete(0,tk.END)
    caja_q_empleados.delete(0,tk.END)
    caja_t_empleados.delete(0,tk.END)
    caja_p_acelga.delete(0,tk.END)
    caja_q_acelga.delete(0,tk.END)
    caja_t_acelga.delete(0,tk.END)
    # COSTOS FIJOS
    caja_p_alquiler.delete(0,tk.END)
    caja_obs_alquiler.delete(0, tk.END)
    caja_p_luz.delete(0,tk.END)
    caja_obs_luz.delete(0, tk.END)
    caja_p_agua.delete(0,tk.END)
    caja_obs_agua.delete(0, tk.END)
    caja_p_telefono.delete(0,tk.END)
    caja_obs_telefono.delete(0, tk.END)
    caja_p_abl.delete(0,tk.END)
    caja_obs_abl.delete(0, tk.END)
    caja_p_diario.delete(0,tk.END)
    caja_obs_diario.delete(0, tk.END)
    caja_p_fumigador.delete(0,tk.END)
    caja_obs_fumigador.delete(0, tk.END)
    caja_p_detergente.delete(0,tk.END)
    caja_obs_detergente.delete(0, tk.END)
    caja_p_monotributo.delete(0,tk.END)
    caja_obs_monotributo.delete(0, tk.END)


### EXCEL INICIAL
comprobar_archivo()

### APP DE ESCRITORIO
ventana = themes.ThemedTk()
ventana.set_theme('plastik') # Other 'ventana.get_themes()'
ventana.config(height=700, width=900)
ventana.title("Aplicación de costos - Viejo Caballito Bar")

### ETIQUETAS
cantidad = ttk.Label(text='Cantidad (Kg./Lit.)').place(x=115,y=40)
precio = ttk.Label(text='Precio por unidad').place(x=230,y=40)
total = ttk.Label(text='Costo total').place(x=355,y=40)
precio_fijos = ttk.Label(text='Costo total').place(x=590, y=40)
obser_fijos = ttk.Label(text='Observación a realizar').place(x=680, y=40)

cv = ttk.Label(text='Panel de costos VARIOS:').place(x=20,y=15)
cf = ttk.Label(text='Panel de costos FIJOS:').place(x=500,y=15)

## COSTOS VARIOS
label_queso = ttk.Label(text='Horma queso  ==> ')
label_queso.place(x=20,y=60)
label_leche = ttk.Label(text='Leche  ==> ')
label_leche.place(x=20,y=85)
label_pollo = ttk.Label(text='Pollo  ==> ')
label_pollo.place(x=20,y=110)
label_carne_picada = ttk.Label(text='Carne Picada  ==> ')
label_carne_picada.place(x=20,y=135)
label_tapa = ttk.Label(text='Tapa  ==> ')
label_tapa.place(x=20,y=160)
label_cebolla = ttk.Label(text='Cebolla  ==> ')
label_cebolla.place(x=20,y=185)
label_pan = ttk.Label(text='Pan  ==> ')
label_pan.place(x=20,y=210)
label_tomate = ttk.Label(text='Tomate  ==> ')
label_tomate.place(x=20,y=235)
label_lechuga = ttk.Label(text='Lechuga  ==> ')
label_lechuga.place(x=20,y=260)
label_yogur = ttk.Label(text='Yogur  ==> ')
label_yogur.place(x=20,y=285)
label_agua = ttk.Label(text='Agua  ==> ')
label_agua.place(x=20,y=310)
label_nalga = ttk.Label(text='Nalga  ==> ')
label_nalga.place(x=20,y=335)
label_empleada = ttk.Label(text='Empleados  ==> ')
label_empleada.place(x=20,y=360)
label_acelga = ttk.Label(text='Acelga  ==> ')
label_acelga.place(x=20,y=385)

## COSTOS FIJOS
label_alquiler = ttk.Label(text='Alquiler  ==> ')
label_alquiler.place(x=500,y=60)
label_luz = ttk.Label(text='Luz  ==> ')
label_luz.place(x=500,y=85)
label_agua = ttk.Label(text='Agua  ==> ')
label_agua.place(x=500,y=110)
label_telefono = ttk.Label(text='Teléfono  ==> ')
label_telefono.place(x=500,y=135)
label_abl = ttk.Label(text='ABL  ==> ')
label_abl.place(x=500,y=160)
label_diario = ttk.Label(text='Diario  ==> ')
label_diario.place(x=500,y=185)
label_fumigador = ttk.Label(text='Fumigador  ==> ')
label_fumigador.place(x=500,y=210)
label_detergente = ttk.Label(text='Detergente  ==> ')
label_detergente.place(x=500,y=235)
label_monotributo = ttk.Label(text='Monotributo  => ')
label_monotributo.place(x=500,y=260)

### CAJAS
## COSTOS VARIOS
caja_q_queso = ttk.Entry()
caja_q_queso.place(x=125, y=60,width=80)
caja_q_queso.insert(tk.END,'')
caja_p_queso = ttk.Entry()
caja_p_queso.place(x=235, y=60,width=80)
caja_p_queso.insert(tk.END,'')
caja_t_queso = ttk.Entry()
caja_t_queso.place(x=345, y=60,width=80)
caja_t_queso.insert(tk.END,'')

caja_q_leche = ttk.Entry()
caja_q_leche.place(x=125, y=85,width=80)
caja_q_leche.insert(tk.END,'')
caja_p_leche = ttk.Entry()
caja_p_leche.place(x=235, y=85,width=80)
caja_p_leche.insert(tk.END,'')
caja_t_leche = ttk.Entry()
caja_t_leche.place(x=345, y=85,width=80)
caja_t_leche.insert(tk.END,'')

caja_q_pollo = ttk.Entry()
caja_q_pollo.place(x=125, y=110,width=80)
caja_q_pollo.insert(tk.END,'')
caja_p_pollo = ttk.Entry()
caja_p_pollo.place(x=235, y=110,width=80)
caja_p_pollo.insert(tk.END,'')
caja_t_pollo = ttk.Entry()
caja_t_pollo.place(x=345, y=110,width=80)
caja_t_pollo.insert(tk.END,'')

caja_q_carnep = ttk.Entry()
caja_q_carnep.place(x=125, y=135,width=80)
caja_q_carnep.insert(tk.END,'')
caja_p_carnep = ttk.Entry()
caja_p_carnep.place(x=235, y=135,width=80)
caja_p_carnep.insert(tk.END,'')
caja_t_carnep = ttk.Entry()
caja_t_carnep.place(x=345, y=135,width=80)
caja_t_carnep.insert(tk.END,'')

caja_q_tapa = ttk.Entry()
caja_q_tapa.place(x=125, y=160,width=80)
caja_q_tapa.insert(tk.END,'')
caja_p_tapa = ttk.Entry()
caja_p_tapa.place(x=235, y=160,width=80)
caja_p_tapa.insert(tk.END,'')
caja_t_tapa = ttk.Entry()
caja_t_tapa.place(x=345, y=160,width=80)
caja_t_tapa.insert(tk.END,'')

caja_q_cebolla = ttk.Entry()
caja_q_cebolla.place(x=125, y=185,width=80)
caja_q_cebolla.insert(tk.END,'')
caja_p_cebolla = ttk.Entry()
caja_p_cebolla.place(x=235, y=185,width=80)
caja_p_cebolla.insert(tk.END,'')
caja_t_cebolla = ttk.Entry()
caja_t_cebolla.place(x=345, y=185,width=80)
caja_t_cebolla.insert(tk.END,'')

caja_q_pan = ttk.Entry()
caja_q_pan.place(x=125, y=210,width=80)
caja_q_pan.insert(tk.END,'')
caja_p_pan = ttk.Entry()
caja_p_pan.place(x=235, y=210,width=80)
caja_p_pan.insert(tk.END,'')
caja_t_pan = ttk.Entry()
caja_t_pan.place(x=345, y=210,width=80)
caja_t_pan.insert(tk.END,'')

caja_q_tomate = ttk.Entry()
caja_q_tomate.place(x=125, y=235,width=80)
caja_q_tomate.insert(tk.END,'')
caja_p_tomate = ttk.Entry()
caja_p_tomate.place(x=235, y=235,width=80)
caja_p_tomate.insert(tk.END,'')
caja_t_tomate = ttk.Entry()
caja_t_tomate.place(x=345, y=235,width=80)
caja_t_tomate.insert(tk.END,'')

caja_q_lechuga = ttk.Entry()
caja_q_lechuga.place(x=125, y=260,width=80)
caja_q_lechuga.insert(tk.END,'')
caja_p_lechuga = ttk.Entry()
caja_p_lechuga.place(x=235, y=260,width=80)
caja_p_lechuga.insert(tk.END,'')
caja_t_lechuga = ttk.Entry()
caja_t_lechuga.place(x=345, y=260,width=80)
caja_t_lechuga.insert(tk.END,'')

caja_q_yogur = ttk.Entry()
caja_q_yogur.place(x=125, y=285,width=80)
caja_q_yogur.insert(tk.END,'')
caja_p_yogur = ttk.Entry()
caja_p_yogur.place(x=235, y=285,width=80)
caja_p_yogur.insert(tk.END,'')
caja_t_yogur = ttk.Entry()
caja_t_yogur.place(x=345, y=285,width=80)
caja_t_yogur.insert(tk.END,'')

caja_q_agua = ttk.Entry()
caja_q_agua.place(x=125, y=310,width=80)
caja_q_agua.insert(tk.END,'')
caja_p_agua = ttk.Entry()
caja_p_agua.place(x=235, y=310,width=80)
caja_p_agua.insert(tk.END,'')
caja_t_agua = ttk.Entry()
caja_t_agua.place(x=345, y=310,width=80)
caja_t_agua.insert(tk.END,'')

caja_q_nalga = ttk.Entry()
caja_q_nalga.place(x=125, y=335,width=80)
caja_q_nalga.insert(tk.END,'')
caja_p_nalga = ttk.Entry()
caja_p_nalga.place(x=235, y=335,width=80)
caja_p_nalga.insert(tk.END,'')
caja_t_nalga = ttk.Entry()
caja_t_nalga.place(x=345, y=335,width=80)
caja_t_nalga.insert(tk.END,'')

caja_q_empleados = ttk.Entry()
caja_q_empleados.place(x=125, y=360,width=80)
caja_q_empleados.insert(tk.END,'')
caja_p_empleados = ttk.Entry()
caja_p_empleados.place(x=235, y=360,width=80)
caja_p_empleados.insert(tk.END,'')
caja_t_empleados = ttk.Entry()
caja_t_empleados.place(x=345, y=360,width=80)
caja_t_empleados.insert(tk.END,'')

caja_q_acelga = ttk.Entry()
caja_q_acelga.place(x=125, y=385,width=80)
caja_q_acelga.insert(tk.END,'')
caja_p_acelga = ttk.Entry()
caja_p_acelga.place(x=235, y=385,width=80)
caja_p_acelga.insert(tk.END,'')
caja_t_acelga = ttk.Entry()
caja_t_acelga.place(x=345, y=385,width=80)
caja_t_acelga.insert(tk.END,'')

caja_total = ttk.Entry()
caja_total.place(x=595, y=615, width=80)
caja_total.insert(tk.END,'')

## COSTOS FIJOS
caja_p_alquiler = ttk.Entry()
caja_p_alquiler.place(x=590, y=60,width=80)
caja_p_alquiler.insert(tk.END,'')
caja_obs_alquiler = ttk.Entry()
caja_obs_alquiler.place(x=680, y=60,width=180)
caja_obs_alquiler.insert(tk.END,'')

caja_p_luz = ttk.Entry()
caja_p_luz.place(x=590, y=85,width=80)
caja_p_luz.insert(tk.END,'')
caja_obs_luz = ttk.Entry()
caja_obs_luz.place(x=680, y=85,width=180)
caja_obs_luz.insert(tk.END,'')

caja_p_agua = ttk.Entry()
caja_p_agua.place(x=590, y=110,width=80)
caja_p_agua.insert(tk.END,'')
caja_obs_agua = ttk.Entry()
caja_obs_agua.place(x=680, y=110,width=180)
caja_obs_agua.insert(tk.END,'')

caja_p_telefono = ttk.Entry()
caja_p_telefono.place(x=590, y=135,width=80)
caja_p_telefono.insert(tk.END,'')
caja_obs_telefono = ttk.Entry()
caja_obs_telefono.place(x=680, y=135,width=180)
caja_obs_telefono.insert(tk.END,'')

caja_p_abl = ttk.Entry()
caja_p_abl.place(x=590, y=160,width=80)
caja_p_abl.insert(tk.END,'')
caja_obs_abl = ttk.Entry()
caja_obs_abl.place(x=680, y=160,width=180)
caja_obs_abl.insert(tk.END,'')

caja_p_diario = ttk.Entry()
caja_p_diario.place(x=590, y=185,width=80)
caja_p_diario.insert(tk.END,'')
caja_obs_diario = ttk.Entry()
caja_obs_diario.place(x=680, y=185,width=180)
caja_obs_diario.insert(tk.END,'')

caja_p_fumigador = ttk.Entry()
caja_p_fumigador.place(x=590, y=210,width=80)
caja_p_fumigador.insert(tk.END,'')
caja_obs_fumigador = ttk.Entry()
caja_obs_fumigador.place(x=680, y=210,width=180)
caja_obs_fumigador.insert(tk.END,'')

caja_p_detergente = ttk.Entry()
caja_p_detergente.place(x=590, y=235,width=80)
caja_p_detergente.insert(tk.END,'')
caja_obs_detergente = ttk.Entry()
caja_obs_detergente.place(x=680, y=235,width=180)
caja_obs_detergente.insert(tk.END,'')

caja_p_monotributo = ttk.Entry()
caja_p_monotributo.place(x=590, y=260,width=80)
caja_p_monotributo.insert(tk.END,'')
caja_obs_monotributo = ttk.Entry()
caja_obs_monotributo.place(x=680, y=260,width=180)
caja_obs_monotributo.insert(tk.END,'')

## BOTONES - MESSAGE BOX
costos = ttk.Button(text='Totalizar costos',command=mult)
costos.place(x=590,y=650)
costos.winfo_class()

confirmacion = ttk.Button(text='Confirmar costos', command=confirmar)
confirmacion.place(x=700,y=650)

boton_borrar = ttk.Button(text='Borrar datos', command=borrar_datos)
boton_borrar.place(x=345,y=650)

ventana.mainloop()

