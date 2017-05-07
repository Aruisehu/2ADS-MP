from box import *
"""
    Projet fait par Yohann Jolain et Sébastien Erfani
    Tous les algorithmes demandés parte du principe que la liste de boite est triée
    La boite est trié via la fonction sort_boxes()
"""
def read_box_file(path):
    box_file = open(path, 'r')
    boxes = []
    for line in box_file:
        #Lis la ligne et créer une liste avec les valeurs la composant
        dimensions = list(map(lambda x: int(x), line.split(" ")))
        boxes.append(Box(dimensions))
    box_file.close()
    return boxes

def get_key(box):
    return box.volume()
        
def sort_boxes(boxes):
    result = sorted(boxes, key = get_key, reverse = True)
    return result

def global_min_surface(boxes):
    #Retourne la surface minimum de toutes les boites données
    return min(list(map(lambda box: box.min_surface(), boxes)))

def greedy_method(boxes):
    # On part du principe simple que la boite avec le plus 
    # grand volume est celle qui pourra avoir le plus de boite sur elle
    # Tout en maximisant la hauteur
    base = None # On a pas de boite qui compose la pile au début
    tower = []
    height = 0
    for box in boxes:
        for i in range(2):
            box.set_max_height_state()
            if (base == None) or (box < base):
                base = box
                tower.append(box)
                height += box.get_height()
            box.base_rotate()
    return height, tower

        

def naive_recursion(boxes, top_box, height, min_surface):
    #top_box représente la boite en haut de la pile
    heights = []
    for box in boxes:
        for i in range(3):
            for j in range(2):
                if top_box == None or box < top_box:
                    h = box.get_height()
                    heights.append(naive_recursion(boxes, box, height + h, min_surface))
                box.base_rotate()
            box.rotate()
    return max(heights) if len(heights) != 0 else height


#boxes = read_box_file("boxes.txt")
boxes = []
boxes.append(Box([10, 20, 30]))
boxes.append(Box([5, 10, 50]))
boxes.append(Box([100, 20, 1]))
sorted_boxes = sort_boxes(boxes)
print(naive_recursion(boxes, None, 0, global_min_surface(boxes)))
print(greedy_method(boxes))



