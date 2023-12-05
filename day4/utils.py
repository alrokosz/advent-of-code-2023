def read_file_lines(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()
    
def setup(lines):
    return [[line[0].rstrip().split(' '), line[1].lstrip().split(' ')] for line in [line.split('|') for line in [line.split(':')[1].lstrip() for line in lines]]]

