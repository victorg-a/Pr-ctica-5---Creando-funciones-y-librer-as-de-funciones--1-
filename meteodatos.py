#! /usr/bin/env-python
# -*- coding: utf-8 -*-

# meteodatos - librería para la consulta de datos meteorológicos obtenidos desde
# las bases de datos disponibles en https://climatologia.meteochile.gob.cl/application/index/menuTematicoEmas
# versión: 0.1
# fecha: abril de 2023
# github: cmoralesd/aprendiendo-python


def leer_archivo(nombre_archivo):
    # nombre_archivo: un archivo csv obtenido desde https://climatologia.meteochile.gob.cl/application/index/menuTematicoEmas
    # retorna: el contenido del archivo como una lista, cuyos elementos son las
    #          líneas del archivo original, sin el caracter final '\n'
    contenido = []
    try:
        with open(nombre_archivo) as archivo:
            for linea in archivo:
                contenido.append(linea[:-1])
        print(f'El archivo fue leido correctamente: {nombre_archivo}')
    except:
        print(f'ERROR: No se pudo abrir el archivo: {nombre_archivo}')
    return contenido  
    

def datos_registrados(datos):
    # parametros:
    #   datos[], es una lista con una fila de encabezado
    # retorna:
    #   una lista con los nombres encontrados en la fila de cabecera
    datos_encontrados = datos[0].split(';')[0]
    return datos_encontrados


def filtrar_cabecera(datos, filtro):
    # datos: la lista con los datos leidos desde el archivo csv
    # filtro: una variable 'str' con el nombre de cabecera que se desea filtrar
    # retorna: una lista con todas las filas de 'datos', pero conteniendo únicamente los datos bajo el nombre 'filtro'.
    #          Los datos que representan números están en formato numérico correspondiente (int o float)

    # identificamos el índice de columna para 'filtro'
    index = datos[0].split(';').index(filtro)
    datos_filtrados = []
    for fila in datos:
        valor = fila.split(';')[index]
        if valor.isnumeric():
            valor = int(valor)
        else:
            try:
                valor = float(valor)
            except:
                pass
        datos_filtrados.append(valor)     
    return datos_filtrados
        
 
def filtrar_dia(datos, dia):
    # datos: una lista cuyas filas contienen los datos agrupados como una cadena de texto
    # dia:   el día que se desea filtrar, en formato 'AAAA-MM-DD', ejemplo: '2023-03-01'
    # retorna: la misma lista 'datos', pero conteniendo únicamente las filas
    #          que coinciden con 'dia' y manteniendo la cabecera
    
    # TODO: Escriba su código aquí
    # ---------------------------------------------
    
    datos_filtrados = [] #lista nro 1
    filtro = datos[0] #lista nro 2

    #agregar datos
    for linea in datos[1:]: #iterando datos de la lista 1
        if dia in linea: #comparando si linea coincide con 'dia'
            datos_filtrados.append(linea) #agrega a la lista
    

    datos_filtrados.insert(0,filtro) #inserta en la primera fila la cabecera
    # ---------------------------------------------
    
    return datos_filtrados #retorna la misma lista 'datos', pero conteniendo únicamente las filas
    # reemplace la lista vacía [] por el resultado de su código


def estadisticas_dia(datos, dia):
    # datos: una lista con datos leidos desde la base de datos meteorológicos,
    #        mediante la función 'leer_archivo()'
    # dia:   el día que se desea reportar, en formato 'AAAA-MM-DD', ejemplo: '2023-03-01'
    # retorna: tmax, tmin, tmedia, la temperatura máxima, mínima y promedio para el día.
    tmax = tmin = tmedia = 0
    
    # TODO: Escriba su código aquí
    # ---------------------------------------------
        
    Datos_ordenados=[] #lista nro 3
    
    #ordenar los datos requeridos para filtrar los datos de temp.
    
    Datos_ordenados = filtrar_dia(datos,dia) #trae los datos del dia indicado
    Temp_filtrada = filtrar_cabecera(Datos_ordenados,"ts") #trae los datos de la cabecera 'ts'
    Temp_filtrada.pop(0) #elimina la cabecera 'ts'

    #temperaturas: maxima, minima y el resultado de la media.
    
    tmax= max(Temp_filtrada) #se obtiene la temperatura máxima
    
    tmin= min(Temp_filtrada) #se obtiene la temperatura mínima
    
    tmedia= round(sum(Temp_filtrada)/len(Temp_filtrada),1) #se obtiene la temperatura media
    # ---------------------------------------------
    # Su código termina aquí, luego se retornan los datos calculados
    
    return tmax, tmin, tmedia #retorna las temperaturas máxima, mínima y promedio
    
  
