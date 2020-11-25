from tkinter import *
from tkinter import ttk
import os, time
from openpyxl import Workbook, load_workbook


def comprobar_archivo():
    existe = os.path.exists('Costos.xlsx')
    if existe:
        wb = load_workbook(filename='Costos.xlsx')
        ws_costos = wb['Dato Costos']
        ws_obs = wb['Observaciones']
        ws_uni = wb['Unidades']
        print('Apertura exitosa del archivo.')
    else:
        wb = Workbook()
        ws_costos = wb.create_sheet('Dato Costos',0)
        ws_obs = wb.create_sheet('Observaciones',1)
        ws_uni = wb.create_sheet('Unidades',2)
        titulo_costos = ('Hora transacción','Queso','Leche','Pollo','Carne P.','Tapa','Cebolla','Pan','Tomate','Lechuga','Yogur','Agua','Nalga','Empleados','Acelga','Huevos','Servilletas','Yerba','Cafe','Jamón','Puerro','Berenjenas','Papa','Calabaza','Alquiler','Luz','AYSA','Telefono','ABL','Diario','Fumig.','Deterg.','Monotr.','Otros','Otros','Otros','Tarjeta?','Total Fijos y Variables')
        ws_costos.append(titulo_costos)
        titulos_obs = ('Hora transacción', 'Alquiler','Luz','AYSA','Telefono','ABL','Diario','Fumig.','Deterg.','Monotr.','Otros','Otros','Otros','Tarjeta?', 'Total Costos Fijos')
        ws_obs.append(titulos_obs)
        titulos_uni =('Hora transacción', 'Cantidad Queso', 'Costo Queso', 'Cantidad leche', 'Costo leche', 'Cantidad pollo', 'Costo pollo', 'Cantidad carne picada', 'Costo carne picada', 'Cantidad tapa', 'Costo tapa', 'Cantidad cebolla', 'Costo cebolla', 'Cantidad pan', 'Costo pan', 'Cantidad tomate', 'Costo tomate', 'Cantidad lechuga', 'Costo lechuga', 'Cantidad yogur', 'Costo yogur', 'Cantidad agua', 'Costo agua', 'Cantidad nalga', 'Costo nalga', 'Cantidad empleados', 'Costo empleados', 'Cantidad acelga', 'Costo acelga',  'Cantidad huevos', 'Costo huevos', 'Cantidad servilletas', 'Costo servilletas', 'Cantidad yerba', 'Costo yerba', 'Cantidad cafe', 'Costo cafe', 'Cantidad jamon', 'Costo jamon', 'Cantidad puerro', 'Costo puerro', 'Cantidad berenjena', 'Costo berenjena', 'Cantidad papa', 'Costo papa', 'Cantidad calabaza', 'Costo calabaza',)
        ws_uni.append(titulos_uni)
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


def guardar_datos_unidades(info):
    wb = load_workbook(filename='Costos.xlsx')
    wb['Unidades'].append(info)
    wb.save('Costos.xlsx')
    print("Carga exitosa de las unidades!!")


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
        cantidad = int(caja_cantidad.get())
        precio = int(caja_precio.get())
        variable = int(caja_precio.get()) * int(caja_cantidad.get())
        total.insert('0',variable)
    except:
        if (caja_precio.get() == '') | (caja_cantidad.get() == ''):
            variable = 0
            cantidad = 0
            precio = 0
        else:
            messagebox.showinfo(title='Error', message='Ingresar un número válido')
    return variable, cantidad, precio


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
        queso, q_queso, p_queso = contenido(caja_p_queso, caja_q_queso, caja_t_queso)
        leche, q_leche, p_leche = contenido(caja_p_leche, caja_q_leche, caja_t_leche)
        pollo, q_pollo, p_pollo = contenido(caja_p_pollo, caja_q_pollo, caja_t_pollo)
        carne_p, q_carne_p, p_carne_p = contenido(caja_p_carnep, caja_q_carnep, caja_t_carnep)
        tapa, q_tapa, p_tapa = contenido(caja_p_tapa, caja_q_tapa, caja_t_tapa)
        cebolla, q_cebolla, p_cebolla = contenido(caja_p_cebolla, caja_q_cebolla, caja_t_cebolla)
        pan, q_pan, p_pan = contenido(caja_p_pan, caja_q_pan, caja_t_pan)
        tomate, q_tomate, p_tomate = contenido(caja_p_tomate, caja_q_tomate, caja_t_tomate)
        lechuga, q_lechuga, p_lechuga = contenido(caja_p_lechuga, caja_q_lechuga, caja_t_lechuga)
        yogur, q_yogur, p_yogur = contenido(caja_p_yogur, caja_q_yogur, caja_t_yogur)
        agua, q_agua, p_agua = contenido(caja_p_agua, caja_q_agua, caja_t_agua)
        nalga, q_nalga, p_nalga = contenido(caja_p_nalga, caja_q_nalga, caja_t_nalga)
        empleados, q_empleados, p_empleados = contenido(caja_p_empleados, caja_q_empleados, caja_t_empleados)
        acelga, q_acelga, p_acelga = contenido(caja_p_acelga, caja_q_acelga, caja_t_acelga)
        huevos, q_huevos, p_huevos = contenido(caja_p_huevos, caja_q_huevos, caja_t_huevos)
        servilletas, q_servilletas, p_servilletas = contenido(caja_p_servilletas, caja_q_servilletas, caja_t_servilletas)
        yerba, q_yerba, p_yerba = contenido(caja_p_yerba, caja_q_yerba, caja_t_yerba)
        cafe, q_cafe, p_cafe = contenido(caja_p_cafe, caja_q_cafe, caja_t_cafe)
        jamon, q_jamon, p_jamon = contenido(caja_p_jamon, caja_q_jamon, caja_t_jamon)
        puerro, q_puerro, p_puerro = contenido(caja_p_puerro, caja_q_puerro, caja_t_puerro)
        beren, q_beren, p_beren = contenido(caja_p_beren, caja_q_beren, caja_t_beren)
        papa, q_papa, p_papa = contenido(caja_p_papa, caja_q_papa, caja_t_papa)
        cala, q_cala, p_cala = contenido(caja_p_calabaza, caja_q_calabaza, caja_t_calabaza)

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
        for caja in cajas:
            try:
                caja.delete(0, tk.END)
            except:
                pass

        cambiar_tarjeta_valor()

        # COMPLETA NUEVAMENTE VALORES
        # COSTOS VARIABLES
        queso, q_queso, p_queso = contenido(caja_p_queso, caja_q_queso, caja_t_queso)
        leche, q_leche, p_leche = contenido(caja_p_leche, caja_q_leche, caja_t_leche)
        pollo, q_pollo, p_pollo = contenido(caja_p_pollo, caja_q_pollo, caja_t_pollo)
        carne_p, q_carne_p, p_carne_p = contenido(caja_p_carnep, caja_q_carnep, caja_t_carnep)
        tapa, q_tapa, p_tapa = contenido(caja_p_tapa, caja_q_tapa, caja_t_tapa)
        cebolla, q_cebolla, p_cebolla = contenido(caja_p_cebolla, caja_q_cebolla, caja_t_cebolla)
        pan, q_pan, p_pan = contenido(caja_p_pan, caja_q_pan, caja_t_pan)
        tomate, q_tomate, p_tomate = contenido(caja_p_tomate, caja_q_tomate, caja_t_tomate)
        lechuga, q_lechuga, p_lechuga = contenido(caja_p_lechuga, caja_q_lechuga, caja_t_lechuga)
        yogur, q_yogur, p_yogur = contenido(caja_p_yogur, caja_q_yogur, caja_t_yogur)
        agua, q_agua, p_agua = contenido(caja_p_agua, caja_q_agua, caja_t_agua)
        nalga, q_nalga, p_nalga = contenido(caja_p_nalga, caja_q_nalga, caja_t_nalga)
        empleados, q_empleados, p_empleados = contenido(caja_p_empleados, caja_q_empleados, caja_t_empleados)
        acelga, q_acelga, p_acelga = contenido(caja_p_acelga, caja_q_acelga, caja_t_acelga)
        huevos, q_huevos, p_huevos = contenido(caja_p_huevos, caja_q_huevos, caja_t_huevos)
        servilletas, q_servilletas, p_servilletas = contenido(caja_p_servilletas, caja_q_servilletas, caja_t_servilletas)
        yerba, q_yerba, p_yerba = contenido(caja_p_yerba, caja_q_yerba, caja_t_yerba)
        cafe, q_cafe, p_cafe = contenido(caja_p_cafe, caja_q_cafe, caja_t_cafe)
        jamon, q_jamon, p_jamon = contenido(caja_p_jamon, caja_q_jamon, caja_t_jamon)
        puerro, q_puerro, p_puerro = contenido(caja_p_puerro, caja_q_puerro, caja_t_puerro)
        beren, q_beren, p_beren = contenido(caja_p_beren, caja_q_beren, caja_t_beren)
        papa, q_papa, p_papa = contenido(caja_p_papa, caja_q_papa, caja_t_papa)
        cala, q_cala, p_cala = contenido(caja_p_calabaza, caja_q_calabaza, caja_t_calabaza)

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
    al_excel = [hora, queso,leche,pollo,carne_p,tapa,cebolla,pan,tomate,lechuga,yogur, agua,nalga,empleados,acelga,huevos,servilletas,yerba,cafe,
                jamon,puerro,beren,papa,cala,alquiler,luz,agua_servicio,telefono,abl,diario,fumigador,detergente,monotributo,otros1, otros2, otros3,pago_tarjeta,facturacion]
    al_excel_obs = [hora, contenido_fijos(caja_p_alquiler,caja_obs_alquiler)[1], contenido_fijos(caja_p_luz, caja_obs_luz)[1],
                    contenido_fijos(caja_p_agua_servicio, caja_obs_agua)[1], contenido_fijos(caja_p_telefono, caja_obs_telefono)[1],
                    contenido_fijos(caja_p_abl, caja_obs_abl)[1], contenido_fijos(caja_p_diario, caja_obs_diario)[1],
                    contenido_fijos(caja_p_fumigador, caja_obs_fumigador)[1], contenido_fijos(caja_p_detergente, caja_obs_detergente)[1],
                    contenido_fijos(caja_p_monotributo, caja_obs_monotributo)[1],contenido_fijos(caja_p_otros1, caja_obs_otros1)[1],
                    contenido_fijos(caja_p_otros2, caja_obs_otros2)[1],contenido_fijos(caja_p_otros3, caja_obs_otros3)[1],pago_tarjeta,costos_fijos]
    al_excel_unidades = [hora, q_queso, p_queso, q_leche, p_leche, q_pollo, p_pollo, q_carne_p, p_carne_p, q_tapa, p_tapa, q_cebolla, p_cebolla,
                         q_pan, p_pan, q_tomate, p_tomate, q_lechuga, p_lechuga, q_yogur, p_yogur, q_agua, p_agua, q_nalga, p_nalga,
                         q_empleados, p_empleados, q_acelga, p_acelga, q_huevos, p_huevos, q_servilletas, p_servilletas, q_yerba, p_yerba,
                         q_cafe, p_cafe, q_jamon, p_jamon, q_puerro, p_puerro, q_beren, p_beren, q_papa, p_papa, q_cala, p_cala]
    guardar_datos_costos(al_excel)
    guardar_datos_obs(al_excel_obs)
    guardar_datos_unidades(al_excel_unidades)


def confirmar():
    if caja_total == '':
        messagebox.showinfo(title='Error', message='Ingresar datos numéricos en el registro.')
    else:
        for caja in cajas:
            caja.delete(0, tk.END)

        caja_total.delete(0,tk.END)
        cambiar_tarjeta_valor()


def borrar_datos():
    for caja in cajas:
        caja.delete(0, tk.END)
    cambiar_tarjeta_valor()


def checkbox_clicked():
    rta = tarjeta_valor.get()
    return rta

### EXCEL INICIAL
comprobar_archivo()

### APP DE ESCRITORIO
root = Tk()
root.title('Viejo Caballito - Costos')
root.iconbitmap('./images.ico')
root.geometry('800x800')

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook, width=850, height=850, bg='peru')
my_frame2 = Frame(my_notebook, width=850, height=850, bg='steelblue')
my_frame3 = Frame(my_notebook, width=850, height=850, bg='lime')

my_frame1.pack(fill='both', expand=1)
my_frame2.pack(fill='both', expand=1)
my_frame3.pack(fill='both', expand=1)

my_notebook.add(my_frame1, text='Orange Tab')
my_notebook.add(my_frame2, text='Blue Tab')
my_notebook.add(my_frame3, text='Lime Tab')

### ETIQUETAS
cantidad = ttk.Label(my_frame1, text='Cantidad (Kg./Lit.)').place(x=115,y=40)
precio = ttk.Label(my_frame1, text='Precio por unidad').place(x=230,y=40)
total = ttk.Label(my_frame1, text='Costo total').place(x=355,y=40)
precio_fijos = ttk.Label(my_frame1, text='Costo total').place(x=590, y=40)
obser_fijos = ttk.Label(my_frame1, text='Observación a realizar').place(x=680, y=40)

cv = ttk.Label(my_frame1, text='Panel de costos VARIOS:').place(x=20,y=15)
cf = ttk.Label(my_frame1, text='Panel de costos FIJOS:').place(x=500,y=15)









root.mainloop()