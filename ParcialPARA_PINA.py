#Parcial Paradigmas de la programación
# Matías Piña, 1°B
#matias92pina@gmail.com

import csv

def cargar_datos(archivo):
    """Con esta función se agregan empleados al archivo con el formato:
    Legajo, Apellido, Nombre, Cant días vacaciones"""
    cont=0
    try:
        with open(archivo,"r",newline="") as file:
            for linea in file:
                cont +=1
            if cont==0:
                arch_nuevo(archivo)
                print("El archivo se ha creado exitosamente")
            else:
                consulta=input("El archivo ya contiene datos. Desea SOBREESCRIBIR? (si/no): ")
                if consulta=="si":
                    arch_nuevo(archivo)
                    print("Se escribireron los datos exitosamente")
                else:
                    arch_exist(archivo)
                    print("Se agregaron los datos exitosamente")
    except IOError:
        print("Error en el archivo de entrada")
def crear_empleado():
    """Esta función crea un diccionario por empleado y los guarda en una lista
    El empleado se ingresa en formato: Legajo, Apellido, Nombre, Total de vacaciones"""
    seguir="si"
    lista_empleados=[]
    campos=["Legajo","Apellido", "Nombre","Total vacaciones"]
    while seguir=="si":
        empleado={}
        for i in campos:
            empleado[i]=input(f"Ingrese {i} del empleado: ")
            if i=="Legajo" or i=="Total vacaciones":
                empleado[i]=int(empleado[i])
        lista_empleados.append(empleado)
        seguir=input("Desea seguir ingresando empleados? (si/no): ")
    return lista_empleados

def arch_nuevo(archivo):
    """La función crea un archivo nuevo (o sobre escribe uno ya
    existente), agregando el encabezado de campos y la lista
    con los datos de los empleados agregados en la fucnión crear_empleado()"""
    campos=["Legajo","Apellido", "Nombre","Total vacaciones"]
    try:
        with open(archivo, "w", newline="") as nuevo:
            nuevo_csv=csv.DictWriter(nuevo, fieldnames=campos)
            nuevo_csv.writeheader()
            nuevo_csv.writerows(crear_empleado())
    except IOError:
        print("Error en el archivo de entrada")
def arch_exist(archivo):
    """La función agrega la lista de los empleados desde el final, sin sobreescribir"""
    campos=["Legajo","Apellido", "Nombre","Total vacaciones"]
    try:
        with open(archivo, "a", newline="") as nuevo:
            nuevo_csv=csv.DictWriter(nuevo, fieldnames=campos)
            nuevo_csv.writerows(crear_empleado())
    except IOError:
        print("Error en el archivo de entrada")

def consulta_pendientes(archivo1, archivo2, legajo):
     """TLa función toma del archivo las vacaciones ya tomadas por el empleado "legajo", y las resta
     a las vacaciones totales. Así obtenemos la cantidad de dias pendientes."""
     cont=0
     pendientes=0
     with open (archivo1, "r", newline="") as f_tomadas, open(archivo2,"r",newline="") as f_totales:
         for linea in f_tomadas:
             linea=linea.split(";")
             if legajo==linea[0]:
                 cont +=1
         empleado=f_totales.readline()
         for empleado in f_totales:
             empleado=empleado.split(";")
             if empleado[0]== legajo:
                pendientes=int(empleado[3]) - cont
                
         print(f"Legajo {linea[0]}: tiene {pendientes} dias de vacaciones")
             

def consulta_legajos():
    ARCHIVO= input("Ingrese el nombre del archivo donde se va cargar/tiene cargados los datos. Recuerde agregar la extensión del mismo: ")
    while True:
        opcion=input("Ingrese una opción del menú:\n1. Cargar nuevo legajo\n2. Consultar días disponibles de vacaciones\n3. Salir")
        if opcion=="3":
            exit()
        if opcion=="1":
            cargar_datos(ARCHIVO)
        if opcion=="2":
            ARCHIVO_1=input("Ingrese el nombre del archivo donde están cargados los días ya tomados por los empleados. Recuerde agregar la extensión del mismo: ")
            legajo=input("Ingrese el número de legajo a consultar")
            consulta_pendientes(ARCHIVO_1, ARCHIVO, legajo)
        
