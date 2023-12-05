from utils import read_file_lines, setup

def find_winning_points(cards):

    card_counts = [1 for _ in range(len(cards))]

    for card_num in range(len(cards)):
        card = cards[card_num]
        winning_nums = set(card[0])
        my_nums = card[1]
        matches = 0

        for num in my_nums:
            if num in winning_nums and num != '':
                matches += 1

        for i in range(matches):
            card_counts[i + card_num + 1] += card_counts[card_num]

    return sum(card_counts)


lines = read_file_lines('day4/data.txt')
cards = setup(lines)
print(find_winning_points(cards))