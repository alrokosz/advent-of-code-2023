from utils import organize, read_file_lines

games = read_file_lines('day2/data.txt')
colors_by_game = organize(games)
print(sum(game['red'] * game['blue'] * game['green'] for game in colors_by_game))