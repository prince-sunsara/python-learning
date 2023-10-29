x = int(input("Enter your number:"))

match x:
    case 0:
        print("x is 0")
    case 143:
        print("x is 143! you got special number..")
    case 1000:
        print("x is 1000")
    case _ if x!=90:
        print(x, "is not equal to 69")
    case _ if x!=420:
        print(x, "is not equal to 420")