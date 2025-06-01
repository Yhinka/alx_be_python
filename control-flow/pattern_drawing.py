# pattern_drawing.py

while True:
    size = int(input("Enter the size of the pattern (positive integer): "))
    def draw_square_pattern(size):
        for i in range(size):
            print("* " * size)
    draw_square_pattern(size)
    break