# pattern_drawing.py

def draw_square_pattern(size):
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after completing a row
        row += 1

def main():
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

if __name__ == "__main__":
    main()