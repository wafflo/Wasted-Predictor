import random

def get_mine_id():
    while True:
        try:
            mine_id = input("Please enter the mine ID: ")
            return mine_id
        except KeyboardInterrupt:
            print("\nYou pressed Ctrl+C. Exiting.")
            exit(0)

def generate_random_stars_and_bombs():
    num_rows = 5
    num_columns = 5
    mine_field = {}

    for row in range(num_rows):
        for col in range(num_columns):
            mine_field[(row, col)] = " "  # Initialize the mine field with empty spaces

    # Randomly place stars and bombs on the mine field
    num_stars = 3
    num_bombs = 2
    for _ in range(num_stars):
        row, col = random.randint(0, num_rows - 1), random.randint(0, num_columns - 1)
        mine_field[(row, col)] = "⭐"  # Use a star symbol to represent stars

    for _ in range(num_bombs):
        row, col = random.randint(0, num_rows - 1), random.randint(0, num_columns - 1)
        mine_field[(row, col)] = "💣"  # Use a bomb symbol to represent bombs

    return mine_field

def main():
    mine_id = get_mine_id()
    print(f"Mine ID: {mine_id}\n")

    mine_field = generate_random_stars_and_bombs()

    # Display the mine field
    num_rows = 5
    num_columns = 5
    for row in range(num_rows):
        for col in range(num_columns):
            print(mine_field[(row, col)], end=" ")
            if col < num_columns - 1:
                print("|", end="")  # Add a vertical line between columns
        print()
        if row < num_rows - 1:
            print("-" * (num_columns * 2 - 1))  # Add a horizontal line between rows

if __name__ == "__main__":
    main()

    # Add a prompt to keep the window open
    input("Press Enter to exit...")
