filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day2\input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines
    
def get_shapes(round):
    shapes = {}
    my_shape = round.split(" ")[1]
    their_shape = round.split(" ")[0]
    if their_shape == "A":
        shapes["them"] = "rock"
    elif their_shape == "B":
        shapes["them"] = "paper"
    elif their_shape == "C":
        shapes["them"] = "scissors"
    if my_shape == "X":
        shapes["me"] = "rock"
    elif my_shape == "Y":
        shapes["me"] = "paper"
    elif my_shape == "Z":
        shapes["me"] = "scissors"
    return shapes

def get_result(shapes):
    if shapes["me"] == shapes["them"]:
        return "draw"
    elif shapes["me"] == "rock" and shapes["them"] == "scissors":
        return "win"
    elif shapes["me"] == "scissors" and shapes["them"] == "paper":
        return "win"
    elif shapes["me"] == "paper" and shapes["them"] == "rock":
        return "win"
    else:
        return "lose"
    
def shape_score(shapes):
    if shapes["me"] == "rock":
        return 1
    if shapes["me"] == "paper":
        return 2
    if shapes["me"] == "scissors":
        return 3
    
def get_score(shapes, result):
    if result == "win":
        return 6 + shape_score(shapes)
    elif result == "draw":
        return 3 + shape_score(shapes)
    elif result == "lose":
        return 0 + shape_score(shapes)
    
def total_score(rounds):
    total = 0
    for round in rounds:
        shapes = get_shapes(round)
        result = get_result(shapes)
        score = get_score(shapes, result)
        total += score
    return total

def get_desired_result(round):
    my_result = round.split(" ")[1]
    if my_result  == "X":
        return "lose"
    elif my_result == "Y":
        return "draw"
    elif my_result == "Z":
        return "win"
    
def get_shape_to_yield_result(their_shape, desired_result):
    if desired_result == "lose":
        if their_shape == "rock":
            return "scissors"
        elif their_shape == "scissors":
            return "paper"
        elif their_shape == "paper":
            return "rock"
    if desired_result == "draw":
        return their_shape
    if desired_result == "win":
        if their_shape == "rock":
            return "paper"
        elif their_shape == "paper":
            return "scissors"
        elif their_shape == "scissors":
            return "rock"
        
def total_score_2(rounds):
    total = 0
    for round in rounds:
        shapes = {}
        their_shape = get_shapes(round)["them"]
        desired_result = get_desired_result(round)
        my_shape = get_shape_to_yield_result(their_shape, desired_result)
        shapes["me"] = my_shape
        score = get_score(shapes, desired_result)
        total += score
    return total


print(total_score(read_input(filename)))
print(total_score_2(read_input(filename)))