import random

NUM_ROWS = 5
NUM_COLUMNS = 5
MIN_STARS = 4
NUM_BOMBS = 2

STAR_EMOJI = "⭐"
BOMB_EMOJI = "💣"

def get_mine_id():
    while True:
        try:
            mine_id = input("Please enter the mine ID: ")
            return mine_id
        except KeyboardInterrupt:
            print("\nYou pressed Ctrl+C. Exiting.")
            exit(0)

def place_stars(mine_field):
    positions = set()
    while len(positions) < MIN_STARS:
        row, col = random.randint(0, NUM_ROWS - 1), random.randint(0, NUM_COLUMNS - 1)
        positions.add((row, col))
        mine_field[(row, col)] = STAR_EMOJI

def place_bombs(mine_field):
    empty_slots = [(row, col) for row in range(NUM_ROWS) for col in range(NUM_COLUMNS) if mine_field[(row, col)] == " "]

    # Bomb placement in all remaining empty slots
    for row, col in empty_slots:
        mine_field[(row, col)] = BOMB_EMOJI

def generate_random_stars_and_bombs():
    mine_field = {}
    for row in range(NUM_ROWS):
        for col in range(NUM_COLUMNS):
            mine_field[(row, col)] = " "  # Initialize the mine field with empty spaces

    # Place stars on the mine field
    place_stars(mine_field)

    # Place bombs on the mine field
    place_bombs(mine_field)

    return mine_field

def main():
    mine_id = get_mine_id()
    print(f"Mine ID: {mine_id}\n")

    mine_field = generate_random_stars_and_bombs()

    # the width of each cell determined on the length of the emojis
    cell_width = max(len(STAR_EMOJI), len(BOMB_EMOJI)) + 2  # Add 2 for padding

    # Display the mine field
    for row in range(NUM_ROWS):
        for col in range(NUM_COLUMNS):
            content = mine_field[(row, col)].center(cell_width)
            print(content, end="")
            if col < NUM_COLUMNS - 1:
                print("|", end="")  # Add a vertical line between columns
        print()
        if row < NUM_ROWS - 1:
            print("-" * (cell_width * NUM_COLUMNS + (NUM_COLUMNS - 1)))  # Add a horizontal line between rows

if __name__ == "__main__":
    main()

    # keep the window open
    input("Press Enter to exit...")
