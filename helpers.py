# read file contents to string
def read_file_contents(file):
    with open(file, 'r') as f:
        return f.read()
