"""PROYECTO FINAL
    Sistema que lleva el control de inventario, ventas, de una venta de Motos"""

#Importamos las librerias
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
    os.system("cls")    #Limpiar Pantall
    print("----------Modulo De Clientes----------")
    print("1--Ver Historial De Compras")
    print("2--Buscar Cliente")  
    print("3-Volver al Menu Principal")
    opcion=(int(input("Ingrese la Opcion:"))) #Seleccionamos la opcion
    if opcion==1:
        clientes() #Redirecciona a las funciones
    else:
        if opcion==2:
            buscar2() #Redirecciona a las funciones
        else:
            if opcion==3:
                inicio() #Redirecciona a las funciones
            else:
                if opcion<1 or opcion>6:
                    print("Opcion Invalida")
                    print("Redirigiendo al Menu")
                    os.system("pause")
                    compra2() #Redirecciona a las funciones
    

def inicio(): #Este modulo es nuestro menu principal con el cual mostraremos las diferentes opciones
    os.system("cls")
    print("-----Venta De Motos X-Force-----")
    print("1---Compra De Motocicletas")
    print("2---Clientes Registrados")
    print("3---Inventario")
    print("4---Venta De Motocicletas")
    print("5---Salir")
    opcion1=int(input("Ingrese Su Opcion: ")) #Con esta validacion redireccionaremos a cada modulo del menu
    if opcion1==1:
        menucomp() #Redirecciona a las funciones
    else:
        if opcion1==2:
            compra2() #Redirecciona a las funciones
        else:
            if opcion1==3:
                inventario() #Redirecciona a las funciones
            else:
                if opcion1==4:
                    catalogo() #Redirecciona a las funciones
                else:
                    if opcion1==5:
                        salir() #Redirecciona a las funciones
                    else:
                        if opcion1<1 or opcion1>5:
                            print("Opcion Incorrecta")
                            print("Redirigiendo al Menu")
                            os.system("pause")
                            inicio()

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
        ingreso() #Redirecciona a las funciones
    else:
        if opcion==2:
            ver() #Redirecciona a las funciones
        else:
            if opcion==3:
                agregar2() #Redirecciona a las funciones
            else:
                if opcion==4:
                    modificar() #Redirecciona a las funciones
                else:
                    if opcion==5:
                        eliminar() #Redirecciona a las funciones
                    else:
                        if opcion==6:
                            buscar() #Redirecciona a las funciones
                        else:
                            if opcion==7:
                                inicio() #Redirecciona a las funciones
                            else:
                                if opcion<1 or opcion>6:
                                    print("Opcion Invalida")
                                    print("Redirigiendo al Menu")
                                    os.system("pause")
                                    inventario() #Redirecciona a las funciones


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
    data = [] #Nos almacenara los datos para luego guardarlos en el archivo txt
    datos=open("inventario.txt","a") #Creacion del archivo de texto 
    datos.close()
    print("Ingreso De Nuevas Motocicletas")
    nombre=input("Ingrese Nombre De La Motocicleta:")
    datos=open("inventario.txt","r") #Lectura en el archivo de texto de inventario
    lineas=datos.read()
    if nombre in lineas: #Validacion del producto si ya existe unicamente se le agregaran unidades
        print("---------------------------------------------")
        print("Producto Ya existe Unicamente Agrege Unidades")
        print("---------------------------------------------")
        agregar(nombre) #Trasladamos el nombre del producto a la funcion donde se agregaran las unidades
    else: #Si no existe seguimos solicitando datos
        color=(str(input("Ingrese Color:")))
        fab=(int(input("Ingrese Año :")))
        cantidad=(int(input("Ingrese Existencia:")))
        compra=(float(input("Ingrese Precio De Compra:")))
        venta=(float(input("Ingrese Precio De Venta:")))
        while compra>venta: #validacion de que el precio de compra no sea mayor al de venta
            print("Precio De Venta No Puede Ser Menor al De Compra")
            venta=(float(input("Ingrese Precio De Venta:")))
        motos=(nombre,color,fab,cantidad,compra,venta) #ALmacenamos los datos en una variable
        data.append(motos) #Grabamos los datos en una lista

        guardar=open("inventario.txt","a") #Se abre la funcion para guardar los datos en el archivo txt
        for motos in data:
            linea=nombre+","+color+","+str(fab)+","+str(cantidad)+","+str(compra)+","+str(venta)+"," #Definimos como se guardaran los datos en el archivo txt
            guardar.write(linea + '\n')   #Guardamos los datos en el archivo txt
        guardar.close() #Cerramos la opcion de escritura en el archivo txt

    os.system("cls")
    print("Agregado Correctamente") #Mensaje que se mostrara al guardar satisfactoriamente el producto
    print("-----Opciones-----") #Opciones para regresar al menu
    print("1-)Volver Al Menu") #Opciones para regresar al menu
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        inventario() #Redirecciona a las funciones
    else:
        if op==2:
            salir() #Redirecciona a las funciones
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                inventario() #Redirecciona a las funciones

def ver(): # Este modulo nos enseñara todos los productos existentes en el modulo
    os.system("cls")
    datos=open("inventario.txt","r") #Lectura del archivo donde se guardaron los productos
    lineas=datos.readlines() #Recorremos el archivo
    datos.close()
    print("*********************************")
    print("*    Motocicletas Existentes    *")
    print("*********************************")
    for linea in lineas:
        leer=linea.split(",") #Separamos cada palabra para que se muestre por poscicion
        print("Motocicleta:" + leer[0]) #Mostramos las posiciones del archivo txt
        print("Color:" + leer[1]) #Mostramos las posiciones del archivo txt
        print("Modelo:" + leer[2]) #Mostramos las posiciones del archivo txt
        print("Existencia:" + leer[3]) #Mostramos las posiciones del archivo txt
        print("Precio Compra: Q." + leer[4]) #Mostramos las posiciones del archivo txt
        print("Precio Venta: Q." + leer[5]) #Mostramos las posiciones del archivo txt
        print('\n') #Damos un salto de linea

    print("-----Opciones-----") #Opciones para regresar al menu
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        inventario() #Redirecciona a las funciones
    else:
        if op==2:
            salir() #Redirecciona a las funciones
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                os.system("pause")
                inventario() #Redirecciona a las funciones   

def agregar(nombre): #Funcion donde se agregaran las unidades a productos existentes si se intenta registar un producto ya existente
    cantidad=(int(input("Ingrese Cantidad a Agregar:"))) #Solicitamos Cantidad
    data = []  #Nos almacenara los datos para luego guardarlos en el archivo txt
    datos=open("inventario.txt","r") #Lectura del archivo donde se guardaron los productos
    lineas=datos.readlines() #Recorremos el archivo
    datos.close() 
    for linea in lineas: #Con el ciclo recorremos el archivo para encontrar el producto
        leer=linea.split(",") #Separamos cada palabra para que se muestre por poscicion
        for a in leer:
            if a.lower() == nombre.lower(): #Nos permite manipular letras mayusculas y minusculas
                nuevo=leer[3] #Invocamos la posicion donde esta las unidades
                total=int(nuevo)+cantidad #Se suma la invocacion anterior con las nuevas cantidades ingresadas

                leer[3]=total #Le asignamos el valor de la suma a la posicion de las unidades en el archivo de texto
                data.append(leer) #Grabamos las unidades en el archivo de texto
                break
            else:
                data.append(leer) #Grabamos las unidades en el archivo de texto
                break
    
        datos1=open("inventario.txt","w") #Abrimos el archivo de texto para sobreescribirlo pero ya con las modificaciones
        for linea in data:
            linea=(linea[0]+","+linea[1]+","+str(linea[2])+","+str(linea[3])+","+str(linea[4])+","+str(linea[5]))+"," #Definimos como se guardaran los datos en el archivo txt
            datos1.write(linea + '\n') #Grabamos los datos en el archivo de texto
        datos1.close()
    

def agregar2(): #Funcion donde se agregaran las unidades a productos existentes pero en si ya en una opcion
    os.system("cls")
    datos=open("inventario.txt","r") #Lectura del archivo donde se guardaron los productos
    lineas=datos.read() #Recorremos el archivo
    print("------Agregar Unidades-------")
    nombre=(str(input("Ingrese nombre De Motocicleta:"))) #Solicitamos nombre del producto
    if nombre in lineas: #Verificamos si el producto ya esta registrado
        cantidad=(int(input("Ingrese Cantidad a Agregar:"))) #Solicitamos Cantidad
        data = [] #Nos almacenara los datos para luego guardarlos en el archivo txt
        datos=open("inventario.txt","r") #Lectura del archivo donde se guardaron los productos
        lineas=datos.readlines() #Recorremos el archivo
        datos.close()
    
        for linea in lineas:
            leer=linea.split(",") #Separamos cada palabra para que se muestre por poscicion
            for a in leer:
                if a.lower() == nombre.lower(): #Nos permite manipular letras mayusculas y minusculas
                    nuevo=leer[3] #Invocamos la posicion donde esta las unidades
                    total=int(nuevo)+cantidad #Se suma la invocacion anterior con las nuevas cantidades ingresadas

                    leer[3]=total #Le asignamos el valor de la suma a la posicion de las unidades en el archivo de texto
                    data.append(leer)  #Grabamos las unidades en el archivo de texto
                    break
                else:
                    data.append(leer) #Grabamos las unidades en el archivo de texto
                    break
    
            datos1=open("inventario.txt","w") #Abrimos el archivo de texto para sobreescribirlo pero ya con las modificaciones
            for linea in data:
                linea=(linea[0]+","+linea[1]+","+str(linea[2])+","+str(linea[3])+","+str(linea[4])+","+str(linea[5]))+"," #Definimos como se guardaran los datos en el archivo txt
                datos1.write(linea + '\n') #Grabamos los datos en el archivo de texto
            datos1.close()
       
        print("Agregado Correctamente") #Mensaje que se mostrara al guardar satisfactoriamente el producto
        print("-----Opciones-----") #Opciones para regresar al menu
        print("1-)Volver Al Menu")
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inventario() #Redirecciona a las funciones
        else:
            if op==2:
                salir() #Redirecciona a las funciones
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu")
                    inventario() #Redirecciona a las funciones
    else:
        print("El Producto No esta Registrado") #Mensaje que se mostrara si el producto no existe
        print("1-)Volver Al Menu") #Opciones para regresar al menu
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inventario() #Redirecciona a las funciones
        else:
            if op==2:
                salir() #Redirecciona a las funciones
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta") 
                    print("Redirigiendo Al Menu")
                    inventario() #Redirecciona a las funciones

def modificar(): #Modulo para modificar datos  
    os.system("cls") #LImpiamos pantalla
    print("-----Modificar Datos-----")
    datos=open("inventario.txt","r") #Lectura del archivo de texto
    lineas=datos.read() #Recorremos el archivo
    nombre=(str(input("Ingrese nombre De Motocicleta:"))) #Solicitamos el nombre del producto
    if nombre in lineas: #Verificamos que este registrado
        data = [] #Nos almacenara los datos para luego guardarlos en el archivo txt
        color=(str(input("Ingrese Color:"))) #Solicitamos los datos
        fab=(int(input("Ingrese Año :"))) #Solicitamos los datos
        cantidad=(int(input("Ingrese Existencia:"))) #Solicitamos los datos
        compra=(float(input("Ingrese Precio De Compra:"))) #Solicitamos los datos
        venta=(float(input("Ingrese Precio De Venta:"))) #Solicitamos los datos
        while compra>venta: #Validacion que el precio de compra no sea menor al de venta
            print("Precio De Venta No Puede Ser Menor al De Compra") 
            venta=(int(input("Ingrese Precio De Venta:"))) #Solicitamos los datos
        
        datos=open("inventario.txt","r") #Lectura del archivo de texto
        lineas=datos.readlines() #Recorremos el archivo
        datos.close()
    
        for linea in lineas:
            leer=linea.split(",")  #Separamos cada palabra para que se invoque por poscicion
            for a in leer: 
                if a.lower() == nombre.lower(): #Nos permite manipular letras mayusculas y minusculas
                    leer[0]=nombre #Asignamos los datos a las posiciones
                    leer[1]=color #Asignamos los datos a las posiciones
                    leer[2]=fab #Asignamos los datos a las posiciones
                    leer[3]=cantidad #Asignamos los datos a las posiciones
                    leer[4]=compra #Asignamos los datos a las posiciones
                    leer[5]=venta #Asignamos los datos a las posiciones

                    data.append(leer) #Guardamos los datos en la lista
                    break
                else:
                    data.append(leer) #Guardamos los datos en la lista
                    break
    
            datos1=open("inventario.txt","w") #Abrimos el archivo de texto para sobre escribir los datos ya modificados
            for linea in data:
                linea=(linea[0]+","+linea[1]+","+str(linea[2])+","+str(linea[3])+","+str(linea[4])+","+str(linea[5]))+"," #Definimos como se guardaran los datos en el archivo txt
                datos1.write(linea + '\n') #Grabamos los datos en el archivo de txto
            datos1.close()
        print("Moficiacion Correcta") #Mensaje que se mostrara al guardar satisfactoriamente los cambios
        print("1-)Volver Al Menu") #Opciones al salir
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inventario() #Redirecciona a las funciones
        else:
            if op==2:
                salir() #Redirecciona a las funciones
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu")
                    os.system("pause")
                    inventario() #Redirecciona a las funciones
    else:
        print("El Producto No se Puede Modificar")  #Mensaje que se mostrara si el producto no existe
        print("No esta registrado")
        print("1-)Volver Al Menu") #Opciones al salir
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inventario() #Redirecciona a las funciones
        else:
            if op==2:
                salir() #Redirecciona a las funciones
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu")
                    os.system("pause")
                    inventario() #Redirecciona a las funciones

def eliminar(): #Funcion para eliminar productos
    palabra=input("Ingrese Nombre de Motocicleta a Eliminar:") #Solicitamos el nombre del producto
    datos = open("inventario.txt","r") #Lectura del archivo de texto
    lineas = datos.readlines()  #Recorremos el archivo
    datos = open("inventario.txt","w")  #Abrimos el archivo para sobre escribir los productos 
    for linea in lineas: 
        if linea!=palabra + "," in linea: 
            print("Se ha eliminado del Inventario") #Mensaje al momento de eliminar
        else: 
            datos.write(linea) #Guardamos los datos en el archivo de texto
    datos.close()   
    datos.close() 

    print("-----Opciones-----") #Opciones al momento de salir
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        inventario() #Redirecciona a las funciones
    else:
        if op==2:
            salir() #Redirecciona a las funciones
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                os.system("pause")
                inventario() #Redirecciona a las funciones

def buscar(): #Funcion para buscar los productos
    nombre=(str(input("Ingrese Nombre de Motocicleta:"))) #Solicitamos el nombre dle producto
    datos=open("inventario.txt","r") #Lectura del archivo de texto donde estan almacenados
    for linea in datos:
        leer=linea.split(',') #Separamos por posicion los datos
        if nombre in linea:
            print("=========================") #Mostramos las coincidencias con la palabra ingresada
            print("Motocicleta:" + leer[0])
            print("Color:" + leer[1])
            print("Modelo:" + leer[2])
            print("Existencia:" + leer[3])
            print("Precio Compra: Q." + leer[4])
            print("Precio Venta: Q." + leer[5])
            print('\n')
    print("-----Opciones-----") #Opciones al momento de salir
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        inventario() #Redirecciona a las funciones
    else:
        if op==2:
            salir() #Redirecciona a las funciones
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                os.system("pause")
                inventario() #Redirecciona a las funciones

#MODULO COMPRA
def clientes(): #Este modulo nos ayudara a ver cuales son los clientes que tenemos registrados
    os.system("cls")
    datos=open("ventas.txt","r") #Lectura del archivo
    lineas=datos.readlines() #Recorremos el archivo de texto
    datos.close()
    print("*********************************") #Mostramos los datos almacenados en el archivo de ventas
    print("*        Ventas Realizadas      *")
    print("*********************************")
    for linea in lineas:
        leer=linea.split(",") #Separamos los datos por posicion
        print("Fecha De Compra:" + leer[0]) #MOstramos los datos
        print("Cliente:" + leer[1]) #MOstramos los datos
        print("NIT:" + leer[2]) #MOstramos los datos
        print("Motocicleta:" + leer[3]) #MOstramos los datos
        print("Modelo:" + leer[4]) #MOstramos los datos
        print("Total Gastado: Q." + leer[8]) #MOstramos los datos
        print("Cantidad Adquirida:" + leer[5]) #MOstramos los datos
        print('\n')

    print("-----Opciones-----") #Menu al salir
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        inicio() #Redirecciona a las funciones
    else:
        if op==2:
            salir() #Redirecciona a las funciones
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                os.system("pause")
                inicio()   #Redirecciona a las funciones

def buscar2(): #Funcion para buscar clientes 
    nombre=(str(input("Ingrese Nombre de La Persona:"))) #Solicitamos los datos
    datos=open("ventas.txt","r") #Lectura del archivo de Texto
    for linea in datos:
        leer=linea.split(',') #Separamos los datos por posicion
        if nombre in linea:
            print("=========================") #Mostramos los datos de los clientes registrados
            print("Nombre:" + leer[1])
            print("NIT:" + leer[2])
            print('\n')
    print("-----Opciones-----") #Menu al salir
    print("1-)Volver Al Menu")
    print("2-)Salir Del Programa")
    op=(int(input("Ingrese Su Opcion:")))
    if op==1:
        compra2() #Redirecciona a las funciones
    else:
        if op==2:
            salir() #Redirecciona a las funciones
        else:
            if op<1 or op>2:
                print("Opcion Incorrecta")
                print("Redirigiendo Al Menu")
                os.system("pause")
                compra2() #Redirecciona a las funciones

#MODULO VENTA
def catalogo(): #MOstraremos el catalogo de productos
    os.system("cls") #Limpiar pantall
    datos=open("inventario.txt","r") #Lectura del archivo donde estan registrados los productos
    lineas=datos.readlines() #Recorremos el archivo
    datos.close()
    print("**********************************") #Mostramos las motocicletas registradas
    print("*    Catalogo De Motocicletas    *")
    print("**********************************")
    for linea in lineas:
        leer=linea.split(",") #Invocamos los datos por posicion
        print("Motocicleta:" + leer[0]) #Mostramos los datos
        print("Color:" + leer[1]) #Mostramos los datos
        print("Modelo:" + leer[2]) #Mostramos los datos
        print("Existencia:" + leer[3]) #Mostramos los datos
        print("Precio Compra: Q." + leer[5]) #Mostramos los datos
        print('\n')
    print("-----Eliga Su Motocicleta-----") #Opcion para realizar la compra
    nombre=(str(input("Ingrese Nombre Completo De La Motocicleta:"))) #Solicitamos el ingreso del nombre del producto a comprar
    compra(nombre) #Enviamos el nombre a la funcion compra para proceder con la compra

def baja(nombre,unidad): #Funcion que nos ayudara al momento de realizar la venta bajar la cantidad en inventario, recibimos los valores de las variables que son el nombre y la cantidad comprada
    os.system("cls") #Limpiar pantalla
    datos=open("inventario.txt","r") #Lectura del archivo de texto
    lineas=datos.read() #Recorremos el archivp
    if nombre in lineas: #Validacion para verificar que el producto este en el archivo
        cantidad=unidad #La cantidad recibida la igualamos con la variable propia
        data = [] #Lista pora guardar los datos
    
        datos=open("inventario.txt","r") #Lectura del archivo de texto
        lineas=datos.readlines() #Recorremos el archivo
        datos.close()
    
        for linea in lineas:
            leer=linea.split(",") #Separamos los datos por posicion
            for a in leer:
                if a.lower() == nombre.lower():
                    nuevo=leer[3] #La posicon de las unidades la invocamos a una variable propia
                    total=int(nuevo)-cantidad #Ralizamos la resta de las unidades vendidas

                    leer[3]=total #Guardamos los datos en la posicion
                    data.append(leer) #Guardamos los datos en la lista
                    break
                else:
                    data.append(leer) #Guardamos los datos en la lista
                    break
    
            datos1=open("inventario.txt","w") #Abrimos el archivo de texto para sobre escribir las modificaciones
            for linea in data:
                linea=(linea[0]+","+linea[1]+","+str(linea[2])+","+str(linea[3])+","+str(linea[4])+","+str(linea[5]))+"," #Definimos como se grabaran los datos en el txt
                datos1.write(linea + '\n') #Grabamos los datos en el archivo de texto
            datos1.close() #Cerramos la lectura
       
        print("Compra Exitosa") #Mensaje al momento de realizar la compra
        print("1-)Volver Al Menu") #Opciones del menu al salir
        print("2-)Salir Del Programa")
        op=(int(input("Ingrese Su Opcion:")))
        if op==1:
            inicio() #Redirecciona a las funciones
        else:
            if op==2:
                salir() #Redirecciona a las funciones
            else:
                if op<1 or op>2:
                    print("Opcion Incorrecta")
                    print("Redirigiendo Al Menu")
                    os.system("pause")
                    inicio() #Redirecciona a las funciones

def compra(nombre): #Funcion para realizar la compra del producto recibimos el nombre del producto de otra funcion para realizar la compra
    data=[] #Lista para almacenar los datos
    datos=open("inventario.txt","r") #Lectura del archivo de texto
    for linea in datos:
        leer=linea.split(',') #Ubicamos los datos por posicion
        if nombre in linea:
            data.append(linea) 

    print("-----Producto a Comprar-----") #Mostramos el producto a comprar
    for a in data:
        leer=a.split(',') #Separamos los datos por posicion
        print("Motocicleta:" + leer[0]) #Mostramos los datos de compra
        print("Color:" + leer[1]) #Mostramos los datos de compra
        print("Modelo:" + leer[2]) #Mostramos los datos de compra
        print("Precio De Compra:" + leer[5]) #Mostramos los datos de compra
    nom=leer[0] #Recuperamos las posiciones para pasar los datos a la facturacion
    color=leer[1] #Recuperamos las posiciones para pasar los datos a la facturacion
    modelo=leer[2] #Recuperamos las posiciones para pasar los datos a la facturacion
    com=leer[4] #Recuperamos las posiciones para pasar los datos a la facturacion
    prec=leer[5] #Recuperamos las posiciones para pasar los datos a la facturacion
    uni=leer[3] #Recuperamos las posiciones para pasar los datos a la facturacion
    print("Confirme Su Compra") #Mensaje de confirmacion
    print("1---SI")
    print("2---NO")
    op=int(input("Ingrese Su Opcion:"))
    if op==1:
        facturacion(nom,color,modelo,com,prec,uni) #Enviamos los datos a la funcion de facturacion para procesar la compra
    else:
        if op==2:
            print("No se confirmo la compra") #Regresamos al catalogo
            print("Redirigiendo al catalogo")
            os.system("pause")
            catalogo()

def ventas(fecha,nombre,nit,producto,unidades,color,modelo,com,prec,total): #Funcion para crear el control de las ventas recibe los datos de la funcion facturacion para grabrlos
    cliente=[] #Lista par guardar datos de la venta
    compr=float(com) #Recuperamos los valores recibidos
    preci=float(prec) #Recuperamos los valores recibidos
    ganancia=((preci-compr)*unidades) #Operacion para calcular ganancia
    venta=(fecha,nombre,producto,modelo,unidades,compr,preci,ganancia) #Guardamos los datos en una variable
    cliente.append(venta) #Grabamos los datos en la lista

    guardar=open("ventas.txt","a+") #Realizamos la creacion a añadir los datos
    for venta in cliente:
        linea=fecha+","+nombre+","+nit+","+producto+","+modelo+","+str(unidades)+","+str(compr)+","+str(preci)+","+str(total)+","+str(ganancia)+"," #Definimos como guardar los datos
        guardar.write(linea + '\n') #Guardamos los datos en el archivo de texto
    guardar.close() #Cerramos


#MODULO FACTURACION
def encabezado():  #Encabezado de las facturas  
    print(" --- VENTA DE MOTOS X-FORCE ---")
    print("     OPERADORA DE TIENDAS S.A.")
    print("VENTA DE MOTOS CHIMALTENANGO")
    print("       7A. CALLE 2-02 ZONA 2")
    print("         TEL: 1234 - 5678\n")


def facturacion(nom,color,modelo,com,prec,uni): #Recibimos los datos de la funcion anterior
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


        input("Para continuar, presione la tecla Enter...")
        ventas(fecha,nombre,nit,producto,unidades,color,modelo,com,prec,total) #Enviamos los datos a la funcion para guardar datos de las ventas
        baja(producto,unidades) #Enviamos datos para realizar la modificacion en el inventario

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