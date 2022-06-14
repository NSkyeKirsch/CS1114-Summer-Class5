def main():

    in_file = open("grades.txt", "r")

    total = 0
    counter = 0

    num_lines = int(in_file.readline())  # reads num of subsequent lines in the file

    for line_num in range(num_lines):
        line = in_file.readline().strip()
        print("\t" if counter > 0 else "", line, end=" ")
        total += int(line)
        counter += 1
    print()
    print("There were", counter, "values read.")
    print("Average is: {:<6.2f}".format(total/counter))

    in_file.close()


if __name__ == "__main__":
    main()