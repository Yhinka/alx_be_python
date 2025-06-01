# pattern_drawing.py


def draw_square_pattern(size):
    for i in range(size):
        yield "* " * size

while True:
    try:
        size = int(input("Enter the size of the pattern (positive integer): "))
        if size > 0:
            draw_square_pattern(size)
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")