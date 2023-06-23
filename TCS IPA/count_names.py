def count_names(lst):
    c = len(lst)
    print("Total names are:", c)
    pass

print("Enter names: ")
lst = []
m = input()

lst = m.split(",")

count_names(lst)

