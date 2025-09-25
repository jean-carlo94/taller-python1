from models.mascota import Mascota
from models.persona import Persona

class Refugio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._mascotas = []
        
    def __str__(self) -> str:
        return f"Refugio {self.nombre} con {len(self._mascotas)} mascotas."

    def registrar_mascota(self, mascota: Mascota):
        self._mascotas.append(mascota)

    def listar_mascotas(self) -> list[Mascota]:
        return [str(mascota) for mascota in self._mascotas]

    def listar_mascotas_adoptadas(self) -> list[Mascota]:
        mascotas_adoptadas = []
        
        for mascota in self._mascotas:
            if not mascota.adoptado: continue
            
            mascotas_adoptadas.append(mascota) 
            
        return mascotas_adoptadas

    def listar_mascotas_disponibles(self) -> list[Mascota]:
        mascotas_disponibles = []
        
        for mascota in self._mascotas:
            if mascota.adoptado: continue
            
            mascotas_disponibles.append(mascota) 
            
        return mascotas_disponibles
    
    def asignar_adopcion(self, persona:Persona, mascota: Mascota) -> Mascota | None:
        if mascota in self._mascotas:
            return persona.adoptar_mascota(mascota)
        else:
            return None
        
    