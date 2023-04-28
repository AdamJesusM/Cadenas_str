#concatenar (hacer una cadena) (+=)
mensaje = ("hola")
mensaje += (" ")
mensaje += ("gente")
khazix = (" hijos mios")
print("concatenacion de datos",mensaje+khazix)

#buscar la poscision de datos (.find)
buscar = mensaje.find("gente")
print(buscar)
extraer = mensaje[5:10]
print("esto es la extraccion de una parte de lo datos",extraer)

#transformar valor numerico a texto en cadena (str)=(string)=(cadena)
numero_1 = 4
numero_2 = 6
print(numero_1, "+", numero_2)
resultado = (numero_1+numero_2) 
resulatado = str(resultado)
print("el resultado de los numeros es: " + resulatado)

#comparacion ==
print("comparacion",)
msj_1 = "hola"
msj_2 = "holaa"
print(msj_1 == msj_2)


