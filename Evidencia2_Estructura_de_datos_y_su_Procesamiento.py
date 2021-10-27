#EVIDENCIA 2
from collections import namedtuple
import datetime
import pandas as pd
import csv
import os
import sys
#
#Creamos tupla
Ventas = namedtuple("Ventas", "folio, fecha, descripcion, cantidad, precio, total")
#
#Creamos un diccionario donde se almacenara la lista
DiccionarioVentas = {}
DiccionarioVentascsv = {}
#
#
SEPARADOR = ("*" * 20) + "\n"
#
while True:  
#  
    print("\nMENÚ")
    print("1) Agregar venta")
    print("2) Busqueda especifica")
    print("3) Mostrar todas las ventas")
    print("4) Registro ventas por fecha")
    print("5) Salir y guardar")
#  
    respuesta = int(input("Elija una opción: "))
#   
#    
    if respuesta == 1:
        #Se crea la lista
        lista_ventas = []
        try:
            with open('Ventas.csv','r',newline = '') as archivo:
                lector = csv.reader(archivo)
                next(lector)
                for folio, fecha, descripcion, cantidad, precio, total in lector:
                    venta = Ventas(folio, fecha, descripcion,cantidad,precio,total) 
                    lista_ventas.append(venta)
                    DiccionarioVentas[folio] = lista_ventas                                    
        except FileNotFoundError:
                print('-------------')
                pass
        while True:
            folio = int(input('\nIngrese el folio: '))
            if folio in DiccionarioVentas.keys():
                print('Este folio ya existe, porfavor ingresa otro')
            else:
                break
        while True:
            agregarArticulo =1
            while agregarArticulo==1:
                fecha_capturada= input('Introduce una fecha (dd/mm/yyyy): ')
                fecha = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
                descripcion= input('Introduce un articulo: ')
                precio=int(input('Introduce el precio del articulo: '))
                cantidad = int(input('Introduce la cantidad: '))
                total = precio * cantidad
                # Almacenamiento en tuplas
                venta = Ventas(folio, fecha, descripcion,cantidad,precio,total) 
                lista_ventas.append(venta)
#                    
                # DiccionarioVentas
                DiccionarioVentas[folio] = lista_ventas
#              
                agregarArticulo=int(input('¿Desea añadir más articulos? \n1)Si \n2)No: '))
#                   
            break                       
#    
    elif respuesta == 2:
        busqueda = int(input("Ingresa el folio a buscar: "))
        if busqueda in DiccionarioVentas:
            df_DiccionarioVentas = pd.DataFrame(DiccionarioVentas[busqueda])
            print(df_DiccionarioVentas)
#           
            sumtotal = df_DiccionarioVentas["total"].sum()
            iva = sumtotal * .16
            totaliva = sumtotal + iva
            print(SEPARADOR)
            print(f"Total : ${sumtotal}")
            print(f"Total + IVA : ${totaliva}")
        else:
            print('El folio no está registrado')            
#          
    elif respuesta == 3:        
#           
        for busqueda in DiccionarioVentas:
            df_DiccionarioV = pd.DataFrame(DiccionarioVentas[folio])
            print(df_DiccionarioV)
#               
    elif respuesta == 4:
        fecha_capturadabus= input('Introduce una fecha a buscar (dd/mm/yyyy): ')
        fecha_capturadabusf = datetime.datetime.strptime(fecha_capturadabus, "%d/%m/%Y").date()
#        
        for busqueda in DiccionarioVentas:
            df_DiccionarioVb = pd.DataFrame(DiccionarioVentas[busqueda])
            busca_fecha = df_DiccionarioVb['fecha'] == fecha_capturadabusf
            print(df_DiccionarioVb[busca_fecha])
#              
            sumtotalv = df_DiccionarioVb[busca_fecha]["total"].sum()
            ivav = sumtotalv * .16
            totalivav = sumtotalv + ivav
            print(SEPARADOR)
            print(f"Total : ${sumtotalv}")
            print(f"Total + IVA : ${totalivav}")
#            
    elif respuesta == 5:
        print("Gracias por su compra, buen día")
        with open("Ventas.csv","w", newline="") as archivo:
            grabador = csv.writer(archivo)
            grabador.writerow(("Folio","Fecha", "Descripción", "Cantidad","Precio","Total"))
            for folio in DiccionarioVentas:
                for datos in DiccionarioVentas[folio]:
                    
                    grabador.writerows([(folio, datos.fecha, datos.descripcion, datos.cantidad, datos.precio, datos.total)])          
            
        print(f"\nGuardado CSV de manera correcta en {os.getcwd()}")
        break