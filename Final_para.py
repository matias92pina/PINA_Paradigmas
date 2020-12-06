#Agregar a las notas. 
#Del archivo clientes.csv, tuve que ingresar manualmente la linea 3: Asunción Ropero Landa,Camino de Ángel Morell 41 Puerta 9,16432378,2016-04-23,juan00@yanez.com,Nexos S.A
#y linea 91: Miguel Ángel Valbuena Aznar,Paseo Julio Jimenez 24,30931091,2012-07-22,adanfatima@alberto.com,Madre Agencia
#porque al ejecutar el archivo recibía el error:
#  File "C:\Users\Usuario\AppData\Local\Programs\Python\Python38-32\lib\encodings\cp1252.py", line 23, in decode
#    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 293: character maps to <undefined>
#Modificada la linea 59 dle archivo viajes.csv. El importe del viaje estaba en otro formado: "2,222.00"
import csv

def consulta_cliente_nom(nombre):
    nombre=nombre.lower()
    cont=0
    try:
        with open("clientes.csv","r",newline="") as file:
            file_csv=csv.reader(file,delimiter=",")
            linea=next(file_csv, None)
            while linea:
                cliente=linea[0].lower()
                if nombre in cliente:
                    print(f"Cliente: {linea[0]}, Documento: {linea[2]},Empresa: {linea[5]}, Dirección: {linea[1]}, Fecha de alta: {linea[3]}, Email: {linea[4]}")
                    cont+=1
                linea=next(file_csv, None)
            if cont==0:
                print("El nombre ingresado no se encuentra en el archivo consultado.")
    except IOError:
        print("Verifique el nombre del archivo que está consultado.")
        menu()

def consulta_cliente_doc(documento):
    cont=0
    tot=0.0
    
    with open("clientes.csv","r",newline="") as file, open("viajes.csv","r",newline="") as file_v:
        file_csv=csv.reader(file,delimiter=",")
        file_v_csv=csv.reader(file_v,delimiter=",")
        linea=next(file_csv, None)
        linea=next(file_csv, None)
        renglon=next(file_v_csv, None)
        renglon=next(file_v_csv, None)
        while linea:
            cliente=linea[2]
            if documento==cliente:
                print(cliente)
                print(linea)
            linea=next(file_csv, None)
        while renglon:
            documento=int(documento)
            monto=float(renglon[2])
            if documento==int(renglon[0]):
                cont+=1
                tot+=monto
            renglon=next(file_v_csv, None)
        print(cont, "{:.2f}".format(tot))

#def suma_doc(documento):
#    total=0.0
#    with open("viajes.csv","r",newline="") as file:
#        file_csv=csv.reader(file, delimiter=",")
#        linea=next(file_csv, None)
#        linea=next(file_csv, None)
#        while linea:
#            monto=float(linea[2])
#            if documento==int(linea[0]):
#                total+=monto
#            linea=next(file_csv, None)
#        print(total)




def consulta_empresa_us(empresa):
    empresa=empresa.lower()
    usuarios=[]
    cont=0
    try:
        with open("clientes.csv","r",newline="") as file:
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
                print(f"Empresa: {consulta}")
                print(f"Total de usuarios: {cont}")
                for i in usuarios:
                    print(i)
            else:
                print("El nombre de empresa ingresado no existe en el archivo consultado.")
    except IOError:
        print("Verifique el nombre del archivo que está consultado.")
        menu()
    except IndexError:
        print("Hubo un error. Es probable que una fila esté completa con espacios vacíos. Complétela o elimínela.")
        menu()


def consulta_empresa_tot(empresa):
    empresa=empresa.lower()
    usuarios=[]
    total=0.0
    try:
        with open("clientes.csv","r",newline="") as f_client, open("viajes.csv","r",newline="") as f_viajes:
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
                print(consulta, "{:.2f}".format(total)) #Este formar redondea en 2 decimales.
    except IOError:
        print("Verifique el nombre del archivo que está consultado.")
        menu()


def menu():
    print("---SISTEMA DE GESTIÓN DE FACTURACIÓN---")
    print("Selecciona una opción del menú.")
    try:
        seleccion=int(input("\t1) Consulta de CLIENTE\n\t2) Consulta de EMPRESA\n\t3) Importe TOTAL por EMPRESA\n\t4) Consulta por DOCUMENTO\n\t5) Salir.\n\t"))
        while seleccion not in range(1,6):
            seleccion=int(input("Por favor, seleccioná una opción válida del menú:\n\t1) Consulta de CLIENTE\n\t2) Consulta de EMPRESA\n\t3) Importe TOTAL por EMPRESA\n\t4) Consulta por DOCUMENTO\n\t5) Salir.\n\t"))
        if seleccion==5: #Salida
            print("Hasta pronto!")
            exit()

        if seleccion==1: #Consulta de usuarios por nombre.
            nombre=input("Ingrese el nombre del CLIENTE a buscar: ")
            consulta_cliente(nombre)

        if seleccion==2: #Consulta de total de usuarios x empresa.
            empresa=input("Ingrese el nombre de la EMPRESA a consultar: ")
            consulta_empresa_us(empresa)

        if seleccion==3: #Consulta de total gastado por empresa
            company=input("Ingrese el nombre de la empresa a consultar: ")
            consulta_empresa_tot(company)

        if seleccion==4:
            documento=input("Ingrese el número de documento a consultar: ")
            consulta_cliente_doc(documento)

    except ValueError:
        print("Las opciones del menú son núméricas.")
        menu()

menu()