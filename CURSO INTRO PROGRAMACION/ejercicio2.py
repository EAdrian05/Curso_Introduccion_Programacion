#Ejercicio 2. Calcular área y perimetro de un circulo

#ENTRADA DE DATOS
PI = 3.1416
radio = float(input("Escriba el valor de radio "))

#PROCESOS
area = PI * pow(radio,2)
perimetro = 2 * PI * radio


#SALIDA DE DATOS
print("El área es = ", round(area,2))
print("El perimetro es = ", round(perimetro,2))