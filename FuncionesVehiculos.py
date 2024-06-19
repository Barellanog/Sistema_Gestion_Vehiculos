import os
import csv
import msvcrt
from colorama import Back,Style,Fore

coleccion_vehiculos = []
marcas_vehiculos = ("Kia","Chevrolet","Audi","Nissan","Otro")
tipos_vehiculos = ("Automovil","Camion","Autobus","Motocicleta")
stock_vehiculos = {"Kia": 10,
                   "Chevrolet": 10,
                   "Audi": 10,
                   "Nissan": 10,
                   "Otro": 20}

def printR(texto):
    print(f"{Fore.RED}{texto}{Style.RESET_ALL}")

def printG(texto):
    print(f"{Fore.GREEN}{texto}{Style.RESET_ALL}")

def printB(texto):
    print(f"{Fore.BLUE}{texto}{Style.RESET_ALL}")

def limpiar():
    print("<<Press any key>>")
    msvcrt.getch()
    os.system('cls')
    
def menu():
    printG("Sistema de Gestion de Vehiculos")
    print("-------------------------------------")
    print("1) Agregar Vehiculo")
    print("2) Listar Vehiculos")
    print("3) Eliminar Vehiculo")
    print("4) Modificar Vehiculo")
    print("5) Filtrar Vehiculos por marca")
    print("6) Generar reporte de vehiculos")
    print("0) Salir")
    print("-------------------------------------")
 
def ValidarPatente(patente):
    for i in range(len(coleccion_vehiculos)):
        if coleccion_vehiculos[i][0] == patente:
            return i
    return -1
    
def AgregarVehiculo():
    limpiar()
    printB("Agregar Vehiculo")
    while True:
        patente = input("Ingresa la patente (4 Letras y 2 Numeros o 2 Letras y 4 Numeros): ").upper()
        if ValidarPatente(patente) == -1:
            if len(patente) == 6:
                printG("Patente registrada")
                limpiar()
                break
            else:
                printR("Patente no valida")
        else:
            printR("Patente repetida")
    
    printB("Marcas disponibles: ")
    for i, marca in enumerate(stock_vehiculos):
        print(f"{i+1}) {marca}: {stock_vehiculos[marca]}")
    while True:
        marca = input("Ingresa la marca: ").title()
        if marca in marcas_vehiculos:
            stock_vehiculos[marca] -= 1
            printG("Marca Registrada")
            limpiar()
            break
        else:
            printR("La marca no existe")
        
    print("Tipos de Vehiculo: ")
    for i in range(len(tipos_vehiculos)):
        print(f"{i+1}) {tipos_vehiculos[i]}")
    while True:
        tipo = input("Ingresa el tipo: ").title()
        if tipo in tipos_vehiculos:
            printG("Tipo Registrado")
            limpiar()
            break
        else:
            printR("El tipo no existe")
    while True:   
        try:
            precio = float(input("Ingresa el precio: "))
            printG("Precio Registrado")
            break
        except:
            printR("El precio no es valido")
    
    coleccion_vehiculos.append([patente, marca, tipo, precio])
    

def ListarVehiculos():
    if len(coleccion_vehiculos) > 0:
        for i in range(len(coleccion_vehiculos)):
            printB("=============================")
            printG(f"Vehiculo N°{i+1}")
            print(f"Patente:   {coleccion_vehiculos[i][0]}\nMarca:     {coleccion_vehiculos[i][1]}\nTipo:      {coleccion_vehiculos[i][2]}\nPrecio:    {coleccion_vehiculos[i][3]}")
            printB("=============================") 
    else:
        printR("No hay vehiculos registrados")
        
def EliminarVehiculo():
    printG("Eliminar Vehiculo")
    patente = input("Ingresa la patente del vehiculo: ").upper()
    posicion = ValidarPatente(patente)
    if posicion >= 0:
        coleccion_vehiculos.pop(posicion)
        printG("Vehiculo Eliminado")
    else:
        printR("La patente no existe")

def ModificarVehiculo():
    printB("Modificar Vehiculo")
    patente = input("Ingresa la patente del vehiculo: ").upper()
    posicion = ValidarPatente(patente)
    if posicion >= 0:
        printG("Patente encontrada")
        printB("Marcas disponibles: ")
        for i, marca in enumerate(stock_vehiculos):
            print(f"{i+1}) {marca}: {stock_vehiculos[marca]}")
        while True:
            marca = input("Ingresa la marca: ").title()
            if marca in marcas_vehiculos:
                stock_vehiculos[marca] -= 1
                printG("Marca Registrada")
                limpiar()
                break
            else:
                printR("La marca no existe")
        
        printB("Tipos de Vehiculo: ")
        for i in range(len(tipos_vehiculos)):
            print(f"{i+1}) {tipos_vehiculos[i]}")
        while True:
            tipo = input("Ingresa el tipo: ").title()
            if tipo in tipos_vehiculos:
                printG("Tipo Registrado")
                limpiar()
                break
            else:
                printR("El tipo no existe")
        while True:
            try:
                precio = float(input("Ingresa el precio: "))
                printG("Precio Registrado")
                break
            except:
                printR("El precio no es valido")
        
        coleccion_vehiculos[posicion] = [patente, marca, tipo, precio]
    else:
        printR("No se ha encontrado la patente")

def FiltrarVehiculos():
    printB("Filtrar Vehiculos")
    for i, marca in enumerate(stock_vehiculos):
        print(f"{i+1}) {marca}")
    marca = input("Ingresa la marca: ").title()
    if marca in marcas_vehiculos:
        for i in range(len(coleccion_vehiculos)):
            if marca == coleccion_vehiculos[i][1]:
                printB("=============================")
                printG(f"Vehiculo N°{i+1}")
                print(f"Patente:   {coleccion_vehiculos[i][0]}\nMarca:     {coleccion_vehiculos[i][1]}\nTipo:      {coleccion_vehiculos[i][2]}\nPrecio:    {coleccion_vehiculos[i][3]}")
                printB("=============================")
            else:
                printR("No hay vehiculos de esa marca registrados")

def GenerarReporte():
    if len(coleccion_vehiculos) > 0:
        printB("Reporte de vehiculos")
        with open('ReporteVehiculos.csv', 'w',newline='',encoding='utf-8') as a:
            escribir = csv.writer(a,delimiter=",")
            escribir.writerows(coleccion_vehiculos)
            printG("Reporte Generado")
    else:
        printR("No hay vehiculos registrados para el reporte")