import pandas as pd

def distribucion_genero_estrato(data: pd.DataFrame, estrato: int):
    # Filtrar los estudiantes del estrato seleccionado
    data = data[data['ESTRATO'] == estrato]
    
    # Calcular la frecuencia de los estudiantes por género
    freq_genero = data['GENERO'].value_counts()
    
    # Crear un DataFrame con los resultados
    df_genero = pd.DataFrame({'F': [freq_genero['F']], 'M': [freq_genero['M']]})
    
    # Mostrar el diagrama de torta
    df_genero.plot.pie(y=[0, 1], labels=['Femenino', 'Masculino'], autopct='%1.1f%%')
    
    return df_genero.to_dict()

def diez_mejores(data: pd.DataFrame):
    # Calcular el promedio del puntaje global por departamento
    data_prom = data.groupby('DEPARTAMENTO')['PUNT_GLOBAL'].mean().sort_values(ascending=False)
    
    # Tomar los 10 mejores departamentos
    data_top10 = data_prom.head(10)
    
    # Crear un DataFrame con los resultados
    df_top10 = pd.DataFrame(data_top10)
    df_top10.plot.barh()
    
    return df_top10.to_dict()

def iniciar_aplicacion(data: pd.DataFrame, estrato: int) -> None:
    dict_genero_estrato = distribucion_genero_estrato(data, estrato)
    dict_diez_mejores = diez_mejores(data)
    dict_final = { 'ESTRATO': dict_genero_estrato, 'PUNT_GLOBAL': dict_diez_mejores }
    print(dict_final)

# Iniciar la aplicación
iniciar_aplicacion(data, 4)