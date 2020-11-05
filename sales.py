import pandas as pd
import numpy as np

precios = {'empanadas': 60, 'tartas': 200,
           'platos': {'plato_sin_guar': 230, 'plato': 280, 'tortilla': 220, 'ensalada': 250, 'ensa_chica': 150,
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
            if 'tar' in e1:
                precio = e2

    elif palabra_clave[:8] == 'Plato S/':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'S/' in e1:
                precio = e2

    elif palabra_clave[:7] == 'Platos':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'tos' in e1:
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
            if 'afe' in e1:
                precio = e2


    elif palabra_clave[:9] == 'Alfajores':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'fajo' in e1:
                precio = e2


    elif palabra_clave[:9] == 'Ensalada':
        for t in lista_precios:
            e1, e2 = t[0], t[1]
            if 'tar' in e1:
                precio = e2


    return precio


sales_dict = {}
for c in columns[:-2]:
    try:
        col_ventas = df_ventas[c]
        col_ventas = np.array(col_ventas.values) * get_price(listado, c)
        sales_dict[c] = col_ventas
        print(f'Correctly stored column ', c)
    except:
        print('Problem storing prduct price')
