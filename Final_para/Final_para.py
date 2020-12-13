#Agregar a las notas. 
#Del archivo clientes.csv, tuve que ingresar manualmente la linea 3: Asunción Ropero Landa,Camino de Ángel Morell 41 Puerta 9,16432378,2016-04-23,juan00@yanez.com,Nexos S.A
#y linea 91: Miguel Ángel Valbuena Aznar,Paseo Julio Jimenez 24,30931091,2012-07-22,adanfatima@alberto.com,Madre Agencia
#porque al ejecutar el archivo recibía el error:
#  File "C:\Users\Usuario\AppData\Local\Programs\Python\Python38-32\lib\encodings\cp1252.py", line 23, in decode
#    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 293: character maps to <undefined>
#Modificada la linea 59 dle archivo viajes.csv. El importe del viaje estaba en otro formado: "2,222.00"
import csv, logging

def continuar():
    cont=int(input("Ingrese 1 para volver al menú o 0 para salir: "))
    try:
        while cont != 0 and cont!=1:
            cont=int(input("Seleccione una opción válida: 1 para volver al menú, 0 para salir del programa: "))
        return cont
    except ValueError:
        print("Selecciona una opción válida del menú.")
        continuar()

def consulta_cliente_nom(nombre, archivo_us):
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

            if continuar()==0:
                print("----\nMuchas gracias!\n----\n")
                exit()
            else:
                menu()
    except IOError:
        print("----\nVerifique el nombre del archivo que está consultado.\n----\n")
        menu()

def consulta_cliente_doc(documento,archivo_us,archivo_via):
    cont=0
    tot=0.0
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
                print("----\n",cliente,"\n----\n")
                print("----\n",linea,"\n----\n")
            linea=next(file_csv, None)
        while renglon:
            documento=int(documento)
            monto=float(renglon[2])
            if documento==int(renglon[0]):
                cont+=1
                tot+=monto
            renglon=next(file_v_csv, None)
        print("----\n",cont, "{:.2f}".format(tot), "\n----\n")
        if continuar()==0:
            print("----\nMuchas gracias!\n----\n")
            exit()
        else:
            menu()


def consulta_empresa_us(empresa,archivo_us):
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
                print(f"----\nEmpresa: {consulta}\n----\n")
                print(f"----\nTotal de usuarios: {cont}\n----\n")
                for i in usuarios:
                    print(i)
            else:
                print("----\nEl nombre de empresa ingresado no existe en el archivo consultado.\n----\n")
            if continuar()==0:
                print("Muchas gracias!")
                exit()
            else:
                menu()
    except IOError:
        print("----\nVerifique el nombre del archivo que está consultado.\n----\n")
        menu()
    except IndexError:
        print("----\nHubo un error. Es probable que una fila esté completa con espacios vacíos. Complétela o elimínela.\n----\n")
        menu()


def consulta_empresa_tot(empresa, archivo_us, archivo_via):
    empresa=empresa.lower()
    usuarios=[]
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
                    linea=next(client_csv, None)
                while renglon:
                    importe=float(renglon[2])
                    for i in usuarios:
                        if i[2]==renglon[0]:
                            total+=importe
                    renglon=next(viajes_csv, None)
                print("----\n",consulta, "{:.2f}".format(total),"----\n") #Este formar redondea en 2 decimales.
                if continuar()==0:
                    print("----\nMuchas gracias!\n----\n")
                    exit()
                else:
                    menu()
    except IOError:
        print("----\nVerifique el nombre del archivo que está consultado.\n----\n")
        menu()

def validacion_clientes(archivo_us):
    try:
        with open(archivo_us, "r") as file:
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
                cont+=1
                linea=next(file_csv, None)

            if hay_error==True:
                print("Verifique el archivo", archivo_us, "y vuelva a inciar el programa.")

    except IOError:
        print("Verifique el nombre de archivo ingresado.")
        print("Verifique el archivo", archivo_us, "y vuelva a inciar el programa.")

def validacion_viajes(archivo_via):
    try:
        with open(archivo_via,"r") as file:
            file_csv=csv.reader(file, delimiter=",")
            linea=next(file_csv, None)
            linea=next(file_csv, None)
            
            cont=1
            while linea:
                if len(linea)!=3:
                    print(f"Linea {cont}: verifique los campos completados en esta linea. Debe contener exactamente 3 campos.")
                        
                if len(linea[0])<7 or len(linea[0])>8 :
                    print(f"Linea {cont}: verifique el número de documento, el mismo debe contener entre 7 y 8 números.")
                
                monto=linea[2].split(".")
                if len(monto[1])!=2:
                    print(f"Linea {cont}: verifique el monto del viaje. Debe contener 2 decimales.")
                if IndexError:
                    print(f"Linea {cont}: verifique el monto del viaje. Debe contener 2 decimales.")
                
    
                cont+=1
                linea=next(file_csv, None)

            if hay_error==True:
                print("Verifique el archivo", archivo_via, "y vuelva a inciar el programa.")

    except IOError:
        print("Verifique el nombre del archivo ingresado.")
        print("Verifique el archivo", archivo_via, "y vuelva a inciar el programa.")

def menu():
    try:
        print("\nSelecciona una opción del menú.")
        logging.basicConfig(filename="historial_acciones.log",filemode="a",format="%(message)s",level=logging.INFO)
        #filename: nombre del archivo / filemode: modo de apertura / format: formato de las lineas del archivo que vamos a escribir
        #level: tipo de mensajes que vamos a guardar.

        logging.info("Acceso a menú.")
        #Tipo de mensaje y mensaje.

        seleccion=int(input("\t1) Consulta de CLIENTE\n\t2) Consulta de EMPRESA\n\t3) Importe TOTAL por EMPRESA\n\t4) Consulta por DOCUMENTO\n\t5) Salir.\n\t"))
        while seleccion not in range(1,6):
            seleccion=int(input("Por favor, seleccioná una opción válida del menú:\n\t1) Consulta de CLIENTE\n\t2) Consulta de EMPRESA\n\t3) Importe TOTAL por EMPRESA\n\t4) Consulta por DOCUMENTO\n\t5) Salir.\n\t"))
        if seleccion==5: #Salida
            print("Hasta pronto!")
            exit()

        if seleccion==1: #Consulta de usuarios por nombre.
            logging.info("Consulta de usuarios por NOMBRE.")
            nombre=input("Ingrese el nombre del CLIENTE a buscar: ")
            consulta_cliente_nom(nombre,file_usuarios)

        if seleccion==2: #Consulta de total de usuarios x empresa.
            logging.info("Consulta del TOTAL DE USUARIOS por Empresa.")
            empresa=input("Ingrese el nombre de la EMPRESA a consultar: ")
            consulta_empresa_us(empresa, file_usuarios)

        if seleccion==3: #Consulta de total gastado por empresa
            logging.info("Consulta de TOTAL DE GASTOS por Empresa")
            company=input("Ingrese el nombre de la empresa a consultar: ")
            consulta_empresa_tot(company, file_usuarios,file_viajes)

        if seleccion==4:
            logging.info("Consulta de usuario por NÚMERO DE DOCUMENTO.")
            documento=input("Ingrese el número de documento a consultar: ")
            consulta_cliente_doc(documento,file_usuarios,file_viajes)

    except ValueError:
        print("Las opciones del menú son núméricas.")
        menu()



file_usuarios=input("Ingrese el nombre del archivo donde están guardados los datos completos de los usuarios: ")
file_usuarios+=".csv"

file_viajes=input("Ingrese el nombre del archivo donde están guardados los datos de los viajes realizados por cada usuario: ")
file_viajes+=".csv"

validacion_clientes(file_usuarios)
validacion_viajes(file_viajes)

print("---SISTEMA DE GESTIÓN DE FACTURACIÓN---")
with open("historial_acciones.log","a") as file:
    file.write("Historial de acciones del menú.\n")

menu()