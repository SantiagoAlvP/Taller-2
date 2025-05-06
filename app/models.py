class Pokenea:
    def __init__(self, id, nombre, altura, habilidad, imagen, frase):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.habilidad = habilidad
        self.imagen = imagen
        self.frase = frase

pokeneas = [
    Pokenea(1, "Paisita", "1.5m", "Jugar guitarrón", "paisita.png", "Más vale maña que fuerza"),
    Pokenea(2, "Arrierito", "1.7m", "Cargar al hombro", "arrierito.png", "No hay atajo sin trabajo"),
    Pokenea(3, "Silletero", "1.6m", "Cargar flores", "silletero.png", "La vida es como un ramo, hay que saberla arreglar"),
    Pokenea(4, "Cafetero", "1.8m", "Preparar tinto", "cafetero.png", "El café como la vida, debe ser fuerte y caliente"),
    Pokenea(5, "Montañero", "1.9m", "Subir cerros", "montañero.png", "El que no conoce Dios, cualquier monte le parece alto"),
    Pokenea(6, "Chocolatero", "1.4m", "Hacer chocolates", "chocolatero.png", "La vida es como el chocolate, amarga sin dulzura"),
    Pokenea(7, "Tabacalero", "1.7m", "Cultivar tabaco", "tabacalero.png", "El humo de la experiencia nunca se va del todo")
]