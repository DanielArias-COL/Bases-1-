from datetime import datetime

# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Convertir la fecha y hora actual al formato de texto 'YYYY-MM-DD HH:MM:SS'
fecha_entrada = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')

# Ahora puedes usar fecha_entrada para insertar en tu base de datos

print(fecha_actual)
print(fecha_entrada)