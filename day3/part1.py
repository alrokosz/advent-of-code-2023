from utils import read_file_lines, are_nbrs_chars

def find_non_adjacent_sum(lines):
    total = 0
    cur_num = ''
    num_start = None

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            end = len(lines[row]) - 1
            char = lines[row][col]
            
            if char.isdigit():
                cur_num += char
                if num_start == None:
                    num_start = col

            if not char.isdigit() or (col == end):
                if len(cur_num) > 0:
                    if are_nbrs_chars(lines, num_start, col - 1, row):
                        total += int(cur_num)
                        
                num_start = None
                cur_num = ''

    return total





lines = read_file_lines('day3/data.txt')
print(find_non_adjacent_sum(lines))
