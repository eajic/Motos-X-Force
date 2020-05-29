import os 
import time 
import re
import json
import pandas as pd
#Declaracion de variables que nos ayudaran en el transcurso del programa
ruta = './ArchivosFacturas/' #Direccion de nuestra carpeta de facturacion
separar = '\n' #Esta variable nos ayudara a realizar saltos de linea en nuestro programa
tipo_extencion = 'txt' #Esto nos servira para el uso en archivos de texto

#MENUS

def compra2(): #Este modulo nos direccionara a mostrar el modulo de clientes
    os.system("cls")     
    print("----------Modulo De Clientes----------")
    print("1--Ver Historial De Compras")
    print("2--Buscar Cliente")  
    print("3-Volver al Menu Principal")
    opcion=(int(input("Ingrese la Opcion:")))
    if opcion==1:
        clientes()
    else:
        if opcion==2:
            buscar2()
        else:
            if opcion==3:
                inicio()
            else:
                if opcion<1 or opcion>6:
                    print("Opcion Invalida")
                    print("Redirigiendo al Menu")
                    os.system("pause")
                    compra2()
    

def inicio(): #Este modulo es nuestro menu principal con el cual mostraremos todo nuestro menu
    os.system("cls")
    print("-----Venta De Motos X-Force-----")
    print("1---Compra De Motocicletas")
    print("2---Clientes Registrados")
    print("3---Inventario")
    print("4---Venta De Motocicletas")
    print("5---Salir")
    opcion1=int(input("Ingrese Su Opcion: ")) #con esta validacion redireccionaremos a cada modulo del menu
    if opcion1==1:
        menucomp()
    else:
        if opcion1==2:
            compra2()
        else:
            if opcion1==3:
                inventario()
            else:
                if opcion1==4:
                    catalogo()
                else:
                    if opcion1==5:
                        salir()
                    else:
                        if opcion1<1 or opcion1>5:
                            print("Opcion Incorrecta")
        
def inventario(): #Este modulo de inventario es el mas importante de nuestro programa ya que le da origen a todo
    os.system("cls")     
    print("----------Modulo De Inventario----------")
    print("1--Ingreso De Productos")
    print("2--Ver Productos")
    print("3--Agregar Unidades")
    print("4--Modificar Producto")
    print("5--Eliminar Producto")
    print("6--Buscar Productos")  
    print("7--Volver al Menu Principal")
    opcion=(int(input("Ingrese la Opcion:")))
    if opcion==1:
        ingreso()
    else:
        if opcion==2:
            ver()
        else:
            if opcion==3:
                agregar2()
            else:
                if opcion==4:
                    modificar()
                else:
                    if opcion==5:
                        eliminar()
                    else:
                        if opcion==6:
                            buscar()
                        else:
                            if opcion==7:
                                inicio()
                            else:
                                if opcion<1 or opcion>6:
                                    print("Opcion Invalida")
                                    print("Redirigiendo al Menu")
                                    os.system("pause")
                                    inventario()


def menucomp(): #Declarando el menu principal de este modulo
    os.system("cls")
    print("----------Modulo De compra---------------") #Mostramos el menu
    print("1--Ingreso De Proveedores")
    print("2--Ver el listado de Proveedores")
    print("3--Modificar algun prveedor")
    print("4--Eliminar Proveedor")
    print("5--Ir al menu de inventario para agregar productos")
    print("6--Retornar al menu principal")
    print("7--salir del programa")
    print("------------------------------------------")
    opcion=( int(input("Ingrese la Opcion:"))) #solicitamos el movimiento por medio de una variable numerica
    if opcion==1: # Y lo validamos con un if 
        ingresoprov() # Y redireccionamos a las funciones de cada opcion
    else:
        if opcion==2:
            verprov()
        else:
            if opcion==3:
                modprov()
            else:
                if opcion==4:
                    eliminarprov()
                else:
                    if opcion==5:
                        inventario()
                    else:
                        if opcion==6:
                            inicio()
                        else:
                            if opcion == 7:
                                salir()
                            else:    
                                if opcion<1 or opcion>6:
                                    print("Opcion Invalida")
                                    menucomp()


#MODULOS DEL INVENTARIO
def ingreso(): #En este modulo registraremos nuestras motocicletas 
    os.system("cls")
    data = []
    datos=open("inventario.txt","a") #Creacion del archivo de texto 
    datos.close()
    print("Ingreso De Nuevas Motocicletas")
    nombre=input("Ingrese Nombre De La Motocicleta:")
    datos=open("inventario.txt","r") #Escritura en el archivo de texto de inventario
    lineas=datos.read()
    if nombre in lineas: #Validacion del producto si ya existe unicamente se le agregaran unidades
        print("---------------------------------------------")
        print("Producto Ya existe Unicamente Agrege Unidades")
        print("---------------------------------------------")
        agregar(nombre) 
    else:
        color=(str(input("Ingrese Color:")))
        fab=(int(input("Ingrese Año :")))
        cantidad=(int(input("Ingrese Existencia:")))
        compra=(float(input("Ingrese Precio De Compra:")))
        venta=(float(input("Ingrese Precio De Venta:")))
        while compra>venta: #validacion de que la compra sea mayor que la venta
            print("Precio De Venta No Puede Ser Menor al De Compra")
            venta=(float(input("Ingrese Precio De Venta:")))
        motos=(nombre,color,fab,cantidad,compra,venta)
        data.append(motos)

        guardar=open("inventario.txt","a") #le asignamos un alias a la opcion guardar
        for motos in data:
            linea=nombre+","+color+","+str(fab)+","+str(cantidad)+","+str(compra)+","+str(venta)+","
            guardar.write(linea + '\n')
        guardar.close()

    os.system("cls")
    print("Agregado Correctamente") 
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        inventario()
    else:
        if op==2:
            salir()
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                inventario()

def ver(): # Este modulo nos enseñara todos los productos existentes en el modulo
    os.system("cls")
    datos=open("inventario.txt","r")
    lineas=datos.readlines()
    datos.close()
    print("*********************************")
    print("*    Motocicletas Existentes    *")
    print("*********************************")
    for linea in lineas:
        leer=linea.split(",")
        print("Motocicleta:" + leer[0])
        print("Color:" + leer[1])
        print("Modelo:" + leer[2])
        print("Existencia:" + leer[3])
        print("Precio Compra: Q." + leer[4])
        print("Precio Venta: Q." + leer[5])
        print('\n')

    print("-----Opciones-----")
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        inventario()
    else:
        if op==2:
            salir()
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                inventario()   

def agregar(nombre):
    cantidad=(int(input("Ingrese Cantidad a Agregar:")))
    data = []
    
    datos=open("inventario.txt","r")
    lineas=datos.readlines()
    datos.close()
    
    for linea in lineas:
        leer=linea.split(",")
        for a in leer:
            if a.lower() == nombre.lower():
                nuevo=leer[3]
                total=int(nuevo)+cantidad

                leer[3]=total
                data.append(leer)
                break
            else:
                data.append(leer)
                break
    
        datos1=open("inventario.txt","w")
        for linea in data:
            linea=(linea[0]+","+linea[1]+","+str(linea[2])+","+str(linea[3])+","+str(linea[4])+","+str(linea[5]))+","
            datos1.write(linea + '\n')
        datos1.close()
    

def agregar2():
    os.system("cls")
    datos=open("inventario.txt","r")
    lineas=datos.read()
    print("------Agregar Unidades-------")
    nombre=(str(input("Ingrese nombre De Motocicleta:")))
    if nombre in lineas:
        cantidad=(int(input("Ingrese Cantidad a Agregar:")))
        data = []
    
        datos=open("inventario.txt","r")
        lineas=datos.readlines()
        datos.close()
    
        for linea in lineas:
            leer=linea.split(",")
            for a in leer:
                if a.lower() == nombre.lower():
                    nuevo=leer[3]
                    total=int(nuevo)+cantidad

                    leer[3]=total
                    data.append(leer)
                    break
                else:
                    data.append(leer)
                    break
    
            datos1=open("inventario.txt","w")
            for linea in data:
                linea=(linea[0]+","+linea[1]+","+str(linea[2])+","+str(linea[3])+","+str(linea[4])+","+str(linea[5]))+","
                datos1.write(linea + '\n')
            datos1.close()
       
        print("Agregado Correctamente")
        print("1-)Volver Al Menu")
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inventario()
        else:
            if op==2:
                salir()
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu")
                    inventario()
    else:
        print("El Producto No esta Registrado")
        print("1-)Volver Al Menu")
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inventario()
        else:
            if op==2:
                salir()
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu")
                    inventario()

def modificar():
    os.system("cls")
    print("-----Modificar Datos-----")
    datos=open("inventario.txt","r")
    lineas=datos.read()
    nombre=(str(input("Ingrese nombre De Motocicleta:")))
    if nombre in lineas:
        data = []
        color=(str(input("Ingrese Color:")))
        fab=(int(input("Ingrese Año :")))
        cantidad=(int(input("Ingrese Existencia:")))
        compra=(float(input("Ingrese Precio De Compra:")))
        venta=(float(input("Ingrese Precio De Venta:")))
        while compra>venta:
            print("Precio De Venta No Puede Ser Menor al De Compra")
            venta=(int(input("Ingrese Precio De Venta:")))
        
        datos=open("inventario.txt","r")
        lineas=datos.readlines()
        datos.close()
    
        for linea in lineas:
            leer=linea.split(",")
            for a in leer:
                if a.lower() == nombre.lower():
                    leer[0]=nombre
                    leer[1]=color
                    leer[2]=fab
                    leer[3]=cantidad
                    leer[4]=compra
                    leer[5]=venta

                    data.append(leer)
                    break
                else:
                    data.append(leer)
                    break
    
            datos1=open("inventario.txt","w")
            for linea in data:
                linea=(linea[0]+","+linea[1]+","+str(linea[2])+","+str(linea[3])+","+str(linea[4])+","+str(linea[5]))+","
                datos1.write(linea + '\n')
            datos1.close()
        print("Agregado Correctamente")
        print("1-)Volver Al Menu")
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inventario()
        else:
            if op==2:
                salir()
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu")
                    inventario()
    else:
        print("El Producto No se Puede Modificar")
        print("No esta registrado")
        print("1-)Volver Al Menu")
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inventario()
        else:
            if op==2:
                salir()
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu")
                    inventario()

def eliminar():
    palabra=input("Ingrese Nombre de Motocicleta a Eliminar:") 
    datos = open("inventario.txt","r")
    lineas = datos.readlines() 
    datos = open("inventario.txt","w") 
    for linea in lineas: 
        if linea!=palabra + "," in linea: 
            print("Se ha eliminado del Inventario")
        else: 
            datos.write(linea) 
    datos.close()   
    datos.close() 

    print("-----Opciones-----")
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        inventario()
    else:
        if op==2:
            salir()
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                inventario()

def buscar():
    nombre=(str(input("Ingrese Nombre de Motocicleta:")))
    datos=open("inventario.txt","r")
    for linea in datos:
        leer=linea.split(',')
        if nombre in linea:
            print("=========================")
            print("Motocicleta:" + leer[0])
            print("Color:" + leer[1])
            print("Modelo:" + leer[2])
            print("Existencia:" + leer[3])
            print("Precio Compra: Q." + leer[4])
            print("Precio Venta: Q." + leer[5])
            print('\n')
    print("-----Opciones-----")
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        inventario()
    else:
        if op==2:
            salir()
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                inventario()

#MODULO COMPRA
def clientes(): #Este modulo nos ayudara a ver cuales son los clientes que tenemos registrados
    os.system("cls")
    datos=open("ventas.txt","r")
    lineas=datos.readlines()
    datos.close()
    print("*********************************")
    print("*        Ventas Realizadas      *")
    print("*********************************")
    for linea in lineas:
        leer=linea.split(",")
        print("Fecha De Compra:" + leer[0])
        print("Cliente:" + leer[1])
        print("NIT:" + leer[2])
        print("Motocicleta:" + leer[3])
        print("Modelo:" + leer[4])
        print("Total Gastado: Q." + leer[8])
        print("Cantidad Adquirida:" + leer[5])
        print('\n')

    print("-----Opciones-----")
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        inicio()
    else:
        if op==2:
            salir()
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                inicio()   

def buscar2():
    nombre=(str(input("Ingrese Nombre de La Persona:")))
    datos=open("ventas.txt","r")
    for linea in datos:
        leer=linea.split(',')
        if nombre in linea:
            print("=========================")
            print("Nombre:" + leer[1])
            print("NIT:" + leer[2])
            print('\n')
    print("-----Opciones-----")
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        compra2()
    else:
        if op==2:
            salir()
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                compra2()

#MODULO VENTA
def catalogo():
    os.system("cls")
    datos=open("inventario.txt","r")
    lineas=datos.readlines()
    datos.close()
    print("**********************************")
    print("*    Catalogo De Motocicletas    *")
    print("**********************************")
    for linea in lineas:
        leer=linea.split(",")
        print("Motocicleta:" + leer[0])
        print("Color:" + leer[1])
        print("Modelo:" + leer[2])
        print("Existencia:" + leer[3])
        print("Precio Compra: Q." + leer[5])
        print('\n')
    print("-----Eliga Su Motocicleta-----")
    nombre=(str(input("Ingrese Nombre Completo De La Motocicleta:")))
    compra(nombre)

def baja(nombre,unidad):
    os.system("cls")
    datos=open("inventario.txt","r")
    lineas=datos.read()
    if nombre in lineas:
        cantidad=unidad
        data = []
    
        datos=open("inventario.txt","r")
        lineas=datos.readlines()
        datos.close()
    
        for linea in lineas:
            leer=linea.split(",")
            for a in leer:
                if a.lower() == nombre.lower():
                    nuevo=leer[3]
                    total=int(nuevo)-cantidad

                    leer[3]=total
                    data.append(leer)
                    break
                else:
                    data.append(leer)
                    break
    
            datos1=open("inventario.txt","w")
            for linea in data:
                linea=(linea[0]+","+linea[1]+","+str(linea[2])+","+str(linea[3])+","+str(linea[4])+","+str(linea[5]))+","
                datos1.write(linea + '\n')
            datos1.close()
       
        print("Compra Exitosa")
        print("1-)Volver Al Menu")
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inicio()
        else:
            if op==2:
                salir()
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu")
                    inicio()
    else:
        print("El Producto No esta Registrado")
        print("1-)Volver Al Menu")
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inicio()
        else:
            if op==2:
                salir()
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu")
                    inicio()

def compra(nombre):
    data=[]
    datos=open("inventario.txt","r")
    for linea in datos:
        leer=linea.split(',')
        if nombre in linea:
            data.append(linea)

    print("-----Producto a Comprar-----")
    for a in data:
        leer=a.split(',')
        print("Motocicleta:" + leer[0])
        print("Color:" + leer[1])
        print("Modelo:" + leer[2])
        print("Precio De Compra:" + leer[5])
    nom=leer[0]
    color=leer[1]
    modelo=leer[2]
    com=leer[4]
    prec=leer[5]
    uni=leer[3]
    print("Confirme Su Compra")
    print("1---SI")
    print("2---NO")
    op=int(input("Ingrese Su Opcion:"))
    if op==1:
        facturacion(nom,color,modelo,com,prec,uni)
    else:
        if op==2:
            print("No se confirmo la compra")
            print("Redirigiendo al catalogo")
            os.system("pause")
            catalogo()

def ventas(fecha,nombre,nit,producto,unidades,color,modelo,com,prec,total):
    cliente=[]
    compr=float(com)
    preci=float(prec)
    ganancia=((preci-compr)*unidades)
    venta=(fecha,nombre,producto,modelo,unidades,compr,preci,ganancia)
    cliente.append(venta)

    guardar=open("ventas.txt","a+")
    for venta in cliente:
        linea=fecha+","+nombre+","+nit+","+producto+","+modelo+","+str(unidades)+","+str(compr)+","+str(preci)+","+str(total)+","+str(ganancia)+","
        guardar.write(linea + '\n')
    guardar.close()


#MODULO FACTURACION
def encabezado():    
    print(" --- VENTA DE MOTOS X-FORCE ---")
    print("     OPERADORA DE TIENDAS S.A.")
    print("VENTA DE MOTOS CHIMALTENANGO")
    print("       7A. CALLE 2-02 ZONA 2")
    print("         TEL: 1234 - 5678\n")


def facturacion(nom,color,modelo,com,prec,uni):
    # Usamos cls para borrar la terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    encabezado()
    fecha=time.strftime("%x")
    print("Fecha:",fecha)
    nombre = inputRequired('Nombre del Cliente: ')
    # Construimos el nombre del archivo
    file_path = os.path.join(ruta, stringToFileName(nombre))
    b=int(inputRequired("¿Desea agregar NIT? si = 1 /no = 0: "))
    if b == 1:
        nit = inputRequired('Ingrese el NIT: ')
    if b == 0:
        nit = ('Consumidor Final')
    producto=nom
    print("Motocicleta:", producto)
    precio=prec
    print("Precio De Compra: Q.", precio)
    unidades = int(input('Unidades del producto a comprar: '))
    unid=int(uni)
    if unidades>unid:
        print("YA no tenemos Unidades Disponibles:")
        print("Redirigiendo al MEnu Principal")
        os.system("pause")
        inicio()
    else:
        precio2=float(prec)
        total=unidades*precio2
        print("Total A Pagar:",total)
        efectivo = float(input('Efectivo: '))
        unidades_general= unidades
        precio_general = precio2
        total_general= precio_general * unidades_general
        if efectivo < total_general:
            print('El valor de pago no puede ser menor al de costo')
            return efectivo
        iva = total_general * 0.12
        cambio = efectivo - total_general
        print('Cambio: ' + str(cambio))
        print('Impuesto: ' + str(iva) + '\n')
        print('\nGRACIAS POR PREFERIRNOS, VUELVA PRONTO')
        # Creamos el producto con nuestro CRUD
        crearFac(fecha,nombre, nit, producto, precio, unidades,total_general,efectivo,cambio, iva)
        print("\n-> LA FACTURA SE GENERO EXITOSAMENTE\n")

        # Regresamos al menu de opciones
        input("Para continuar, presione la tecla Enter...")
        ventas(fecha,nombre,nit,producto,unidades,color,modelo,com,prec,total)
        baja(producto,unidades)

def inputPositiveNumber(mensaje):
  while True:
    x = float (inputNumber(mensaje))
    if x < 0:
        print('\nERROR: El número Ingresado Tiene que ser Positivo, Vuelve a Intentarlo\n')
    else:
        break
  return x

# Funcion que solo permite ingresar numeros enteros
def inputNumber(mensaje):
  while True:
    try:
      x = float(input(mensaje))
    except ValueError:
      print("\nERROR: Tienes que Ingresar un Numero Entero, Vuelve a Intentarlo\n")
      continue
    else:
      return x

def inputRequired(mensaje):
  while True:
    x = (input(mensaje))
    if len(x) < 1:
        print('\nERROR: Tienes que Ingresar Almenos un carácter, Vuelve a Intentarlo\n')
    else:
        break
  return x

def stringToFileName(input_string, ext = tipo_extencion):
  return re.sub('[^A-Za-z0-9]+', '', input_string) + '.' + ext

def crearFac(fecha, nombre, nit, producto, precio, unidades,total_general, efectivo, cambio,iva):

  file_path=os.path.join(ruta, stringToFileName(nombre))
  file = open(file_path, "w")
  file.write(' --- VENTA DE MOTOS ---' + separar + '--- OPERADORA DE TIENDAS S.A. ---' + separar + 'VENTA DE MOTOS CHIMALTENANGO' + separar + '----- 7A. CALLE 2-02 ZONA 2 -----' + separar + '------ Tel: 1234 - 5678 ------' +separar + separar +'Fecha: '+ fecha + separar + 'Nombre: ' + nombre + separar + 'NIT: ' + str(nit) + separar + 'Producto: ' + str(producto) + separar + 'Precio: Q' + str(precio) + separar + 'Unidades: ' + str(unidades ) + separar + 'Total: ' + str(total_general) + separar + 'Efectivo: Q' + str(efectivo) + separar + 'Cambio: Q' + str(cambio) + separar + 'Impuesto: Q' + str(iva) + separar + separar + 'GRACIAS POR PREFERIRNOS, VUELVA PRONTO')
  file.close()

#MODULO PROVEEDORES
def ingresoprov(): #Inicia la creacion del ingreso de proveedores
    os.system("cls") #Esta opcion nos ayudara a limpiar pantalla
    dat = [] #declaracion de nuestra lista en ella alojaremos los datos para poder modificarlos y leerlos
    prov=open("proveedores.txt","a") #creamos y abrimos el archivo de texto
    prov.close()
    print("Ingreso De Proveedores.....!!!")
    nombre=input("Ingrese el Nombre del Proveedor:")
    prov=open("proveedores.txt","r")
    lineas=prov.read()
    if nombre in lineas: #aca validamos que el nombre de nuestro proveedor no se encuentre ya registrado
        print("---------------------------------------------")
        print("El proveedor ya se encuentra registrado Desea modificarlo")
        print("---------------------------------------------")
        modprov()
    else:
        nit=(str(input("Ingrese Numero de nit del proveedor:")))
        direccion=(str(input("Ingrese la Direccion :")))
        email=(str(input("Ingrese el correo del proveedor:")))
        numero=(int(input("Ingrese el Numero del proveedor:")))
        while nombre == " ":
            print("Por favor ingrese un nombre")
            nombre=input("Ingrese un Nombre:")
        listado=(nombre,nit,direccion,email,numero)
        dat.append(listado)

        guardar=open("proveedores.txt","a")
        for listado in dat:
            linea=nombre+","+str(nit)+","+str(direccion)+","+str(email)+","+str(numero)
            guardar.write(linea + '\n')
        guardar.close()

    os.system("cls")
    print("Proveedor Agregado Correctamente") 
    print("1-)Volver Al Menu de compra de motocicletas")
    print("2-)Volver al menu de Inicio")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        menucomp()
    else:
        if op==2:
            inicio()
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu compra de motocicletas")
                menucomp()

def verprov(): #creacion del modulo para ver proveedores
    os.system("cls")
    prov=open("proveedores.txt","r") #se abre el archivo de texto para leer
    lineas=prov.readlines()
    prov.close() #se Cierra el archivo de texto
    print("_________________________________")
    print("_____Catalogo de Proveedores_____")
    print("_____Estos son los existentes____")
    for linea in lineas:
        leer=linea.split(",")
        print("Nombre:" + leer[0])
        print("No. de Nit:" + leer[1])
        print("Direccion:" + leer[2])
        print("Correro:" + leer[3])
        print("Numero telefonico: " + leer[4])

    print("-----Opciones-----")
    print("1-)Volver Al Menu compra de motocicletas")
    print("2-)Volver al menu principal")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        menucomp()
    else:
        if op==2:
            inicio() #aca vamos a adjuntar el modulo principal para que nuestro programa sea mas eficiente
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu proveedores")
                menucomp()        

def modprov(): #creamos el medulo pra eliminar proveedores
    os.system("cls")
    print("-----Modificar Datos del Proveedor-----")
    prov=open("proveedores.txt","r") #para modificarlo vamos a escribir sobre lo que ya esta escrito para eso lo buscaremos por el nombre
    lineas=prov.read()
    nombre=input("Ingrese nombre Del Proveedor:")
    if nombre in lineas:
        dat = []
        nit=(str(input("Ingrese Numero de Nit del proveedor:")))
        direccion=(str(input("Ingrese la Direccion :")))
        email=(str(input("Ingrese el correo del proveedor:")))
        numero=(int(input("Ingrese el Numero del proveedor:")))
        
        prov=open("proveedores.txt","r")
        lineas=prov.readlines()
        prov.close()
    
        for linea in lineas:
            leer=linea.split(",")
            for a in leer:
                if a.lower() == nombre.lower():
                    leer[0]=nombre
                    leer[1]=nit
                    leer[2]=direccion
                    leer[3]=email
                    leer[4]=numero

                    dat.append(leer)
                    break
                else:
                    dat.append(leer)
                    break
    
            dato=open("proveedores.txt","w")
            for linea in dat:
                dato.write(linea[0]+","+str(linea[1])+","+str(linea[2])+","+str(linea[3])+","+str(linea[4]))
                dato.write("\n")
            dato.close()
        print("Agregado Correctamente")
        print("1-)Volver Al Menu compra de motocicletas")
        print("2-)Volver al menu principal")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            menucomp()
        else:
            if op==2:
                inicio()
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu Compra de motocicletas")
                    menucomp()
    else:
        print("El Producto No se Puede Modificar")
        print("No esta registrado")
        print("1-)Volver Al Menu compra de motocicletas e ingresar la informacion del proveedor")
        print("2-)Volver Al Menu Principal")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            menucomp()
        else:
            if op==2:
                inicio()
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu compra de motocicletas")
                    menucomp()

def eliminarprov(): #creamos la funcion para poder eliminar proveedores
    os.system("cls")
    nomprov=input("Ingrese Nombre del proveedor que desea Eliminar:") 
    prov = open("proveedores.txt","r")
    lineas = prov.readlines() 
    prov = open("proveedores.txt","w") 
    for linea in lineas: 
        if linea!=nomprov + "," in linea: #leemos linea por linea para encontrar las coincidencias y lo eliminamos 
            print("Se ha eliminado del Inventario")
        else: 
            prov.write(linea) 
    prov.close()   
    prov.close() 

    print("-----Opciones-----")
    print("1-)Volver Al Menu compra de motocicletas")
    print("2-)Ir al menu principal")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        menucomp()
    else:
        if op==2:
            inicio()
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu compra de motocicletas")
                menucomp()

def salir():
    print("Ha decidido salir Salu2")
    exit()
    
inicio() #Declaramos la funcion inicio en donde se aloja nuestro menu principal