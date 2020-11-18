import pandas as pd
import numpy as np
import os, xlwings as xw
import datetime as dt

# Almacenamiento de precios
precios = {'empanadas': 60, 'tartas': 200,
           'platos': {'plato_sin_guar': 230, 'plato_completo': 280, 'tortilla': 220, 'ensalada': 250, 'ensa_chica': 150,
                      'porcion_papas': 160, 'omelette': 200},
           'cafeteria': {'cafe_chico': 80, 'jarrito': 90, 'cafe_leche': 120, 'lagrima': 90, 'te': 80,
                         'cafe_llevar': 90, 'alfa': 60,'medialuna': 30},
           'postre': {'ensa_fruta': 150,'flan': 100},
           'bebida': {'gaseosa': 80,'agua': 75,'cerveza': 100}}

# Descarga de datos del excel de la aplicacion
df_ventas = pd.read_excel('Ventas.xlsx', engine="openpyxl", header=0, index_col=0, parse_dates=True)
df_costos = pd.read_excel('Costos.xlsx', engine="openpyxl", header=0, index_col=0, parse_dates=True)

# Extraccion de precios del diccionario de precios en formato de lista de tuplas para ser utilizado.
lista_productos = []
lista_precios = []

for k, v in precios.items():
    if (type(k) == str) & (type(v) == int):
        lista_productos.append(k)
        lista_precios.append(v)

    elif (type(k) == str) & (type(v) == dict):
        for d in v.items():
            p, q = d[0], d[1]
            lista_productos.append(p)
            lista_precios.append(q)

listado = list(zip(lista_productos, lista_precios))

productos_aplicacion = []
i = 0
for ind, row in df_ventas.iterrows():
    if i < 3:
        if i == 0:
            prods = row.index.values
            for e in prods:
                productos_aplicacion.append(e)
        else:
            pass
    i+=1

columns = df_ventas.columns.values

# Creo funciones de obtencion de precio y envio de informacion procesada a excel
def get_price(lista_precios, palabra_clave):
    if palabra_clave[:3] == 'Emp':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'emp' in e1:
                precio = e2

    elif palabra_clave[:3] == 'Tar':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'tartas' in e1:
                precio = e2

    elif palabra_clave[:8] == 'Plato S/':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'sin_guar' in e1:
                precio = e2

    elif 'Plato del Día' in palabra_clave:
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'plato_completo' in e1:
                precio = e2

    elif palabra_clave[:8] == 'Tortilla':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'illa' in e1:
                precio = e2

    elif palabra_clave[:9] == 'Ensalada':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'lada' in e1:
                precio = e2

    elif palabra_clave[:5] == 'Ensa.':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if '_chica' in e1:
                precio = e2

    elif palabra_clave[:7] == 'Cafe ch':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'cafe_chico' in e1:
                precio = e2

    elif palabra_clave[:7] == 'Jarrito':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'jarrito' in e1:
                precio = e2

    elif palabra_clave[:7] == 'Cafe C/':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'cafe_leche' in e1:
                precio = e2

    elif palabra_clave[:8] == 'Cafe P/l':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'cafe_llevar' in e1:
                precio = e2

    elif palabra_clave[:2] == 'Te':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'te' in e1:
                precio = e2

    elif palabra_clave[:7] == 'Lagrima':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'lagrima' in e1:
                precio = e2

    elif palabra_clave[:9] == 'Alfajores':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'alfa' in e1:
                precio = e2

    elif 'Medialunas' in palabra_clave:
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'medialuna' in e1:
                precio = e2

    elif palabra_clave[:6] == 'Gaseos':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'gaseosa' in e1:
                precio = e2

    elif palabra_clave[:8] == 'Ensa. Fr':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'ensa_fruta' in e1:
                precio = e2

    elif palabra_clave[:6] == 'Omelet':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'ome' in e1:
                precio = e2

    elif 'Agua' in palabra_clave:
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'agua' in e1:
                precio = e2

    elif palabra_clave[:13] == 'Papas':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'papas' in e1:
                precio = e2

    elif palabra_clave[:12] == 'Porción puré':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'papas' in e1:
                precio = e2

    elif palabra_clave[:5] == 'Cerve':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'cerv' in e1:
                precio = e2

    elif 'Flan' in palabra_clave:
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'flan' in e1:
                precio = e2

    return precio

def envio_excel(dataframe_ventas, dataframe_ventas_diarias, dataframe_costos, dataframe_costos_diarios):
    if os.path.exists('data_powerbi.xlsx'):
        wb = xw.Book('data_powerbi.xlsx')
        # SHEET VENTAS GENERAL
        ws = wb.sheets('ventas')
        ws.range('A1').expand().value = dataframe_ventas
        # SHEET VENTAS DIARIAS
        ws2 = wb.sheets('ventas diarias')
        ws2.range('A1').expand().value = dataframe_ventas_diarias
        # SHEET COSTOS GENERAL
        ws3 = wb.sheets('costos')
        ws3.range('A1').expand().value = dataframe_costos
        # SHEET COSTOS DIARIOS
        ws4 = wb.sheets('costos diarios')
        ws4.range('A1').expand().value = dataframe_costos_diarios
        print('Carga exitosa de datos!')
    else:
        print('Archivo no existente..')

# Almaceno informacion de PxQ en el diccionario "sales_dict" para luego hacer un dataframe
sales_dict = {}
for c in columns[:-3]:
        try:
            col_ventas = df_ventas[c]
            col_ventas = np.array(col_ventas.values) * get_price(listado, c)
            sales_dict[c] = col_ventas
            print(f'Correctly stored column ', c)
        except:
            sales_dict[c] = np.zeros(len(df_ventas))
            print('Stored zeros')

# Calcular ventas totales
ventas_final = pd.DataFrame(sales_dict, columns=columns[:-3], index=df_ventas.index.values)
descuentos = df_ventas.loc[:, ['Descuentos', 'Tarjeta D.']]
ventas_final = pd.merge(ventas_final, descuentos, left_index=True, right_index=True)
ventas_final = ventas_final.iloc[1:]
ventas_final['Total Nuevo'] = np.sum(ventas_final, axis=1)
# Agrupar por fecha
ventas_agrupadas = ventas_final.groupby(ventas_final.index).sum().reset_index()
ventas_agrupadas = ventas_agrupadas.groupby(ventas_agrupadas['index'].dt.date).sum()

# Calcular costos totales
costos_final = df_costos.reset_index()
dates = []
for d in costos_final['Hora transacción'].values:
    d_new = pd.to_datetime(d)
    year = d_new.year
    month = d_new.month
    day = d_new.day
    dates.append((int(year),int(month),int(day)))

n_dates = []
for d in dates:
    year,month,day = d
    d_n = dt.datetime(year,month,day)
    n_dates.append(d_n)

costos_agrupados = costos_final
costos_agrupados['Hora transacción'] = n_dates
costos_agrupados = costos_agrupados.groupby('Hora transacción').sum()
for i in range(len(costos_agrupados)):
    if i < 9:
        costos_agrupados.Empleados.values[i] = 660
        costos_agrupados.Huevos.values[i] = 0
    else:
        costos_agrupados.Empleados.values[i] = 875
        costos_agrupados.Huevos.values[i] = 0

costos_agrupados = costos_agrupados[costos_agrupados.columns.values[:-1]]
costos_agrupados['Final'] = np.sum(costos_agrupados, axis=1)
costos_final.set_index('Hora transacción', inplace=True)

for i in range(len(costos_final)):
    costos_final.Huevos.values[i] = 0
for i in range(len(costos_final)):
    costos_final.Empleados.values[i] = 0

costos_final = costos_final[costos_final.columns.values[:-1]]
costos_final['Final'] = np.sum(costos_final, axis=1)

# Pasaje a Excel de informacion
envio_excel(ventas_final, ventas_agrupadas, costos_final , costos_agrupados)

