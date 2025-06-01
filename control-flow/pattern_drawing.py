# pattern_drawing.py

size = int(input("Enter the size of the pattern: "))
def draw_square_pattern(size):
    for i in range(size):
        print("* " * size)
draw_square_pattern(size)