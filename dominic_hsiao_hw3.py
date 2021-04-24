def main():
    check_year()
    return


def check_year():

    a = input("Please type a year ")

    b = 69

    a = int(a)
    #print(a)
    if (a % 4 == 0):
        if (a % 100 == 0):
            if (a % 400 == 0):
                b = 1

            else:
                b = 0

        else:
            b = 1

    else:
        b = 0

    if (b == 1):
        print(str(a) + " is a leap year")
    else:
        print(str(a) + " is not a leap year")


if __name__ == "__main__":
    main()
