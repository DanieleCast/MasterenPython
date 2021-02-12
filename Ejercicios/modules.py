import datetime
fecha = datetime.datetime.now()
print (fecha.year)
print(fecha.day)
print(fecha.month)

fecha_format = fecha.strftime("%d/%m/%Y, %H:%M")
print(f"La Fecha es: {fecha_format}")