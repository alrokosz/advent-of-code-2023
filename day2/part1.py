from utils import organize, read_file_lines

def game_possible(game: dict, index: int) -> int:
    red_max = 12
    green_max = 13
    blue_max = 14

    if (game['red'] <= red_max) and (game['green'] <= green_max) and (game['blue'] <= blue_max):
        return index + 1
    return 0


games = read_file_lines('day2/data.txt')
colors_by_game = organize(games)

# red_max = 12
# green_max = 13
# blue_max = 14

# total = 0
# for i in range(len(colors_by_game)):
#     game = colors_by_game[i]
#     if (game['red'] <= red_max) and (game['green'] <= green_max) and (game['blue'] <= blue_max):
#         total += i + 1

print(sum(game_possible(colors_by_game[i], i) for i in range(len(colors_by_game))))