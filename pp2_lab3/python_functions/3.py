def solve(numheads,numlegs):
    # c+r=numheads
    # 2c+4r=numlegs
    
    chickens=(4*numheads-numlegs)/2
    rabbits=numheads-chickens
    if chickens>0 and rabbits>0 and chickens.is_integer() and rabbits.is_integer():
        return int(chickens),int(rabbits)
    else:
        return None
print(solve(35,94))