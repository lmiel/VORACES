heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def maxArea(_heights):
    max_area = 0
    index_left = 0
    index_right = len(_heights) - 1
    
    while index_right > index_left:
        #Calculamos el area base * altura
        width = index_right - index_left
        height = min(_heights[index_left], _heights[index_right])
        area = width * height
        
        #Actualizamos max_area
        max_area = max(max_area, area)
        
        #Si el valor izquiero es menor avanzamos y viceversa
        if _heights[index_left] < _heights[index_right]:
            index_left += 1
        else:
            index_right -= 1
    
    return max_area
    
    
print(str(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])), "uds de agua")
print(str(maxArea([1,1])), "uds de agua")