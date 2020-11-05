import pandas as pd
import numpy as np
import os, xlwings as xw

precios = {'empanadas': 60, 'tartas': 200,
           'platos': {'plato_sin_guar': 230, 'plato_completo': 280, 'tortilla': 220, 'ensalada': 250, 'ensa_chica': 150,
                      'porcion_papas': 160, 'omelette': 200},
           'cafeteria': {'cafe_chico': 80, 'jarrito': 90, 'cafe_leche': 120, 'lagrima': 90, 'te': 80,
                         'cafe_llevar': 90, 'alfa': 60,'medialuna': 30},
           'postre': {'ensa_fruta': 150,'flan': 100},
           'bebida': {'gaseosa': 80,'agua': 75,'cerveza': 100}}

df_ventas = pd.read_excel('Ventas.xlsx', header=0, index_col=0, parse_dates=True)
df_costos = pd.read_excel('Costos.xlsx', header=0, index_col=0, parse_dates=True)

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

    elif palabra_clave[:7] == 'Platos':
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

    elif palabra_clave[:4] == 'Cafe':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'cafe_chico' in e1:
                precio = e2

    elif palabra_clave[:9] == 'Alfajores':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'alfa' in e1:
                precio = e2


    elif palabra_clave[:5] == 'Media':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'medialuna' in e1:
                precio = e2

    elif palabra_clave[:10] == 'Gaseosa ch':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'gaseosa' in e1:
                precio = e2

    elif palabra_clave[:10] == 'Gaseosa gr':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'agua' in e1:
                precio = e2

    elif palabra_clave[:13] == 'Porción papas':
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
    return precio


def envio_excel(dataframe_ventas, dataframe_ventas_diarias):
    if os.path.exists('data_powerbi.xlsx'):
        wb = xw.Book('data_powerbi.xlsx')
        # SHEET VENTAS GENERAL
        ws = wb.sheets('ventas')
        ws.range('A1').expand().value = dataframe_ventas
        # SHEET VENTAS DIARIAS
        ws2 = wb.sheets('ventas diarias')
        ws2.range('A1').expand().value = dataframe_ventas_diarias
        print('Carga exitosa de datos!')
    else:
        print('Archivo no existente..')


sales_dict = {}
for c in columns[:-3]:
    #if not sales_dict:
    #    sales_dict['Hora'] = df_ventas.index.values
    #else:
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
ventas_final['Total Nuevo'] = np.sum(ventas_final, axis=1)
# Agrupar por fecha
ventas_agrupadas = ventas_final.groupby(ventas_final.index).sum().reset_index()
ventas_agrupadas = ventas_agrupadas.groupby(ventas_agrupadas['index'].dt.date).sum()
# Pasaje a Excel de informacion
envio_excel(ventas_final, ventas_agrupadas)