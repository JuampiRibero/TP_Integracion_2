from itertools import product

# Lista de años de nacimiento
anios = [2004, 1984, 1989, 1999, 2002]

# Clasificación en pares e impares
pares = [anio for anio in anios if anio % 2 == 0]
impares = [anio for anio in anios if anio % 2 != 0]

# Años bisiestos (divisibles por 4, no por 100, excepto si son divisibles por 400)
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

bisiestos = [anio for anio in anios if es_bisiesto(anio)]

# Verificación: ¿Todos nacieron después del 2000?
todos_despues_2000 = all(anio > 2000 for anio in anios)

# Edades en 2025
edades = [2025 - anio for anio in anios]

# Producto cartesiano entre años y edades
producto_cartesiano = list(product(anios, edades))

# Resultados
print("Años:", anios)
print("Pares:", pares)
print("Impares:", impares)
print("Años bisiestos:", bisiestos)
print("¿Todos nacieron después del 2000? →", "✅ Sí" if todos_despues_2000 else "❌ No")
print("Edades en 2025:", edades)
print("Producto cartesiano (año, edad):")
for par in producto_cartesiano:
    print(par)
 