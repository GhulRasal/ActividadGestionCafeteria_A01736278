#
# José Luis Zago Guevara  |  A01736278
# Actividad | Pruebas Sistema de Gestión de Cafetería
# TC3005B.502
#

def funcionBeb(entrada):
  # Eliminar espacios en blanco y partir entrada en secciones
  entrada = entrada.replace(" ", "")
  secciones = entrada.split(",")
  nombre = secciones[0]
  sizes = secciones[1:]
  
 #Nombre primero, alfabético y de 2 - 15 caracteres.
  if nombre.isnumeric() or nombre == "":
    return "Inválida: el nombre de la bebida debe ir primero"
  if not nombre.isalpha():
    return "Inválida: nombre de bebida debe contener únicamente caracteres alfabéticos"
  elif len(nombre) < 2 or len(nombre) > 15:
    return "Inválida: nombre de bebida debe ser entre 2 y 15 caracteres"

  #Tamaños de Bebida en buen formato y orden.
  if len(sizes) < 1 or len(sizes) > 5:
    return "Inválida: ingresa de 1 a 5 números enteros separados por una coma"
  sizes_enteros = []
  for size in sizes:
        try:
            size_entero = int(size)
            if size_entero < 1 or size_entero > 48:
                return "Inválida: ingresa números enteros entre 1 y 48"
            sizes_enteros.append(size_entero)
        except ValueError:
            return "Inválida: ingresa números enteros entre 1 y 48, sin espacios en blanco"
  if sizes_enteros != sorted(sizes_enteros):
    return "Inválida: los números del tamaño deben ir en orden ascendente"

  return "Válida"