#Ejercicio 5. Cálculo con formula general

#ENTRADA DE DATOS
mes = input("Escriba el mes de nomina ")
dias_laborables = int(input("Escriba los dias laborables "))
pago_por_dia = float(input("Escriba el salario diario $"))
IVA = .16
ISR = .10


#PROCESOS
pago_bruto_mensual = dias_laborables * pago_por_dia
iva_trasladado = pago_bruto_mensual * IVA
subtotal = pago_bruto_mensual + iva_trasladado
iva_retenido = (2*iva_trasladado)/3
isr_retenido = pago_bruto_mensual * ISR
pago_neto = subtotal - iva_retenido - isr_retenido

#SALIDA DE DATOS
print(f"El total a pagar en el mes de {mes} es de ${round(pago_neto,2)}")