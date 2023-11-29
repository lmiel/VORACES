def get_min_swaps(seats):
    lookup = {id : pos for pos, id in enumerate(seats)}
    switchs = 0
    position = 0
    while position < len(seats):
        if abs(lookup.get(position) - lookup.get(position + 1)) != 1:
            switchs += 1
            #switch
            temp = lookup.get(lookup.get(position + 1))
            lookup[position + 1] = lookup.get(position + 1 if position % 2 else position - 1)
            lookup[position + 1] = temp
        position += 2
    return switchs

print(get_min_swaps([0,2,1,3]))
print(get_min_swaps([3,2,0,1]))