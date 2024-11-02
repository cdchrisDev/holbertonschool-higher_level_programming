#!/usr/bin/python3
def write_file(filename="", text=""):
    cnt = 0
    with open(filename, 'w', encoding='utf-8') as f:
        for c in text:
            f.write(c)
            cnt += 1
        return cnt


if __name__ == '__main__':
    nb_characters = write_file("my_first_file.txt",
                               "This School is so cool!\n")
    print(nb_characters)
