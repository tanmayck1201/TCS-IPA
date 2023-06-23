str = input()
suffix = "ly"
str = str.split()
print(str)
str1 = ""
for i in str:
    if i.endswith(suffix):
        print(len(str))
        print(i[:-len(str)])
        str1 = str1+" "+i
    else:
        str1 = str1+" "+i
str1 = str1.lstrip()
print(str1)
