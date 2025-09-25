from models.mascota import Mascota


class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        self.mascotas_adoptadas = []

    def __str__(self) -> str:
        return f"{self.nombre}, {self.edad} años"
    
    def presentarse(self) -> str:
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
    def adoptar_mascota(self, mascota: Mascota) -> Mascota | None:
        if mascota.adoptado:
            return None
        else:
            mascota.adoptado = True
            self.mascotas_adoptadas.append(mascota)
            return mascota