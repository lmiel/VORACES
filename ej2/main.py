def give_candy(kids_hunger):
    #Damos al primer niño los caramelos necesarios
    #para no dar a ninguno un numero negativo de caramelos
    total_candy = (kids_hunger[0] - min(kids_hunger)) + 1
    
    #La hambre y los caramelos que dimos al anterior niño
    prev_kid_hunger = kids_hunger[0]
    prev_kid_candy = total_candy
    
    for kid_hunger in kids_hunger[1:]:
        candy_for_kid = 0
        #Calculamos cuantos caramelos dar en base
        # al anterior y a su hambre
        if kid_hunger > prev_kid_hunger:
            candy_for_kid = prev_kid_candy + 1
        else:
            candy_for_kid = prev_kid_candy - 1
                
        #Actualizamos valores
        total_candy += candy_for_kid
        prev_kid_candy = candy_for_kid
        prev_kid_hunger = kid_hunger
    
    return total_candy

print(str(give_candy([1,0,2])), "caramelos en total")
print(str(give_candy([1,2,2])), "caramelos en total")