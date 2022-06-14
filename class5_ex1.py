def main():
    in_file = open("input.txt", 'r')

    """for line in in_file:
        new_list = line.strip().split(". ")

    print(new_list)"""

    for line_str in in_file:
        new_string = line_str[0:15]
        # print(new_string)
        line_str = line_str.strip()
        for char in line_str:
            print("'" + char + "'")

    in_file.close()


if __name__ == "__main__":
    main()
