#Recuperatorio Paradigmas de la programación. IFTS n°18
#Alumno: PIÑA, Matías- 1°B
#Profesora: RODRIGUEZ, Eliana

import csv

#1ro, hay que cargar datos de empleadxs: (int)legajo, apellido, nombre
#Hacemos función para crear empleadxs

def crear_emp():
    datos=["Legajo","Apellido","Nombre"]
    lista_emp=[]
    seguir="si"
    while seguir=="si":
        empleadx={}
        for i in datos:
            empleadx[i]=input(f"Ingrese {i} de empleadx: ")
            if i=="Legajo":
                try:
                    empleadx[i]=int(empleadx[i])
                except ValueError:
                    print(f"Para indicar el Legajo debe ingresar un NÚMERO entero.")
                    empleadx[i]=input(f"Ingrese {i} de empleadx: ")
        lista_emp.append(empleadx)
        seguir=input("Desea seguir ingresadno empleadxs? (si/no)\n").lower()
        while seguir!="si" and seguir !="no":
            seguir=input("Ingrese una opción válida: si/no\n").lower()
    return lista_emp


#Creemos la función que va a guardar los datos en un archivo.
def cargar_emp(archivo):
    datos=["Legajo","Apellido","Nombre"]
    try:
        with open(archivo,"r",newline="") as file:
            opcion=input("El archivo ya existe. Desea SOBREESCRIBIR los datos? Si selecciona 'si' perderá todos los datos cargados al momento: (si/no)\n")
            while opcion!="si" and opcion!="no":
                opcion=input("Seleccione una opción válida: si/no\n")
            if opcion=="no":
                #volver a abrir el archivo en  "a" para escribir desde la última posición.
                with open(archivo,"a",newline="") as file:
                    file_csv=csv.DictWriter(file, fieldnames=datos)
                    file_csv.writerows(crear_emp())
                print("Se han agregado los datos exitosamente.")
            if opcion=="si":
                #volver a abrir el archivo en "w" para escribirlo desde el inicio
                with open(archivo,"w",newline="") as file_si:
                    file_si_csv=csv.DictWriter(file_si, fieldnames=datos)
                    file_si_csv.writeheader()
                    file_si_csv.writerows(crear_emp())
                print("Se han sobreeescrito los datos. Se agregaron exitosamente.")
    except IOError:
        print(f"El archivo no existe. Se creará uno nuevo con el nombre ingresado: {archivo}.")
        with open(archivo,"w",newline="") as file_si:
            file_si_csv=csv.DictWriter(file_si, fieldnames=datos)
            file_si_csv.writeheader()
            file_si_csv.writerows(crear_emp())
        print("Se ha creado el archivo y se han guardado los datos exitosamente.")

def consulta(archivo1, archivo2, legajo):
    
    try:
        with open(archivo1, "r", newline="") as gastos, open (archivo2, "r", newline="") as empleadx:
            gastos_csv=csv.reader(gastos,delimiter=";")
            empleadx_csv=csv.reader(empleadx, delimiter=";")
            
            linea=next(gastos_csv, None)
            linea=next(gastos_csv, None)
            item=next(empleadx_csv, None)
            item=next(empleadx_csv, None)

            tot=0
            limite=5000
            while linea:
                if int(linea[0])==legajo:
                    importe=int(linea[1])
                    tot += importe
                linea=next(gastos_csv, None)
            while item:
                if int(item[0])==legajo:
                    if tot>limite:
                        print(f"Legajo {legajo}: {item[2]} {item[1]} gastó ${tot} y se ha pasado del presupuesto ${tot-limite}")
                    else:
                        print(f"Legajo {legajo}: {item[2]} {item[1]} gastó ${tot}")
                item=next(empleadx_csv, None)
    except IOError:
        print("Verifique el nombre de los archivos ingresados.")







                