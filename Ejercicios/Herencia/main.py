import clases

persona = clases.persona()
persona.setNombre("Daniel")
persona.setApellido("Castaño")
persona.setAltura("170 cm")
persona.setEdad("28")

#print(f"La persona es {persona.getNombre()}")
print(persona.hablar())

developer = clases.Informatico()

print(developer.getLenguajes())

developer.aprenderLenguajes("Java")

print(developer.getLenguajes())

developer.aprenderLenguajes("HTML")

print(developer.getLenguajes())

print(developer.)