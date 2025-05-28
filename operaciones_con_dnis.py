# Código base en Python de las operaciones con DNIs.

from functools import reduce

# Guardamos los nombres y DNIs en listas paralelas. El índice i en nombres[i] corresponde al mismo índice en dnis[i].
nombres = ['A (Julian)', 'B (Celeste)', 'C (Juan Pablo)', 'D (Guillermo)', 'E (Matias)']
dnis = ['45568971', '30799014', '34197659', '42042862', '43988550']

# Generamos una lista con los conjuntos de dígitos únicos de cada DNI. Usamos set(dni) para eliminar dígitos repetidos.
conjuntos_digitos = [set(dni) for dni in dnis]

# Mostramos los conjuntos de dígitos únicos por persona.
print("\nConjuntos de dígitos únicos:")
for i in range(len(nombres)):
    print(f"{nombres[i]}: {conjuntos_digitos[i]}")

# Realizamos las operaciones entre conjuntos
union_total = set.union(*conjuntos_digitos)
interseccion_total = set.intersection(*conjuntos_digitos)
diferencias = [conjuntos_digitos[i] - union_total.difference(conjuntos_digitos[i]) for i in range(len(dnis))]
diferencia_simetrica = reduce(lambda x, y: x.symmetric_difference(y), conjuntos_digitos)

print("\nOperaciones entre conjuntos:")
print(f"Unión total: {union_total}")
print(f"Intersección total: {interseccion_total}")
print("Diferencias por persona:")
for i in range(len(nombres)):
    print(f"{nombres[i]}: {diferencias[i]}")
print(f"\nDiferencia simétrica: {diferencia_simetrica}")

# Realizamos el conteo de frecuencia de cada dígito y la suma total
print("\nFrecuencia y suma de dígitos:")
for i in range(len(dnis)):
    dni = dnis[i]
    frecuencias = [0] * 10  # índices del 0 al 9
    suma = 0
    for dig in dni:
        dig_int = int(dig)
        frecuencias[dig_int] += 1
        suma += dig_int
    # Mostramos la frecuencia no cero
    frec_utiles = {str(i): frecuencias[i] for i in range(10) if frecuencias[i] > 0}
    print(f"{nombres[i]}: Frecuencias: {frec_utiles}, Suma: {suma}")

# Evaluaciones lógicas
print("\nEvaluación de condiciones lógicas:")

# ¿Todos los conjuntos tienen al menos 6 elementos?
diversidad_alta = all(len(conjunto) >= 6 for conjunto in conjuntos_digitos)
print(f"Diversidad alta: {'Verdadero' if diversidad_alta else 'Falso'}")

# ¿Algún dígito aparece en todos los conjuntos?
if interseccion_total:
    print(f"Dígito(s) común(es): {', '.join(interseccion_total)}")
else:
    print("No hay dígitos comunes.")

# ¿Intersección total con exactamente un elemento?
if len(interseccion_total) == 1:
    print(f"Dígito representativo: {next(iter(interseccion_total))}")
else:
    print("No hay dígito representativo.")