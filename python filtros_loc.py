from main import df

# 1. Nómina Básica
nomina_basica = df.loc[:, ['Nombre', 'Salario_COP']]

# 2. Rango Geográfico
rango_geo = df.loc[10:20, ['Ciudad', 'Edad']]

# 3. Búsqueda Nominal
df_nombres = df.set_index('Nombre')
datos_elena = df_nombres.loc['Elena Marín']

# 4. Habilidades Maestría
maestria_exp = df.loc[df['Nivel_Estudio'] == 'Maestría', ['Experiencia_Años']]

# 5. Región Caribe
caribe_remoto = df.loc[df['Ciudad'] == 'Barranquilla', 'Nivel_Estudio':'Remoto']

# 6. Presupuesto Itagüí
salarios_itagui = df.loc[df['Ciudad'] == 'Itagüí', ['Salario_COP']]

# 7. Muestreo Intercalado
muestreo_intercalado = df.loc[df.index % 2 == 0, ['Nombre', 'Nivel_Estudio']]

# 8. Veteranía
veterania = df.loc[df['Edad'] > 40, ['Nombre', 'Remoto']]

# 9. Cierre de Lista
ultimos_registros = df.loc[df.index[-5:]]

# 10. Precisión de Años
precision_anos = df.loc[df['Experiencia_Años'] == 10, ['Ciudad']]