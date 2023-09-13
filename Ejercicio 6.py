#Este programa va a tener como finalidad mezclar varios elementos que pueda solicitar el usuario o
#vamos a colocar diferentes métodos para poder realizar actividades simples o secuenciales 
#del mismo modo, permitirá realizar salidas de información sujetasa condiciones lógicas 

print ("--------- inicio del programa----------")

print = input ("Ingrese su nombre completo:  ")

Edad1 = int(input("¿Cual es su edad?:  "))

if Edad1 < 18: 
    print ("eres menor de edad.")
else: 
    print ("eres mayor de edad.")


#Acá el usuario una vez se establece si es mayor de edad, le vamos a solicitar una contraseña 

ClaveMayorEdad = ("--------- módulo de seguridad ---------")

print("Su contraseña fue enviada exitosamente a su correo")

Contraseña = input ("Por favor, introduce tu contraseña:  ")
ClaveMayorEdad = "Contraseña"
Password = input * ("Ingrese la contraseña que fue enviada a su correo")

if ClaveMayorEdad == Password.lower ():
    print ("Contraseña correcta")
else: 
    print ("Contraseña incorrecta")

print ("---------- módulo 3 de interacción -----------")

print ("Escriba una frase o palabra para seguir adelante en la autenticación")

frase = input ("Introduce una frase")

#Si se desea reemplazar la contraseña, solicite al usuario escribir en diferentes letras o números 
#la nueva contraseña o simplemente solicite un parámetro de validación 

vocal = input ("Introduzca una vocal en minúscula")
print (frase.replace(vocal, vocal.upper))

print ("Usted ha completado los tres módulos de autenticación / puede seguir adelante con el pago")
