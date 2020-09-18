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
        ws_costos = wb['Dato Costos']
        ws_obs = wb['Observaciones']
        print('Apertura exitosa del archivo.')
    else:
        wb = Workbook()
        ws_costos = wb.create_sheet('Dato Costos',0)
        ws_obs = wb.create_sheet('Observaciones',1)
        titulo_costos = ('Hora transacción','Queso','Leche','Pollo','Carne P.','Tapa','Cebolla','Pan','Tomate','Lechuga','Yogur','Agua','Nalga','Empleados','Acelga','Huevos','Servilletas','Yerba','Cafe','Jamón','Puerro','Berenjenas','Papa','Calabaza','Alquiler','Luz','AYSA','Telefono','ABL','Diario','Fumig.','Deterg.','Monotr.','Otros','Otros','Otros','Tarjeta?','Total')
        ws_costos.append(titulo_costos)
        titulos_obs = ('Hora transacción', 'Alquiler','Luz','AYSA','Telefono','ABL','Diario','Fumig.','Deterg.','Monotr.','Otros','Otros','Otros','Tarjeta?')
        ws_obs.append(titulos_obs)
        wb.save(filename='Costos.xlsx')
        print('Creación exitosa del archivo')


def guardar_datos_costos(pedido):
    wb = load_workbook(filename='Costos.xlsx')
    wb['Dato Costos'].append(pedido)
    wb.save('Costos.xlsx')    
    print("Carga exitosa del costo!!")


def guardar_datos_obs(info):
    wb = load_workbook(filename='Costos.xlsx')
    wb['Observaciones'].append(info)
    wb.save('Costos.xlsx')    
    print("Carga exitosa de las observaciones!!")
  

def cambiar_tarjeta_valor():
    if tarjeta_valor.get() == int(1):
        tarjeta_valor.set(0)
        print('Borrado boton tarjeta_valor')
    else:
        print('Boton no tildado..')
        print(tarjeta_valor.get())
        print(type(tarjeta_valor.get()))
        pass


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
        observacion = caja_obs.get()
    except:    
        if caja_precio.get() == '':
            variable = 0
            observacion = ''
        else:
            messagebox.showinfo(title='Error', message='Ingresar un número válido')
    return variable, observacion


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
        huevos = contenido(caja_p_huevos, caja_q_huevos, caja_t_huevos)
        servilletas = contenido(caja_p_servilletas, caja_q_servilletas, caja_t_servilletas)
        yerba = contenido(caja_p_yerba, caja_q_yerba, caja_t_yerba)        
        cafe = contenido(caja_p_cafe, caja_q_cafe, caja_t_cafe)
        jamon = contenido(caja_p_jamon, caja_q_jamon, caja_t_jamon)
        puerro = contenido(caja_p_puerro, caja_q_puerro, caja_t_puerro)
        beren = contenido(caja_p_beren, caja_q_beren, caja_t_beren)
        papa = contenido(caja_p_papa, caja_q_papa, caja_t_papa)
        cala = contenido(caja_p_calabaza, caja_q_calabaza, caja_t_calabaza)

        # COSTOS FIJOS
        alquiler = contenido_fijos(caja_p_alquiler,caja_obs_alquiler)[0]
        luz = contenido_fijos(caja_p_luz, caja_obs_luz)[0]
        agua_servicio = contenido_fijos(caja_p_agua_servicio, caja_obs_agua)[0]
        telefono = contenido_fijos(caja_p_telefono, caja_obs_telefono)[0]
        abl = contenido_fijos(caja_p_abl, caja_obs_abl)[0]
        diario = contenido_fijos(caja_p_diario, caja_obs_diario)[0]
        fumigador = contenido_fijos(caja_p_fumigador, caja_obs_fumigador)[0]
        detergente = contenido_fijos(caja_p_detergente, caja_obs_fumigador)[0]
        monotributo = contenido_fijos(caja_p_monotributo, caja_obs_monotributo)[0]
        otros1 = contenido_fijos(caja_p_otros1, caja_obs_otros1)[0]
        otros2 = contenido_fijos(caja_p_otros2, caja_obs_otros2)[0]
        otros3 = contenido_fijos(caja_p_otros3, caja_obs_otros3)[0]

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
        caja_t_acelga.delete(0,tk.END)
        caja_t_huevos.delete(0,tk.END)
        caja_t_servilletas.delete(0,tk.END)
        caja_t_yerba.delete(0,tk.END)
        caja_t_cafe.delete(0,tk.END)
        caja_t_jamon.delete(0,tk.END)
        caja_t_puerro.delete(0,tk.END)
        caja_t_beren.delete(0,tk.END)
        caja_t_papa.delete(0,tk.END)
        caja_t_calabaza.delete(0,tk.END)

        cambiar_tarjeta_valor()

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
        huevos = contenido(caja_p_huevos, caja_q_huevos, caja_t_huevos)
        servilletas = contenido(caja_p_servilletas, caja_q_servilletas, caja_t_servilletas)
        yerba = contenido(caja_p_yerba, caja_q_yerba, caja_t_yerba)
        cafe = contenido(caja_p_cafe, caja_q_cafe, caja_t_cafe)
        jamon = contenido(caja_p_jamon, caja_q_jamon, caja_t_jamon)
        puerro = contenido(caja_p_puerro, caja_q_puerro, caja_t_puerro)
        beren = contenido(caja_p_beren, caja_q_beren, caja_t_beren)
        papa = contenido(caja_p_papa, caja_q_papa, caja_t_papa)
        cala = contenido(caja_p_calabaza, caja_q_calabaza, caja_t_calabaza)

        # COSTOS FIJOS
        alquiler = contenido_fijos(caja_p_alquiler,caja_obs_alquiler)[0]
        luz = contenido_fijos(caja_p_luz, caja_obs_luz)[0]
        agua_servicio = contenido_fijos(caja_p_agua_servicio, caja_obs_agua)[0]
        telefono = contenido_fijos(caja_p_telefono, caja_obs_telefono)[0]
        abl = contenido_fijos(caja_p_abl, caja_obs_abl)[0]
        diario = contenido_fijos(caja_p_diario, caja_obs_diario)[0]
        fumigador = contenido_fijos(caja_p_fumigador, caja_obs_fumigador)[0]
        detergente = contenido_fijos(caja_p_detergente, caja_obs_fumigador)[0]
        monotributo = contenido_fijos(caja_p_monotributo, caja_obs_monotributo)[0]
        otros1 = contenido_fijos(caja_p_otros1, caja_obs_otros1)[0]
        otros2 = contenido_fijos(caja_p_otros2, caja_obs_otros2)[0]
        otros3 = contenido_fijos(caja_p_otros3, caja_obs_otros3)[0]

    pago_tarjeta = checkbox_clicked()
    costos_varios = queso + leche + pollo + carne_p + tapa + cebolla + pan + tomate + lechuga+yogur+agua+nalga+empleados + acelga + huevos + servilletas + yerba + cafe + jamon + puerro + beren + papa + cala
    costos_fijos = alquiler + luz + agua_servicio + telefono + abl + diario + fumigador + detergente + monotributo + otros1 + otros2 + otros3
    facturacion = costos_varios + costos_fijos
    caja_total.insert('0',facturacion)

    # PASAJE A EXCEL
    al_excel = [hora, queso,leche,pollo,carne_p,tapa,cebolla,pan,tomate,lechuga,yogur, agua,nalga,empleados,acelga,huevos,servilletas,yerba,cafe,jamon,puerro,beren,papa,cala,alquiler,luz,agua,telefono,abl,diario,fumigador,detergente,monotributo,otros1, otros2, otros3,pago_tarjeta,facturacion]
    al_excel_obs = [hora, contenido_fijos(caja_p_alquiler,caja_obs_alquiler)[1], contenido_fijos(caja_p_luz, caja_obs_luz)[1], contenido_fijos(caja_p_agua_servicio, caja_obs_agua)[1], contenido_fijos(caja_p_telefono, caja_obs_telefono)[1], contenido_fijos(caja_p_abl, caja_obs_abl)[1], contenido_fijos(caja_p_diario, caja_obs_diario)[1], contenido_fijos(caja_p_fumigador, caja_obs_fumigador)[1], contenido_fijos(caja_p_detergente, caja_obs_fumigador)[1], contenido_fijos(caja_p_monotributo, caja_obs_monotributo)[1],contenido_fijos(caja_p_otros1, caja_obs_otros1)[1], contenido_fijos(caja_p_otros2, caja_obs_otros2)[1],contenido_fijos(caja_p_otros3, caja_obs_otros3)[1],costos_fijos]
    guardar_datos_costos(al_excel)
    guardar_datos_obs(al_excel_obs)


def confirmar():
    if caja_total == '':
        messagebox.showinfo(title='Error', message='Ingresar datos numéricos en el registro.')
    else:
        # COSTOS VARIABLESW
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
        caja_p_huevos.delete(0,tk.END)
        caja_q_huevos.delete(0,tk.END)
        caja_t_huevos.delete(0,tk.END)
        caja_p_servilletas.delete(0,tk.END)
        caja_q_servilletas.delete(0,tk.END)
        caja_t_servilletas.delete(0,tk.END)
        caja_p_yerba.delete(0,tk.END)
        caja_q_yerba.delete(0,tk.END)
        caja_t_yerba.delete(0,tk.END)
        caja_p_cafe.delete(0,tk.END)
        caja_q_cafe.delete(0,tk.END)
        caja_t_cafe.delete(0,tk.END)
        caja_p_jamon.delete(0,tk.END)
        caja_q_jamon.delete(0,tk.END)
        caja_t_jamon.delete(0,tk.END)
        caja_p_puerro.delete(0,tk.END)
        caja_q_puerro.delete(0,tk.END)
        caja_t_puerro.delete(0,tk.END)
        caja_p_beren.delete(0,tk.END)
        caja_q_beren.delete(0,tk.END)
        caja_t_beren.delete(0,tk.END)
        caja_p_papa.delete(0,tk.END)
        caja_q_papa.delete(0,tk.END)
        caja_t_papa.delete(0,tk.END)
        caja_p_calabaza.delete(0,tk.END)
        caja_q_calabaza.delete(0,tk.END)
        caja_t_calabaza.delete(0,tk.END)
        # COSTOS FIJOS
        caja_p_alquiler.delete(0,tk.END)
        caja_obs_alquiler.delete(0, tk.END)
        caja_p_luz.delete(0,tk.END)
        caja_obs_luz.delete(0, tk.END)
        caja_p_agua_servicio.delete(0,tk.END)
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
        caja_p_otros1.delete(0,tk.END)
        caja_obs_otros1.delete(0, tk.END)
        caja_p_otros2.delete(0,tk.END)
        caja_obs_otros2.delete(0, tk.END)
        caja_p_otros3.delete(0,tk.END)
        caja_obs_otros3.delete(0, tk.END)
        
        caja_total.delete(0,tk.END)    
        cambiar_tarjeta_valor()


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
    caja_p_huevos.delete(0,tk.END)
    caja_q_huevos.delete(0,tk.END)
    caja_t_huevos.delete(0,tk.END)
    caja_p_servilletas.delete(0,tk.END)
    caja_q_servilletas.delete(0,tk.END)
    caja_t_servilletas.delete(0,tk.END)
    caja_p_yerba.delete(0,tk.END)
    caja_q_yerba.delete(0,tk.END)
    caja_t_yerba.delete(0,tk.END)
    caja_p_cafe.delete(0,tk.END)
    caja_q_cafe.delete(0,tk.END)
    caja_t_cafe.delete(0,tk.END)
    caja_p_jamon.delete(0,tk.END)
    caja_q_jamon.delete(0,tk.END)
    caja_t_jamon.delete(0,tk.END)
    caja_p_puerro.delete(0,tk.END)
    caja_q_puerro.delete(0,tk.END)
    caja_t_puerro.delete(0,tk.END)
    caja_p_beren.delete(0,tk.END)
    caja_q_beren.delete(0,tk.END)
    caja_t_beren.delete(0,tk.END)
    caja_p_papa.delete(0,tk.END)
    caja_q_papa.delete(0,tk.END)
    caja_t_papa.delete(0,tk.END)
    caja_p_calabaza.delete(0,tk.END)
    caja_q_calabaza.delete(0,tk.END)
    caja_t_calabaza.delete(0,tk.END)
    # COSTOS FIJOS
    caja_p_alquiler.delete(0,tk.END)
    caja_obs_alquiler.delete(0, tk.END)
    caja_p_luz.delete(0,tk.END)
    caja_obs_luz.delete(0, tk.END)
    caja_p_agua_servicio.delete(0,tk.END)
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
    caja_p_otros1.delete(0,tk.END)
    caja_obs_otros1.delete(0, tk.END)
    caja_p_otros2.delete(0,tk.END)
    caja_obs_otros2.delete(0, tk.END)
    caja_p_otros3.delete(0,tk.END)
    caja_obs_otros3.delete(0, tk.END)
    
    cambiar_tarjeta_valor()


def checkbox_clicked():
    rta = tarjeta_valor.get()
    return rta


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

### CHECKBOX
tarjeta_valor = tk.IntVar()
tarjeta = ttk.Checkbutton(text='Pago con tarjeta?', variable=tarjeta_valor, command=checkbox_clicked)
tarjeta.place(x=500, y=585)


## COSTOS VARIOS
label_queso = ttk.Label(text='Horma queso  ==> ')
label_queso.place(x=20,y=60)
label_leche = ttk.Label(text='Leche  ==> ')
label_leche.place(x=20,y=85)
label_pollo = ttk.Label(text='Pollo  ==> ')
label_pollo.place(x=20,y=110)
label_carne_picada = ttk.Label(text='Carne Picada  ==> ')
label_carne_picada.place(x=20,y=135)
label_tapa = ttk.Label(text='Tapas  ==> ')
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
label_huevos = ttk.Label(text='Huevos  ==> ')
label_huevos.place(x=20,y=410)
label_servilletas = ttk.Label(text='Servilletas  ==> ')
label_servilletas.place(x=20,y=435)
label_yerba = ttk.Label(text='Yerba  ==> ')
label_yerba.place(x=20,y=460)
label_cafe = ttk.Label(text='Café  ==> ')
label_cafe.place(x=20,y=485)
label_jamon = ttk.Label(text='Jamón  ==> ')
label_jamon.place(x=20,y=510)
label_puerro = ttk.Label(text='Puerro  ==> ')
label_puerro.place(x=20,y=535)
label_beren = ttk.Label(text='Berenjenas  ==> ')
label_beren.place(x=20,y=560)
label_papa = ttk.Label(text='Papas  ==> ')
label_papa.place(x=20,y=585)
label_cala = ttk.Label(text='Calabaza  ==> ')
label_cala.place(x=20,y=610)

## COSTOS FIJOS
label_alquiler = ttk.Label(text='Alquiler  ==> ')
label_alquiler.place(x=500,y=60)
label_luz = ttk.Label(text='Luz  ==> ')
label_luz.place(x=500,y=85)
label_agua_servicio = ttk.Label(text='AYSA ==> ')
label_agua_servicio.place(x=500,y=110)
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
label_otros1 = ttk.Label(text='Otros  => ')
label_otros1.place(x=500,y=285)
label_otros2 = ttk.Label(text='Otros  => ')
label_otros2.place(x=500,y=310)
label_otros3 = ttk.Label(text='Otros  => ')
label_otros3.place(x=500,y=335)

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

caja_q_huevos = ttk.Entry()
caja_q_huevos.place(x=125, y=410,width=80)
caja_q_huevos.insert(tk.END,'')
caja_p_huevos = ttk.Entry()
caja_p_huevos.place(x=235, y=410,width=80)
caja_p_huevos.insert(tk.END,'')
caja_t_huevos = ttk.Entry()
caja_t_huevos.place(x=345, y=410,width=80)
caja_t_huevos.insert(tk.END,'')

caja_q_servilletas = ttk.Entry()
caja_q_servilletas.place(x=125, y=435,width=80)
caja_q_servilletas.insert(tk.END,'')
caja_p_servilletas = ttk.Entry()
caja_p_servilletas.place(x=235, y=435,width=80)
caja_p_servilletas.insert(tk.END,'')
caja_t_servilletas = ttk.Entry()
caja_t_servilletas.place(x=345, y=435,width=80)
caja_t_servilletas.insert(tk.END,'')

caja_q_yerba = ttk.Entry()
caja_q_yerba.place(x=125, y=460,width=80)
caja_q_yerba.insert(tk.END,'')
caja_p_yerba = ttk.Entry()
caja_p_yerba.place(x=235, y=460,width=80)
caja_p_yerba.insert(tk.END,'')
caja_t_yerba = ttk.Entry()
caja_t_yerba.place(x=345, y=460,width=80)
caja_t_yerba.insert(tk.END,'')

caja_q_cafe = ttk.Entry()
caja_q_cafe.place(x=125, y=485,width=80)
caja_q_cafe.insert(tk.END,'')
caja_p_cafe = ttk.Entry()
caja_p_cafe.place(x=235, y=485,width=80)
caja_p_cafe.insert(tk.END,'')
caja_t_cafe = ttk.Entry()
caja_t_cafe.place(x=345, y=485,width=80)
caja_t_cafe.insert(tk.END,'')

caja_q_jamon = ttk.Entry()
caja_q_jamon.place(x=125, y=510,width=80)
caja_q_jamon.insert(tk.END,'')
caja_p_jamon = ttk.Entry()
caja_p_jamon.place(x=235, y=510,width=80)
caja_p_jamon.insert(tk.END,'')
caja_t_jamon = ttk.Entry()
caja_t_jamon.place(x=345, y=510,width=80)
caja_t_jamon.insert(tk.END,'')

caja_q_puerro = ttk.Entry()
caja_q_puerro.place(x=125, y=535,width=80)
caja_q_puerro.insert(tk.END,'')
caja_p_puerro = ttk.Entry()
caja_p_puerro.place(x=235, y=535,width=80)
caja_p_puerro.insert(tk.END,'')
caja_t_puerro = ttk.Entry()
caja_t_puerro.place(x=345, y=535,width=80)
caja_t_puerro.insert(tk.END,'')

caja_q_beren = ttk.Entry()
caja_q_beren.place(x=125, y=560,width=80)
caja_q_beren.insert(tk.END,'')
caja_p_beren = ttk.Entry()
caja_p_beren.place(x=235, y=560,width=80)
caja_p_beren.insert(tk.END,'')
caja_t_beren = ttk.Entry()
caja_t_beren.place(x=345, y=560,width=80)
caja_t_beren.insert(tk.END,'')

caja_q_papa = ttk.Entry()
caja_q_papa.place(x=125, y=585,width=80)
caja_q_papa.insert(tk.END,'')
caja_p_papa = ttk.Entry()
caja_p_papa.place(x=235, y=585,width=80)
caja_p_papa.insert(tk.END,'')
caja_t_papa = ttk.Entry()
caja_t_papa.place(x=345, y=585,width=80)
caja_t_papa.insert(tk.END,'')

caja_q_calabaza = ttk.Entry()
caja_q_calabaza.place(x=125, y=610,width=80)
caja_q_calabaza.insert(tk.END,'')
caja_p_calabaza = ttk.Entry()
caja_p_calabaza.place(x=235, y=610,width=80)
caja_p_calabaza.insert(tk.END,'')
caja_t_calabaza = ttk.Entry()
caja_t_calabaza.place(x=345, y=610,width=80)
caja_t_calabaza.insert(tk.END,'')

caja_total = ttk.Entry()
caja_total.place(x=500, y=615, width=160)
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

caja_p_agua_servicio = ttk.Entry()
caja_p_agua_servicio.place(x=590, y=110,width=80)
caja_p_agua_servicio.insert(tk.END,'')
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

caja_p_otros1 = ttk.Entry()
caja_p_otros1.place(x=590, y=285,width=80)
caja_p_otros1.insert(tk.END,'')
caja_obs_otros1 = ttk.Entry()
caja_obs_otros1.place(x=680, y=285,width=180)
caja_obs_otros1.insert(tk.END,'')

caja_p_otros2 = ttk.Entry()
caja_p_otros2.place(x=590, y=310,width=80)
caja_p_otros2.insert(tk.END,'')
caja_obs_otros2 = ttk.Entry()
caja_obs_otros2.place(x=680, y=310,width=180)
caja_obs_otros2.insert(tk.END,'')

caja_p_otros3 = ttk.Entry()
caja_p_otros3.place(x=590, y=335,width=80)
caja_p_otros3.insert(tk.END,'')
caja_obs_otros3 = ttk.Entry()
caja_obs_otros3.place(x=680, y=335,width=180)
caja_obs_otros3.insert(tk.END,'')

## BOTONES - MESSAGE BOX
costos = ttk.Button(text='Totalizar costos',command=mult)
costos.place(x=500,y=650)
costos.winfo_class()

confirmacion = ttk.Button(text='Confirmar costos', command=confirmar)
confirmacion.place(x=595,y=650)

boton_borrar = ttk.Button(text='Borrar datos', command=borrar_datos)
boton_borrar.place(x=345,y=650)

ventana.mainloop()

