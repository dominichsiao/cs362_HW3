def main():
    check_year()
    return


def check_year():

    #s
    #a = input("Please type a year ")
    #a = int(a)

    #while(a < 0):
        #print("Invalid Year, please try again")
        #a = input("Please type a year ")
        #a = int(a)

    while True:
        try:
            a = int(input("Please type a year "))
        except ValueError:
            print("Sorry not a year") 
            continue
        if(a < 0):
            print("sorry not year")
        else:
            break   
    

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
