import pandas as pd

def accidente(data: pd.DataFrame) -> dict:
    # Filtrar los datos para obtener solo aquellos registros que tengan una dirección con el estándar "CALLE_NUMERO".
    data = data[data['DIRECCION'].str.contains('CALLE_NUMERO')]

    # Filtrar los datos para obtener solo aquellos registros que correspondan a la calle 30 de Barranquilla.
    data = data[data['DIRECCION'].str.contains('CALLE 30')]

    # Calcular la cantidad total de accidentes por gravedad en la calle 30 de Barranquilla.
    accidentes_gravedad = data.groupby('GRAVEDAD')['GRAVEDAD'].count()

    # Calcular la clase de accidente más frecuente en la calle 30 de Barranquilla.
    clase_mas_accidente = data.groupby('CLASE')['CLASE'].count().idxmax()
    cantidad_accidentes = data.groupby('CLASE')['CLASE'].count().max()

    # Encontrar la máxima cantidad de heridos reportados en un accidente de la calle 30 en Barranquilla.
    max_heridos = data['CANT_HERIDOS'].max()
    fecha_max_heridos = data[data['CANT_HERIDOS'] == max_heridos]['FECHA'].iloc[0].strftime('%d/%m/%Y')

    # Crear un diccionario con los resultados y retornarlo.
    resultados = {
        'clase_mas_accidente': (clase_mas_accidente, cantidad_accidentes),
        'accidentes_gravedad': accidentes_gravedad.to_dict(),
        'cantidad_max_heridos': (max_heridos, fecha_max_heridos)
    }
    return resultados
"""La función toma como parámetro un DataFrame que contiene los accidentes registrados en Barranquilla almacenados en un archivo csv. Luego, filtra los datos para obtener solo aquellos registros que tengan una dirección con el estándar "CALLE_NUMERO" y que correspondan a la calle 30 de Barranquilla.

A continuación, se calcula la cantidad total de accidentes por gravedad en la calle 30 de Barranquilla mediante la función groupby de pandas. También se calcula la clase de accidente más frecuente en la calle 30 de Barranquilla mediante la función idxmax() de pandas.

Finalmente, se encuentra la máxima cantidad de heridos reportados en un accidente de la calle 30 en Barranquilla mediante la función max() de pandas y se obtiene la fecha correspondiente al registro con esa cantidad de heridos mediante la función iloc() de pandas y strftime"""





