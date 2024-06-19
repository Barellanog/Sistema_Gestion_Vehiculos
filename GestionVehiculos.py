import FuncionesVehiculos as fv

while True:
    fv.limpiar()
    fv.menu()
    opcion = input("Seleccione: ")
    
    if opcion == "0":
        fv.printB("Gracias por ocupar el sistema de gestión de vehiculos")
        break
    if opcion == "1":
        fv.AgregarVehiculo()
    if opcion == "2":
        fv.ListarVehiculos()
    if opcion == "3":
        fv.EliminarVehiculo()
    if opcion == "4":
        fv.ModificarVehiculo()
    if opcion == "5":
        fv.FiltrarVehiculos()
    if opcion == "6":
        fv.GenerarReporte()