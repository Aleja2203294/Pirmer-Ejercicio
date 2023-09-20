#Los ciclos para la programación son secuenciales que permiten la realización o ejecución de funciones para poder abreviar
#o automatizar código, esta el ciclo "for" que significa "para" y el ciclo "while" que significa "mientras que"


print ("Tipo de programa que incluya un ciclo")

print ("----------INICIO DEL CICLO-----------")

import random 
for i in range (10):
    print (i**2)

print ("----------FINALICE EL CICLO-----------")

#El programa que vamos a realizar tiene como finalidad hacer un ciclo en donde le pida ingresar hasta 3 un número, en este caso la edad,
#y cuando genere la variable correcta ejecute en pantalla la siguiente acción, por ejemplo: Digita tu número de cédula, 3. Digite si desea
#saber el núemro de silla donde fue asignado.

print("ADMISIÓN PARA ENTRAR")

Nombre = str (input("Por favor, escriba su nombre completo:"))
Edad = float (input ("Digite su edad en número:"))
Identificación = float (input("Por favor, escriba su número de identificación sin ninguna simbología:"))
Lista_Edades = ["15","16","17","18","19","20"]
Lista_Admitidos = ["15","16","17","18","19","20"]

#for Lista_Edades in range (1):
    #print(Edad>=15)

#if Edad >= 15:
    #print("Admitido")

#else:
    
    #print("No Admitido")
while (Lista_Edades >= 15):
    print ("Está admitido, su edad es  ", Edad)
else: 
    print ("No está admitido, su edad es  ", Edad)

    #print("Gracias" , Nombre, "Tu número asignado es el siguiente:", random)

    #Vamos a medir la distancia de un corredor realizando un ciclo While que permita calcular o efectura 
#empleandose las variables velocidad x tiempo, y en ese sentido calcular la distancia que ejecuta
#el corredor 

Distancia = 0

while (Distancia <= 1500): 
    velocidad = float (input("Digite la velocidad que quiere que el atleta desarrolle (m/s):  "))
    tiempo = int (input("Digite el tiempo que obtuvo el atleta en el momento de desplazarse:  "))

    Distancia = velocidad * tiempo 

    if (Distancia <= 1500):
        print ("El atleta corrió" , Distancia , "Metros recorridos")
        print ("La distancia recorrida mínima debe ser mayor a 1500 m ")
    else:
        print ("El atleta recorrió " , Distancia , "Metros")
        print ("El atleta recorrió más de 1500 m ")