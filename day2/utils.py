def read_file_lines(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()
    
def organize(all_games):
    games = []
    for game in all_games:
        current = game.split(':')[1].lstrip().split(';')
        games.append(current)

    organized_games = []
    for game in games:
        draws_by_color = {'red': 0, 'green': 0, 'blue': 0}
        for draws in game:
            for draw in draws.lstrip().split(', '):
                n, color = draw.split(' ')
                if draws_by_color[color] < int(n):
                    draws_by_color[color] = int(n)
        organized_games.append(draws_by_color)
    return organized_games
            