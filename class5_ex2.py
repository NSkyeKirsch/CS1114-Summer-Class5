def main():
    out_file = open('output_file.txt', 'a')  # append: adds to a file instead of overwriting it
    print("Hello NYU.", file=out_file)
    print("This is CS-1114 and CS-410X", file=out_file)
    print("This part is not printed to the file.")
    out_file.close()


if __name__ == "__main__":
    main()
