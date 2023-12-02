def read_file_lines(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()

def find_first_digit(string):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    lowest_index = len(string) - 1
    lowest_number = None
    for number in numbers:
        if (0 <= string.find(number) < lowest_index):
            lowest_index = string.find(number)
            lowest_number = number
    for i in range(lowest_index):
        if string[i].isdigit():
            return int(string[i])
    if lowest_number == None:
        return find_last_digit(string)
    return numbers.index(lowest_number) + 1

def find_last_digit(str):
    string = str[::-1]
    numbers = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
    lowest_index = len(string) - 1
    lowest_number = None
    for number in numbers:
        if (0 <= string.find(number) < lowest_index):
            lowest_index = string.find(number)
            lowest_number = number
    for i in range(lowest_index):
        if string[i].isdigit():
            return int(string[i])
    if lowest_number == None:
        return find_first_digit(str)
    return numbers.index(lowest_number) + 1



lines = read_file_lines("/Users/alexanderrokosz/dev/advent-of-code-2023/day1/data.txt")

print(sum(int(f"{find_first_digit(item)}{find_last_digit(item)}") for item in lines))