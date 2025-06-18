try:
  num1 = float(input("Introduce el Numerador: "))
  num2 = float(imput("Introduce el Denominador: "))
  resultado = num1 / num2
  print("El resultado es:", resultado)
except ZeroDivisionError:
  print("Error: No se puede Dividir entre cero")
except ValueError:
  print("Error: Introduce un Numero Valido")
