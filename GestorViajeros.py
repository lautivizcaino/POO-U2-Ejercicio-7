from Viajero import ViajeroFrecuente
import csv

class GestorViajeros:
    def __init__(self):
        self.__listaViajeros= []

    def agregarViajero(self,viajero):
        self.__listaViajeros.append(viajero)
    
    def leerArchivo(self): 
        File = open('archivo.csv')
        reader = csv.reader(File,delimiter=',')
        for row in reader:
            num_viajero= int(row[0])
            dni = row[1]
            nombre = row[2]
            apellido = row[3]
            millas_acum = int(row[4])
            UnViajero= ViajeroFrecuente(num_viajero,dni,nombre,apellido,millas_acum)
            self.agregarViajero(UnViajero)
        File.close()
    def buscarViajero(self,viajero):
        for v in self.__listaViajeros:
            if v.getNum()==viajero:
                return v
    def compararCantMillas(self,viajero,n):
        if viajero==n:
            print('viajero==n: {}'.format(viajero==n))
        if n==viajero:
            print('n==viajero: {}'.format(n==viajero))
    def acumularMillas(self,viajero,millas):
        viajero=millas+viajero
        print(viajero.cantidadMillas())
    def canjearMillas(self,viajero,millas):
        viajero=millas-viajero
        print(viajero.cantidadMillas())
    def __str__(self):
        v=''
        for viajero in self.__listaViajeros:
            v+= str(viajero) + '\n'
        return v
