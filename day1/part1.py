from .. import utils

def read_file_lines(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()

def find_first_and_last_digit(string):
    digits = ''
    for char in string:
        if char.isdigit():
            digits += char
            break
    for char in reversed(string):
        if char.isdigit():
            digits += char
            break
    return int(digits)


lines = read_file_lines("/Users/alexanderrokosz/dev/advent-of-code-2023/day1/data.txt")

print(sum(find_first_and_last_digit(item) for item in lines))