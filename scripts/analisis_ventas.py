import pandas as pd

#Creacion de datos
data = {
    "producto": ["Queso", "Fideos", "Leche", "Arroz", "Arvejas"],
    "cantidad": [2, 1, 3, 1, 2],
    "precio": [170, 70, 100, 50, 30]
}

df = pd.DataFrame(data)

#Guardar CSV
df.to_csv("datos/ventas.csv", index=False)

df = pd.read_csv("datos/ventas.csv")

#Calcular total
df["total"] = df["cantidad"] * df["precio"]

print("Tabla de productos:")
print(df)

print("\nTotal:")
print(df["total"].sum())

#Analisis por producto
ranking = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False)
print("\nVentas por producto:")
print(ranking)

#Exportar resultado
resultado = df.groupby("producto")["cantidad"].sum()
resultado.to_csv("resultados/ventas_por_producto.csv")