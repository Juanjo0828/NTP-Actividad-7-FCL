from main import df

# 1. Primeros Registros
primeros_5 = df.iloc[0:5]

# 2. Punto Central
fila_24 = df.iloc[24]

# 3. Columnas Alternas
cols_alternas = df.iloc[0:10, [0, 2, 5]]

# 4. Dato Específico
valor_celda = df.iloc[10, 3]

# 5. Último Decil
ultimas_10 = df.iloc[-10:]

# 6. Subsección de Matriz
subseccion = df.iloc[15:26, 1:5]

# 7. Propiedades Finales
ultimas_2_cols = df.iloc[:, -2:]

# 8. Muestreo Estratificado
filas_especificas = df.iloc[[0, 10, 20, 30, 40], [0, 5]]

# 9. Segmento Final
segmento_final = df.iloc[-10:, 0:3]

# 10. Inversión
df_invertido = df.iloc[::-1]