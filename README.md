#Como ejecutar el programa 

1. Descargar python--verse
2. Abre terminal y encontrar carpeta con los archios necesarios 
3. Ejecuta comanbdo de python 
4. Importa la biblioteca y crear instancia biblio = Biblioteca()
5. Agregar libros de la biblioteca 
   biblio.agregar_libro("Willy Wonka", "Roald Dahl", 7")
6. Presta un libro a un usuario:
   biblio.prestar_libro("usuario1, "2025")
7. Consulta si un libro esta disponible 
   print(biblio.esta_disponible("2025")
8. Devuelve in libro 
   biblio.devolver_libro("2025")
9. Sugerir un libro no leido por el usuario 
   print(biblio.sugerir_libro("usuario1"))
10. Obtener los libros mas populares 
    print(biblio.libros_populares())
11. Obtener recomendaciopn basada en colaborativo
    print(biblio.recomendar_libro_colaborativo())
12. El codigo esta almacenado en memoria por lo tanto si se cierra sesion se pierde todo. 
