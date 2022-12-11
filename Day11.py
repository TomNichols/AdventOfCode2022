import operator as opr

filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day11\input.txt"
test = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day11\test_input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

class Game:
    def __init__(self, round, file):
        self.round = round
        self.monkeys = self.get_monkeys(file)
        self.modulus = self.get_modulus()

    def next_round(self):
        self.round += 1

    def pass_object(self, id_from, id_to):
        moved_item = self.monkeys[id_from].items[0]
        self.monkeys[id_from].items.pop(0)
        self.monkeys[id_to].items.append(moved_item)

    def play_round(self):
        for monkey in self.monkeys:
            monkey.inspect_items(self)
        self.next_round()

    def get_modulus(self):
        modulus = 1
        for monkey in self.monkeys:
            modulus *= monkey.divisor
        return modulus

    def get_monkeys(self, file):
        monkeys = []
        for line in read_input(file):
            if "Monkey" in line:
                id = int(line.split(" ")[1].split(":")[0])
            elif "Starting items:" in line:
                items = list(map(int, line.split("Starting items: ")[1].split(", ")))
            elif "Operation: " in line:
                if len(line.split("old")) > 2:
                    operator = "**"
                    increase = 2
                elif "+" in line:
                    operator = "+"
                    increase = int(line.split(" ")[len(line.split(" "))-1])
                else:
                    operator = "*"
                    increase = int(line.split(" ")[len(line.split(" "))-1])
            elif "Test: " in line:
                divisor = int(line.split(" ")[len(line.split(" "))-1])
            elif "If true: " in line:
                if_true = int(line.split(" ")[len(line.split(" "))-1])
            elif "If false: " in line:
                if_false = int(line.split(" ")[len(line.split(" "))-1])
                monkey = Monkey(id, items, operator, increase, divisor, if_true, if_false, 0)
                monkeys += [monkey]
        return monkeys
            
class Monkey:
    def __init__(self, id, items, operator, increase, divisor, if_true, if_false, inspect_count):
        self.id = id
        self.items = items
        self.operator = operator
        self.increase = increase
        self.divisor = divisor
        self.if_true = if_true
        self.if_false = if_false
        self.inspect_count = inspect_count

    def increase_worry(self, worry):
        ops = {
            "+": opr.add,
            "*": opr.mul,
            "**": opr.pow
        } 
        op_func = ops[self.operator]
        return op_func(worry, self.increase)
    
    def decrease_worry(self, worry):
        return worry // 3

    def test_item(self, worry):
        if worry % self.divisor == 0:
            return True
        else:
            return False
    
    def inc_inspect_count(self):
        self.inspect_count += 1

    def inspect_items(self, game):
        items_length = len(self.items)
        for idx in range(items_length):
            item = self.items[0] % game.modulus
            item = self.increase_worry(item)
            #item = self.decrease_worry(item) # NOTE: Uncomment for part 1
            self.items[0] = item
            if self.test_item(item):
                game.pass_object(self.id, self.if_true)
            else:
                game.pass_object(self.id, self.if_false)
            self.inc_inspect_count()

# Play the game
game = Game(0, filename)
while game.round < 10000: # NOTE: Change to 20 for part 1
    game.play_round()

# Collect the inspection counts
counts = []
for monkey in game.monkeys:
    count = monkey.inspect_count
    counts += [count]
sorted_list = sorted(counts)[::-1]
print(sorted_list[0] * sorted_list[1])