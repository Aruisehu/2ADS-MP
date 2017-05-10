from box import *
from copy import deepcopy
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

def generate_all_boxes(boxes):
    all_boxes = []
    for box in boxes:
        for i in range(3):
            all_boxes.append(box)
            box = box.rotate()
    return all_boxes

def sort_boxes(boxes):
    result = sorted(boxes, key = lambda x: x.surface(), reverse = True)
    return result

def greedy_method(boxes):
    # On part du principe simple que la boite avec le plus
    # grand volume est celle qui pourra avoir le plus de boite sur elle
    # Tout en maximisant la hauteur
    base = None # On a pas de boite qui compose la pile au début
    tower = []
    height = 0
    for box in boxes:
        for i in range(2):
            if (base == None) or (box < base):
                base = box
                tower.append(box)
                height += box.get_height()
            box.base_rotate()
    return height

def naive_recursion(boxes, top_box, height):
    #top_box représente la boite en haut de la pile
    heights = []
    start = top_box if top_box != None else 0
    for i in range(start, len(boxes)):
        for j in range(2):
            if top_box == None or boxes[i] < boxes[top_box]:
                h = boxes[i].get_height()
                heights.append(naive_recursion(boxes, i, height + h))
            boxes[i].base_rotate()
    return max(heights) if len(heights) != 0 else height

def bottom_up(boxes):
    track = [0] * len(boxes) # Stock height
    keep = [-1] * len(boxes) # Stock boxes under the box at index i
    boxes.reverse()
    for i in range(len(boxes)):
        track[i] = boxes[i].get_height()
        for j in range(len(boxes)):
            if boxes[j] < boxes[i]:
                if track[j] + boxes[i].get_height() > track[i]:
                    track[i] = track[j] + boxes[i].get_height()
                    keep[i] = j
    max_height = max(track)
    x = track.index(max_height)
    tower = []
    while x != -1:
        tower.append(boxes[x])
        x = keep[x]
    return max_height, tower

def top_down(boxes, saved_heights, top_box, height):
    #top_box représente la boite en haut de la pile
    heights = []
    if top_box != None:
        if saved_heights[top_box] != -1:
            return saved_heights[top_box]

    for i in range(len(boxes)):
        for j in range(2):
            if top_box == None or boxes[i] < boxes[top_box]:
                h = boxes[i].get_height()
                heights.append(top_down(boxes, saved_heights, i, height + h))
            boxes[i].base_rotate()

    if len(heights) != 0 and top_box != None:
        saved_heights[top_box] = max(heights)
        return saved_heights[top_box]
    else:
        if top_box == None:
            return max(saved_heights)
        else:
            saved_heights[top_box] = height
            return height

#boxes = read_box_file("boxes.txt")
boxes = [] # La réponse devrait être 121
boxes.append(Box([10, 20, 30]))
boxes.append(Box([5, 10, 50]))
boxes.append(Box([100, 20, 1]))
all_boxes = generate_all_boxes(boxes)
sorted_boxes = sort_boxes(all_boxes)
print(bottom_up(deepcopy(sorted_boxes))[0])

saved_heights = [-1] * len(sorted_boxes)
print(top_down(deepcopy(sorted_boxes), saved_heights, None, 0))
#print(greedy_method(deepcopy(sorted_boxes)))
#print(naive_recursion(deepcopy(sorted_boxes), None, 0))
