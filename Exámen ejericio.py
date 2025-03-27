import random 

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.historial_usuarios = {}

    def agregar_libro(self,titulo,autor,cantidad):
        if titulo in self.libros:
            self.libros[titulo] = (autor,self.libros[titulo][1] + cantidad)
        else: 
            self.libros[titulo] = (autor,cantidad) 

    def prestar_libro(self,usuario,titulo):
        if titulo in self.libros and self.libros[titulo][1] > 0:
            self.libros[titulo] = (self.libros[titulo][0], self.libros[titulo][1] - 1)
            if usuario not in self.historial_usuarios:
                self.historial_usuarios[usuario] = set()
            self.historial_usuarios[usuario].add(titulo)
            return True
        return False
    
    def devolver_titulo(self,titulo):
        if titulo in self.libros:
            self.libros[titulo] = (self.libros[titulo][0], self.libros[titulo][1]+1 )

    def esta_disponible(self,titulo):
        return self.libros.get(titulo,(None,0))[1]>0
    
    def sugerir_libro(self,usuario):
        leidos = self.historial_usuarios.get(usuario, set())
        no_leidos = [titulo for titulo in self.libros if titulo not in leidos and self.libros[titulo][1]>0]
        return random.choice(no_leidos)if no_leidos else None 
    
    def libros_populares(self):
        count = {}
        for libros in self.historial_usuarios.values():
             for libro in libros:
                 if libro in count:
                     count_libro += 1
                 else:
                     count_libro = 1 
                     return sorted(count.items(), key=lambda x: x[1], reverse = True) [:5]
    
    def recomendar_libro_colaborativo(self,usuario):
        usuario_actual_libros = self.historial_usuarios.get(usuario, set())
        similitudes = {}

        for otro_usuario, libros in self.historial_usuarios.items():
            if otro_usuario != usuario:
                similitud = len(usuario_actual_libros & libros)
                similitudes[otro_usuario] = similitud

                if not similitudes:
                    return None 
                usuario_mas_similar = max(similitudes, key=similitudes.get)

                posibles_sugerencias = self.historial_usuarios[usuario_mas_similar] - usuario_actual_libros
                return random.choice (list(posibles_sugerencias)) if posibles_sugerencias else None 
            
            
            


            

