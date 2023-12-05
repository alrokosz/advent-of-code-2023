from utils import read_file_lines, setup

def find_winning_points(cards):
    total = 0

    for card in cards:
        winning_nums = set(card[0])
        my_nums = card[1]
        # init to -1 so we can use 2 ** matches, but need to check if it's greater than -1 below
        matches = -1

        for num in my_nums:
            if num in winning_nums and num != '':
                matches += 1

        if matches >= 0:
            total += 2 ** matches

    return total


lines = read_file_lines('day4/data.txt')
cards = setup(lines)
print(find_winning_points(cards))



