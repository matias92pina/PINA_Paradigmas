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
    menu()


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
                print("Se han agregado los datos exitosamente.\n")
            if opcion=="si":
                #volver a abrir el archivo en "w" para escribirlo desde el inicio
                with open(archivo,"w",newline="") as file_si:
                    file_si_csv=csv.DictWriter(file_si, fieldnames=datos)
                    file_si_csv.writeheader()
                    file_si_csv.writerows(crear_emp())
                print("Se han sobreeescrito los datos. Se agregaron exitosamente.\n")
            menu()
    except IOError:
        print(f"El archivo no existe. Se creará uno nuevo con el nombre ingresado: {archivo}.")
        with open(archivo,"w",newline="") as file_si:
            file_si_csv=csv.DictWriter(file_si, fieldnames=datos)
            file_si_csv.writeheader()
            file_si_csv.writerows(crear_emp())
        print("Se ha creado el archivo y se han guardado los datos exitosamente.\n")
        menu()

#Creamos la función para consultar el gasto hecho por x empleadx
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
                        print(f"Legajo {legajo}: {item[2]} {item[1]} gastó ${tot} y se ha pasado del presupuesto ${tot-limite}\n")
                    else:
                        print(f"Legajo {legajo}: {item[2]} {item[1]} gastó ${tot}\n")
                item=next(empleadx_csv, None)
            menu()
    except IOError:
        print("Verifique el nombre de los archivos ingresados.\n")
        menu()

#Función del menú principal.
def menu():
    print("MENÚ PRINCIPAL.")
    try:
        seleccion=int(input("Ingrese una opción del menú:\n1) Cargar empleadxs.\n2) Consultar gastos por empleadx.\n3) Salir.\n"))
        while seleccion not in range(1,4):
            seleccion=int(input("Ingrese una opción válida del menú:\n1) Cargar empleadxs.\n2) Consultar gastos por empleadx.\n3) Salir.\n"))
        if seleccion==3:
            exit()
        if seleccion==1:
            argumento=input("Ingrese el nombre del archivo donde desea CARGAR empleadxs: ")
            argumento+=".csv"
            cargar_emp(argumento)
        if seleccion==2:
            arg1=input("Ingrese el nombre archivo donde tiene guardados los GASTOS por cada empleadx: ")
            arg1+=".csv"
            arg2=input("Ingrese el nombre del archivo donde tiene guardados los datos básicos de cada empleadx: ")
            arg2+=".csv"
            try:
                legajo=int(input("Ingrese el número de legajo a consultar: "))
                consulta(arg1,arg2,legajo)
            except ValueError:
                legajo=int(input("Ingrese un NÚMERO para indicar el Legajo: "))
                consulta(arg1,arg2,legajo)
    except ValueError:
        print("Ingrese una opción válida.\n")
        menu()
        

menu()

     