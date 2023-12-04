def read_file_lines(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()
    
    
def is_character(char):
    return not char.isdigit() and char != '.'


def are_nbrs_chars(lines: list, num_start, num_end, row: int) -> bool:

    start = num_start - 1 if num_start > 0 else 0
    end = num_end + 2 if num_end < len(lines[row]) - 1 else num_end + 1

    if row > 0:
        above = lines[row - 1][start : end]
        for char in above:
            if is_character(char):
                return True

    if row < len(lines) - 1:
        below = lines[row + 1][start : end]
        for char in below:
            if is_character(char):
                return True

    left = '.' if num_start <= 0 else lines[row][num_start - 1]
    right = '.' if num_end >= len(lines[row]) - 1 else lines[row][num_end + 1]

    if is_character(left) or is_character(right):
        return True
    
    return False


    