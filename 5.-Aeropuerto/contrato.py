
class Contratato:
    def __init__(self):
        self.matrizContrato = []


    def llenarDatos(self):
        print("Seleccione un contrato")
        print("1. Contrato de turista\n2.-Sucursal\n3.-Hotel\n4.-Vuelo")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
           from turista import MenuTurista
           menuTurista = MenuTurista()
           menuTurista.mainTurista()
        elif opcion == 2:
            from sucursal import MenuSucursal
            menuSucursal = MenuSucursal()
            menuSucursal.mainSucursal()
            self.llenarDatos()
        elif opcion == 3:
            from hoteles import MenuHotel
            menuHotel = MenuHotel()
            menuHotel.mainHotel()
            self.llenarDatos()
        elif opcion == 4:
            from vuelos import MenuVuelo
            menuVuelo = MenuVuelo()
            menuVuelo.mainVuelo()
            self.llenarDatos()
        else:
            print("Opcion invalida")
            self.llenarDatos()
       

    def llenarContrato(self):
        #Voy a conactenar la matriz turista con la matriz contrato
        print("Selecciones que turista es")
        from turista import MenuTurista
        menuTurista = MenuTurista()
        menuTurista.printTurista()
        print("Seleccione una opcion")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            self.matrizContrato.append(self.matrizTurista[0])
        elif opcion == 2:
            self.matrizContrato.append(self.matrizTurista[1])
        elif opcion == 3:
            self.matrizContrato.append(self.matrizTurista[2])
        elif opcion == 4:
            self.matrizContrato.append(self.matrizTurista[3])
        else:
            print("Opcion no valida")


