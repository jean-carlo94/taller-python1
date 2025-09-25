class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, adoptado: bool = False):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.adoptado = adoptado

    def __str__(self) -> str:
        return f"{self.nombre} es un(a) {self.especie} de {self.edad} años y " + ("está adoptado." if self.adoptado else "no está adoptado.")
    
MASCOTAS = [
    Mascota("Firulais", "Perro", 3),
    Mascota("Michi", "Gato", 2),
    Mascota("Nemo", "Pez", 1),
    Mascota("Paco", "Loro", 4),
    Mascota("Bunny", "Conejo", 2),
]