#Ejercicio 5. Cálculo con formula general

#ENTRADA DE DATOS
a = int(input("Escriba el valor de a "))
b = int(input("Escriba el valor de b "))
c = int(input("Escriba el valor de c "))


#PROCESOS
formula_general = (-(b)-(pow(pow(b,2)-(4*a*c),1/2)))/(2*a)
formula_general_2 = (-(b)+(pow(pow(b,2)-(4*a*c),1/2)))/(2*a)

#SALIDA DE DATOS
print("El resultado es igual a ",formula_general)
print("El resultado es igual a ",formula_general_2)
