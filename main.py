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
            for j in range(2): 
                all_boxes.append(box)
                box = box.base_rotate()
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
        if (base == None) or (box < base):
            base = box
            tower.append(box)
            height += box.get_height()
    return height, tower

def naive_recursion(boxes, top_box, height):
    #top_box représente la boite en haut de la pile
    heights = []
    start = top_box if top_box != None else 0
    for i in range(start, len(boxes)):
        if top_box == None or boxes[i] < boxes[top_box]:
            h = boxes[i].get_height()
            heights.append(naive_recursion(boxes, i, height + h))
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
    top_box = 0 if top_box == None else top_box + 1
    if saved_heights[top_box] != -1:
        return saved_heights[top_box]

    last = True
    for i in range(top_box, len(boxes)):
        if top_box == 0 or boxes[i] < boxes[top_box - 1]:
            h = 0 if top_box == 0 else boxes[top_box - 1].get_height()
            added_height= top_down(boxes, saved_heights, i, height + h)
            saved_heights[top_box] = max(saved_heights[top_box], h + added_height) 
            last = False

    if last:
        saved_heights[top_box] = boxes[top_box - 1].get_height()
    return saved_heights[top_box]

boxes = read_box_file("boxes.txt")
#boxes = [] # La réponse devrait être 121
#boxes.append(Box([10, 20, 30]))
#boxes.append(Box([5, 10, 50]))
#boxes.append(Box([100, 20, 1]))
all_boxes = generate_all_boxes(boxes)
sorted_boxes = sort_boxes(all_boxes)
saved_heights = [-1] * (len(sorted_boxes) + 1)
print(top_down(deepcopy(sorted_boxes), saved_heights, None, 0))
print(bottom_up(deepcopy(sorted_boxes)))
print(greedy_method(deepcopy(sorted_boxes)))

boxes1 = [] # La réponse devrait être 121
boxes1.append(Box([10, 20, 30]))
boxes1.append(Box([5, 10, 50]))
boxes1.append(Box([100, 20, 1]))

all_boxes1 = generate_all_boxes(boxes1)
sorted_boxes1 = sort_boxes(all_boxes1)
saved_heights1 = [-1] * (len(sorted_boxes) + 1)
print(top_down(deepcopy(sorted_boxes1), saved_heights1, None, 0))
print(bottom_up(deepcopy(sorted_boxes1)))
print(greedy_method(deepcopy(sorted_boxes1)))
print(naive_recursion(deepcopy(sorted_boxes1), None, 0))
