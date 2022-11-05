#Ejercicio 4. Conversion de grados

#ENTRADA DE DATOS
grados_c = int(input("Escriba la cantidad en grados Celcius "))
CONST_C_A_F = 273.15

#PROCESOS
grados_c_a_f = (grados_c * 9/5) + 32
grados_c_a_K = grados_c + CONST_C_A_F


#SALIDA DE DATOS
print("Es igual a ",grados_c_a_f,"Fahrenheit")
print("Es igyal a ",grados_c_a_K,"Kelvin")