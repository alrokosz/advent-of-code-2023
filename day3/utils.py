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



def find_num_nbrs(row, visited, index, r):
    if (index < 0) or (index > len(row) - 1) or (not row[index].isdigit()) or (f'{r}{index}' in visited):
        return ''
    # print(f'{r}{index}')
    visited.add(f'{r}{index}')
    return find_num_nbrs(row, visited, index - 1, r) + row[index] + find_num_nbrs(row, visited, index + 1, r)


def are_nbrs_nums(lines: list, index: int, row: int) -> bool:
    visited = set()
    nbrs = []

    start = index - 1 if index > 0 else 0
    end = index + 2 if index < len(lines[row]) - 1 else index + 1

    if row > 0:
        above = lines[row - 1][start : end]
        for i in range(len(lines[row - 1])):
            if start <= i < end:
                char = lines[row - 1][i]
                if char.isdigit():
                    n = find_num_nbrs(lines[row - 1], visited, i, row - 1)
                    if n != '':
                        nbrs.append(n)

    if row < len(lines) - 1:
        below = lines[row + 1][start : end]
        for i in range(len(lines[row])):
            if start <= i < end:
                char = lines[row + 1][i]
                if char.isdigit():
                    n = find_num_nbrs(lines[row + 1], visited, i, row + 1)
                    if n != '':
                        nbrs.append(n)

    left = '.' if index <= 0 else lines[row][index - 1]
    right = '.' if index >= len(lines[row]) - 1 else lines[row][index + 1]

    if left.isdigit():
        n = find_num_nbrs(lines[row], visited, index - 1, row)
        if n != '':
            nbrs.append(n)
    
    if right.isdigit():
        n = find_num_nbrs(lines[row], visited, index + 1, row)
        if n != '':
            nbrs.append(n)
    
    return nbrs



