from box import *

def read_box_file(path):
    box_file = open(path, 'r')
    boxes = []
    for line in box_file:
        #Lis la ligne et créer une liste avec les valeurs la composant
        dimensions = list(map(lambda x: int(x), line.split(" ")))
        boxes.append(Box(dimensions))
    return boxes
        


def global_min_surface(boxes):
    #Retourne la surface minimum de toutes les boites données
    return min(list(map(lambda box: box.min_surface(), boxes)))

#def naive_recursion(boxes):



boxes = read_box_file("boxes.txt")
