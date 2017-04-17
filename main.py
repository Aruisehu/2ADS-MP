from box import *

def read_box_file(path):
    box_file = open(path, 'r')
    boxes = []
    for line in box_file:
        #Lis la ligne et créer une liste avec les valeurs la composant
        dimensions = list(map(lambda x: int(x), line.split(" ")))
        boxes.append(Box(dimensions))
    return boxes

def get_key(box):
    return box.volume()
        
def sort_boxes(boxes):
    result = sorted(boxes, key = get_key, reverse=True)
    return result

def global_min_surface(boxes):
    #Retourne la surface minimum de toutes les boites données
    return min(list(map(lambda box: box.min_surface(), boxes)))

def naive_recursion(boxes, top_box, height, min_surface):
    #top_surface représente la surface de la boite du haut de la pile
    if top_box != None:
        if (top_box.surface() == min_surface):
            return height
    surfaces = []
    for box in boxes:
        for i in range(3):
            if top_box == None or box < top_box:
                h = box.get_height()
                surfaces.append(naive_recursion(boxes, box, height + h, min_surface))
            box.rotate()
    return max(surfaces) if len(surfaces) != 0 else height


#boxes = read_box_file("boxes.txt")
boxes = []
boxes.append(Box([10, 20, 30]))
boxes.append(Box([5, 10, 50]))
boxes.append(Box([100, 20, 1]))
sorted_boxes = sort_boxes(boxes)
print(sorted_boxes)
print(naive_recursion(boxes, None, 0, global_min_surface(boxes)))



