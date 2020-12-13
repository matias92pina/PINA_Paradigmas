#Final Paradigmas de programación 2/2020. IFTS N°18
#Matías Piña- matias92pina@gmail.com- 1°B
#Prof: Eliana Rodriguez.


#Del archivo clientes.csv, tuve que ingresar manualmente la linea 3: Asunción Ropero Landa,Camino de Ángel Morell 41 Puerta 9,16432378,2016-04-23,juan00@yanez.com,Nexos S.A
#y linea 91: Miguel Ángel Valbuena Aznar,Paseo Julio Jimenez 24,30931091,2012-07-22,adanfatima@alberto.com,Madre Agencia
#porque al ejecutar el archivo recibía el error:
#  File "C:\Users\Usuario\AppData\Local\Programs\Python\Python38-32\lib\encodings\cp1252.py", line 23, in decode
#    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 293: character maps to <undefined>
#Modificada la linea 59 dle archivo viajes.csv. El importe del viaje estaba en otro formado: "2,222.00"

import csv, logging, datetime

def volver_menu():
    """Función para consultar si volvemos al menú principal o cerramos el programa"""
    cont=int(input("Ingrese 1 para volver al menú o 0 para salir: "))
    try:
        while cont != 0 and cont!=1:
            cont=int(input("Seleccione una opción válida: 1 para volver al menú, 0 para salir del programa: "))
        if cont==0:
            print("Hasta pronto!")
            exit()
        else:
            menu()
    except ValueError:
        print("Selecciona una opción válida del menú.")
        volver_menu()

def consulta_cliente_nom(nombre, archivo_us):
    """Función para realizar la consulta de los datos personales de usuarios. Búsuqeda por nombre. No incluye viajes realizados."""
    nombre=nombre.lower()
    cont=0
    try:
        with open(archivo_us,"r",newline="") as file:
            file_csv=csv.reader(file,delimiter=",")
            linea=next(file_csv, None)
            while linea:
                cliente=linea[0].lower()
                if nombre in cliente:
                    print(f"----\nCliente: {linea[0]}, Documento: {linea[2]},Empresa: {linea[5]}, Dirección: {linea[1]}, Fecha de alta: {linea[3]}, Email: {linea[4]}\n----\n")
                    cont+=1
                linea=next(file_csv, None)
            if cont==0:
                print("----\nEl nombre ingresado no se encuentra en el archivo consultado.\n----\n")

            volver_menu()

    except IOError:
        print("----\nVerifique el nombre del archivo que está consultado.\n----\n")
        menu()

def consulta_cliente_doc(documento,archivo_us,archivo_via):
    """Función para realizar la consulta de los viajes realizados por cada usuario. Búsuqeda por número de documento. Incluye datos personales."""
    cont=0
    esta=0
    tot=0.0
    try:
        with open(archivo_us,"r",newline="") as file, open(archivo_via,"r",newline="") as file_v:
            file_csv=csv.reader(file,delimiter=",")
            file_v_csv=csv.reader(file_v,delimiter=",")
            linea=next(file_csv, None)
            linea=next(file_csv, None)
            renglon=next(file_v_csv, None)
            renglon=next(file_v_csv, None)
            while linea:
                cliente=linea[2]
                if documento==cliente:
                    esta+=1
                    print("----\n",cliente,"\n----\n")
                    print("----\n",linea,"\n----\n")
                    print("Viajes realizados.")
                linea=next(file_csv, None)
            if esta==0:
                print("El documento ingresado no se encuentra en los archivos.")
                volver_menu()
            while renglon:
                documento=int(documento)
                monto=float(renglon[2])
                if documento==int(renglon[0]):
                    cont+=1
                    tot+=monto
                    print(renglon[1]," $",renglon[2])
                renglon=next(file_v_csv, None)
            print("----\n Cantidad de viajes:",cont,"Total: $","{:.2f}".format(tot), "\n----\n")
            volver_menu()
    except IOError:
        print("----\nVerifique el nombre del archivo que está consultado.\n----\n")
        exit()


def consulta_empresa_us(empresa,archivo_us):
    """Función para consultar la cantidad de usuarios que pertecen a una empresa. Búqueda por nombre. No incluye viajes realizados."""
    empresa=empresa.lower()
    usuarios=[]
    cont=0
    try:
        with open(archivo_us,"r",newline="") as file:
            file_csv=csv.reader(file,delimiter=",")
            linea=next(file_csv, None)
            while linea:
                companya=linea[5].lower()
                if empresa in companya:
                    usuarios.append(linea)
                    consulta=linea[5]
                    cont+=1
                linea=next(file_csv, None)
            if cont != 0:
                print(f"----\nEmpresa: {consulta}")
                print(f"Total de usuarios: {cont}\n----\n")
                for i in usuarios:
                    print(i)
            else:
                print("----\nEl nombre de empresa ingresado no existe en el archivo consultado.\n----\n")
            volver_menu()
    except IOError:
        print("----\nVerifique el nombre del archivo que está consultado.\n----\n")
        menu()
    except IndexError:
        print("----\nHubo un error. Es probable que una fila esté completa con espacios vacíos. Complétela o elimínela.\n----\n")
        menu()


def consulta_empresa_tot(empresa, archivo_us, archivo_via):
    """Función para consultar el total gastado en viajes por empresa. No incluye detalle de los viajes."""
    empresa=empresa.lower()
    usuarios=[]
    esta=0
    total=0.0
    try:
        with open(archivo_us,"r",newline="") as f_client, open(archivo_via,"r",newline="") as f_viajes:
                client_csv=csv.reader(f_client,delimiter=",")
                viajes_csv=csv.reader(f_viajes,delimiter=",")
                linea=next(client_csv, None)
                renglon=next(viajes_csv, None)
                renglon=next(viajes_csv, None)
                while linea:
                    companya=linea[5].lower()
                    if empresa in companya:
                        usuarios.append(linea)
                        consulta=linea[5]
                        esta+=1
                    linea=next(client_csv, None)
                if esta==0:
                    print("----\nEl nombre de empresa ingresado no existe en el archivo consultado.\n----\n")
                    volver_menu()
                while renglon:
                    importe=float(renglon[2])
                    for i in usuarios:
                        if i[2]==renglon[0]:
                            total+=importe
                    renglon=next(viajes_csv, None)
                print("----\n",consulta,"Gasto total: $","{:.2f}".format(total),"\n----\n") #Este format redondea en 2 decimales.
                volver_menu()
    except IOError:
        print("----\nVerifique el nombre del archivo que está consultado.\n----\n")
        menu()

def validacion_clientes(archivo_us):
    try:
        with open(archivo_us, "r",newline="") as file:
            file_csv=csv.reader(file,delimiter=",")
            linea=next(file_csv, None)
            linea=next(file_csv, None)
            hay_error=False
            cont=1
            while linea:
                if len(linea)!=6:
                    print(f"Linea {cont}: verifique los campos completados en esta linea. Debe contener exactamente 6 campos.")
                    hay_error=True
                if len(linea[2])<7 or len(linea[2])>8 :
                    print(f"Linea {cont}: verifique el número de documento, el mismo debe contener entre 7 y 8 números.")
                    hay_error=True
                if "@" not in linea[4] or "." not in linea[4]:
                    print(f"Linea {cont}: verifique el correo electrónico. ")
                    hay_error=True
                for i in linea:
                    if i=="":
                        print(f"Linea {cont}: un campo está vacío.")
                        hay_error=True
                cont+=1
                linea=next(file_csv, None)

            if hay_error==True:
                print("Verifique el archivo", archivo_us, "y vuelva a inciar el programa.")
                exit()

    except IOError:
        print("Verifique el archivo", archivo_us, "y vuelva a inciar el programa.")
        exit()
    except UnicodeDecodeError:
        print("Verifique el formato de texto del archivo,", archivo_us)
        exit()

def validacion_viajes(archivo_via):
    try:
        with open(archivo_via,"r",newline="") as file:
            file_csv=csv.reader(file, delimiter=",")
            linea=next(file_csv, None)
            linea=next(file_csv, None)
            hay_error=False
            cont=1
            while linea:
                if len(linea)!=3:
                    print(f"Linea {cont}: verifique los campos completados en esta linea. Debe contener exactamente 3 campos.")
                    hay_error=True    
                if len(linea[0])<7 or len(linea[0])>8 :
                    print(f"Linea {cont}: verifique el número de documento, el mismo debe contener entre 7 y 8 números.")
                    hay_error=True
                try:
                    monto=linea[2].split(".")
                    if len(monto[1])!=2:
                        print(f"Linea {cont}: verifique el monto del viaje. Debe contener 2 decimales.")
                        hay_error=True
                except IndexError:
                    print(f"Linea {cont}: verifique el monto del viaje (debe contener 2 decimales) y los campos completados(deben ser 3 exactamente)")
                    hay_error=True
                for i in linea:
                    if i=="":
                        print(f"Linea {cont}: un campo está vacío.")
                        hay_error=True
    
                cont+=1
                linea=next(file_csv, None)

            if hay_error==True:
                print("Verifique el archivo", archivo_via, "y vuelva a inciar el programa.")
                exit()

    except IOError:
        print("Verifique el archivo", archivo_via, "y vuelva a inciar el programa.")
        exit()
    except UnicodeDecodeError:
        print("Verifique el formato de texto del archivo,", archivo_via)
        exit()

def menu():
    try:
        print("\nSelecciona una opción del menú.")
        logging.basicConfig(filename="historial_acciones.log",filemode="a",format="%(message)s",level=logging.INFO)
        #filename: nombre del archivo / filemode: modo de apertura / format: formato de las lineas del archivo que vamos a escribir
        #level: tipo de mensajes que vamos a guardar.

        logging.info("Acceso a menú.")
        #Tipo de mensaje y mensaje.

        seleccion=int(input("\t1) Consulta de CLIENTE por NOMBRE\n\t2) Consulta de CLIENTE por DOCUMENTO\n\t3) Consulta de EMPRESA\n\t4) Consulta de GASTO TOTAL por EMPRESA\n\t5) Salir.\n\t"))
        while seleccion not in range(1,6):
            seleccion=int(input("Por favor, seleccioná una opción válida del menú:\n\t1) Consulta de CLIENTE por NOMBRE\n\t2) Consulta de CLIENTE por DOCUMENTO\n\t3) Consulta de EMPRESA\n\t4) Consulta de GASTO TOTAL por EMPRESA\n\t5) Salir.\n\t"))
        if seleccion==5: #Salida
            print("Hasta pronto!")
            exit()

        if seleccion==1: #Consulta de usuarios por nombre.
            nombre=input("Ingrese el nombre de Cliente a buscar: ")
            while not nombre.isalpha():
                print("Debe ingresar un nombre o apellido. Sólo letras.")
                nombre=input("Ingrese el nombre del CLIENTE a buscar: ")
            logging.info("Consulta de usuarios por NOMBRE.")
            consulta_cliente_nom(nombre,file_usuarios)

        if seleccion==2:
            documento=input("Ingrese el número de documento de Cliente a consultar: ")
            while not documento.isdigit():
                print("El número de documento debe expresarlo sólo en números.")
                documento=input("Ingrese el número de documento a consultar: ")
            while len(documento)<7 or len(documento)>8:
                print("El número de documento debe contener entre 7 y 8 caracteres.")
                documento=input("Ingrese el número de documento a consultar: ")
            logging.info("Consulta de usuario por NÚMERO DE DOCUMENTO.")
            consulta_cliente_doc(documento,file_usuarios,file_viajes)

        if seleccion==3: #Consulta de total de usuarios x empresa.
            #No validamos el tipo de string que ingresa en Empresa porque podría agregarse alguna que sea alfanumérica o tenga símbolos en el nombre. 
            empresa=input("Ingrese el nombre de la EMPRESA a consultar: ")
            logging.info("Consulta del TOTAL DE USUARIOS por Empresa.")
            consulta_empresa_us(empresa, file_usuarios)

        if seleccion==4: #Consulta de total gastado por empresa
            logging.info("Consulta de TOTAL DE GASTOS por Empresa")
            company=input("Ingrese el nombre de la empresa a consultar: ")
            consulta_empresa_tot(company, file_usuarios,file_viajes)

    except ValueError:
        print("Las opciones del menú son núméricas.")
        menu()


print("---SISTEMA DE GESTIÓN DE FACTURACIÓN---\n\tSelección de archivos.")
file_usuarios=input("Ingrese el nombre de Archivo con DATOS de CLIENTES/USUARIOS: ")
file_usuarios+=".csv"

file_viajes=input("Ingrese el nombre de Archivo con DATOS de VIAJES REALIZADOS: ")
file_viajes+=".csv"

validacion_clientes(file_usuarios)
validacion_viajes(file_viajes)

print("\n---SISTEMA DE GESTIÓN DE FACTURACIÓN---\n\tMENÚ PRINCIPAL:")

#logging.basicConfig(filename="historial_acciones.log",filemode="a",format="%(asctime)s %(message)s",datefmt="%Y-%m-%d",level=logging.INFO)
#logging.info("Incio del programa.")
##no uso este formato porque quiero que sólo me de la fecha en el primer renglón "del día".

fecha=datetime.date.today()
with open("historial_acciones.log","a") as file:
    file.write(f"{fecha} - Inicio del programa\n")

menu()