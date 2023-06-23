def loveforkanha(l):
    print("\n")
    print(l[0], "is my lover!")
    print(l[1], "is my boyfriend!")
    print(l[2], "is my hubby!")
    print(l[3], "is my sweetheart!")
    print(l[4], "is my baby!")
    print(l[5], "is my darling!")
    print(l[6], "is my life!")
    print(l[7], "is my jaan!")
    print(l[8], "is my everything!")
    print("\n")
    print("& other names are: ")
    i = 9
    while i < len(l):
        print(l[i])
        i += 1


print("Enter the name(s) of your loved one!...\n")

n = input()
l = n.split(",")

loveforkanha(l)


