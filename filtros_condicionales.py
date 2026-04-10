from main import df

# 1. Altos Ingresos
altos_ingresos = df[df['Salario_COP'] > 10000000]

# 2. Sede Principal
sede_medellin = df[df['Ciudad'] == 'Medellín']

# 3. Experiencia Senior
senior = df[df['Experiencia_Años'] > 15]

# 4. Investigación Remota
remoto_doctorado = df[(df['Nivel_Estudio'] == 'Doctorado') & (df['Remoto'] == True)]

# 5. Segmento Joven
segmento_joven = df[(df['Edad'] >= 25) & (df['Edad'] <= 30)]

# 6. Salarios Bajos
salarios_bajos = df[df['Salario_COP'] < 4000000]

# 7. Especialista Valle
especialista_cali = df[(df['Ciudad'] == 'Cali') & (df['Nivel_Estudio'] == 'Especialización')]

# 8. Altos Salarios Junior
altos_junior = df[(df['Experiencia_Años'] < 5) & (df['Salario_COP'] > 4000000)]

# 9. Nivel Técnico
nivel_tecnico = df[df['Nivel_Estudio'].isin(['Tecnología', 'Pregrado'])]

# 10. Presencialidad Santander
presencial_bucaramanga = df[(df['Ciudad'] == 'Bucaramanga') & (df['Remoto'] == False)]