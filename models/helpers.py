from models.refugio import Refugio
from models.mascota import Mascota
from models.persona import Persona

r = Refugio("Hogar de Patitas")

# Imprimir Lista de mascotas
def print_lis_mascotas(mascotas: list[Mascota]):
    for i in range(len(mascotas)):
        print(f"| \033[45m({i + 1}).\033[0m \033[32m{mascotas[i]}\033[0m")

# Listar mascotas
def listar_mascotas():
    mascotas = r.listar_mascotas()
    
    if(len(mascotas) == 0):
        print("|\033[33m No hay mascotas disponibles en este momento.\033[0m")
        return

    print_lis_mascotas(mascotas)
    
# Listar mascotas disponibles 
def listar_mascotas_disponibles():
    mascotas_disponibles = r.listar_mascotas_disponibles()
    
    if(len(mascotas_disponibles) == 0):
        print("|\033[33m No hay mascotas disponibles para adoptar en este momento.\033[0m")
        return

    print_lis_mascotas(mascotas_disponibles)
        
# Listar mascotas adoptadas
def listar_mascotas_adoptadas():
    mascotas_adoptadas = r.listar_mascotas_adoptadas()
    
    if(len(mascotas_adoptadas) == 0):
        print("|\033[33m No hay mascotas adoptadas en este momento.\033[0m")
        return

    print_lis_mascotas(mascotas_adoptadas)
    
# Buscar mascotas
def buscar_mascota_por_nombre():
    nombre = input("|\033[46m Ingrese el nombre de la mascota que desea buscar: \033[0m")
    mascotas = r.listar_mascotas()
    resultado = [mascota for mascota in mascotas if nombre.lower() in mascota.lower()]
    
    if len(resultado) == 0:
        print(f"|\033[33m No se encontraron mascotas con el nombre '{nombre}'.\033[0m")
    else:
        print_lis_mascotas(resultado)

    retry = str(input("|\033[34m Buscar Nuevamente?: (\033[32mSI\033[0m/\033[31mNO\033[0m) \033[0m")).upper()
    
    if(retry == 'SI'):
        buscar_mascota_por_nombre()
    else:
        return
        
# Registrar mascotas   
def registrar_mascota():
    try:
        nombre = str(input("|\033[44m Ingrese el nombre de la Mascota: \033[0m"))
        edad = int(input("|\033[44m Ingrese la edad (años) de la Mascota: \033[0m"))
        especie = str(input("|\033[44m Ingrese la especie de la Mascota: \033[0m"))
    except ValueError:
        print("|\033[31m El Tipo de dato es invalido \033[0m")
        return

    nueva_mascota = Mascota(nombre, especie, edad)
    r.registrar_mascota(nueva_mascota)
    
    print(f"|\033[32m La mascota {nueva_mascota.nombre} ha sido registrada exitosamente. \033[0m")
    print(f"|\033[32m {nueva_mascota} \033[0m")
    return

# Registrar personas
def registrar_persona():
    try:
        nombre = str(input("|\033[44m Ingrese el nombre de la Persona: \033[0m"))
        edad = int(input("|\033[44m Ingrese la edad (años) de la Persona: \033[0m"))
    except ValueError:
        print("|\033[31m El Tipo de dato es invalido \033[0m")
        return

    nueva_persona = Persona(nombre, edad)
    
    print(f"|\033[32m La Persona {nueva_persona.nombre} ha sido registrada exitosamente. \033[0m")
    
    return nueva_persona

# Adoptar mascotas 
def adoptar_mascota():    
    adoptante = registrar_persona()
    listar_mascotas_disponibles()
    
    if(len(r._mascotas) == 0): return
    
    try:
        numero = int(input("|\033[44m Ingrese el numero de la mascota que desea adoptar: \033[0m"))
    except ValueError:
        print("|\033[31m El Tipo de dato es invalido \033[0m")
        return

    try:
        mascota_adopcion = r._mascotas[numero - 1]
    except Exception:
        print("|\033[33m La mascota no se encuentra disponible \033[0m")
        return
        
    adopcion = r.asignar_adopcion(adoptante,mascota_adopcion)
    
    if(not adopcion):
        print(f"Lo siento, {mascota_adopcion.nombre} no está en el refugio.")
        
    print(f"|\033[32m La Persona {adoptante.nombre} a adoptado a {mascota_adopcion.nombre} Exitosamente \033[0m")    
    
    return