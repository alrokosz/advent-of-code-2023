from utils import read_file_lines, are_nbrs_nums

# find all stars with adjacent numbers
def find_gear_ratio_sum(lines):
    total = 0

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            end = len(lines[row]) - 1
            char = lines[row][col]
            
            if char == '*':
                nbrs = are_nbrs_nums(lines, col, row)
                if len(nbrs) == 2:
                    total += int(nbrs[0]) * int(nbrs[1])

    return total
                

# find adjacent numbers

# squre numbers and add to total
lines = read_file_lines('day3/data.txt')
print(find_gear_ratio_sum(lines))
# return total