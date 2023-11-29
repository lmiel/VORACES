def skips(distances):
    index = 0
    list_length = len(distances)
    
    # Vector one-hot de posiciones visitadas
    visited = [0] * list_length
    
    #Loopear hasta llegar al final o volver a un indice visitado
    while index != list_length - 1:
        
        # Acabamos si nos salimos de la lista o volvemos de nuevo
        # a un indice visitado
        if index > list_length - 1 or visited[index]:
            return False
        #Actualizamos
        visited[index] = 1
        index += distances[index]
    return True

print("Si" if skips([2,3,1,1,4]) else "No", "se puede llegar al final")
print("Si" if skips([3,2,1,0,4]) else "No", "se puede llegar al final")
        