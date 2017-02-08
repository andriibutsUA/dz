import os


def print_files(path):
    files = os.scandir(path)
    for i in files:
        if i.is_file():
            if i.name.endswith('.txt'):
                with open(path + i.name, 'r') as f:
                    for line in f:
                        print(line)


print(print_files('files/'))