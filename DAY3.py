from random import choice, randrange, shuffle
vegetarian = ['x', '-']
non_vegetarian = ['o', 'x', '-']

def skewer_vegan(vegan, number: int):
    list_vegan= []
    for c in range(number):
        number_skewers = randrange(1, 13)
        skewer = ['-']
        for i in range(number_skewers):
            skewer.append(choice(vegan))
        skewer.append('-')
        skewer = ''.join(skewer)    
        list_vegan.append(skewer)
    return list_vegan

def skewer_non_vegan(ox, number: int):
    list_no_vegan = []
    for c in range(number):
        number_skewers = randrange(1, 13)
        skewer = ['-']
        for i in range(number_skewers):
            skewer.append(choice(ox))
        skewer.append('-')
        skewer = ''.join(skewer)
        list_no_vegan.append(skewer)
    return list_no_vegan   
vegan = skewer_vegan(vegetarian, 2)
non_vegan = skewer_non_vegan(non_vegetarian, 6)

list_skewers = (vegan + non_vegan)
shuffle(list_skewers)
print(list_skewers)


