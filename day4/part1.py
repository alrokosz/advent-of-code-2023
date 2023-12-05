from utils import read_file_lines, setup

def find_winning_points(cards):
    total = 0

    for card in cards:
        winning_nums = set(card[0])
        my_nums = card[1]
        matches = 0

        for num in my_nums:
            if num in winning_nums and num != '':
                matches += 1

        if matches > 0:
            total += 2 ** (matches - 1)

    return total


lines = read_file_lines('day4/data.txt')
cards = setup(lines)
print(find_winning_points(cards))



