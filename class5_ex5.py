def main():
    name = input("Enter your name: ")

    error = True
    while error:
        try:
            index = int(input("Enter an integer index: "))
            print("The {}th character of {} is '{}'".format(index, name, name[index]))
            error = False
        except ValueError:
            print("NO!!!!!! That's not an integer!!!!!")
        except IndexError:
            print("NO!!!!!! Out of Range!!!!!")

    print("End of program.")


if __name__ == "__main__":
    main()
