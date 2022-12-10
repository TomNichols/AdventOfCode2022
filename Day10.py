filename = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day10\input.txt"
test = r"C:\Users\nicholst\Projects\AdventOfCode\2022\Day10\test_input.txt"

def read_input(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

class CRT:
    def __init__(self, cycle, X):
        self.cycle = cycle
        self.X = X
        self.cycle_history = {}
        self.sprite = [0,1,2]
        self.pixels = {}

    def render_pixel(self):
        self.sprite = [self.X-1,self.X,self.X+1]
        if (self.cycle-1) % 40 in self.sprite:
            self.pixels[self.cycle-1] = "#"
        else:
            self.pixels[self.cycle-1] = "."
        
    def next_cycle(self):
        self.render_pixel()
        self.cycle_history[self.cycle] = self.X
        self.cycle += 1
    
    def noop(self):
        self.next_cycle()

    def addx(self, V):
        self.next_cycle()
        self.next_cycle()
        self.X += V

    def signal_strength(self, cycle):
        return self.cycle_history[cycle] * cycle
    
    def render_screen(self):
        pixels_list = list(self.pixels.values())
        for pixel_set in chunker(pixels_list, 40):
            print("".join(pixel_set))

# Solution
crt = CRT(1,1)
for line in read_input(filename):
    if line.split(" ")[0] == "noop":
        crt.noop()
    else:
        crt.addx(int(line.split(" ")[1]))

print(sum([crt.signal_strength(20), 
            crt.signal_strength(60), 
            crt.signal_strength(100), 
            crt.signal_strength(140),
            crt.signal_strength(180),
            crt.signal_strength(220)]))

print(crt.render_screen())