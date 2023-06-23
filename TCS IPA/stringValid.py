n = int(input())
list_str = []


def ValidStr(strLis):
    countValidString = 0
    CountInvalidString = 0
    for str in strLis:
        temp = ""
        for word in str.split():
            temp = temp + word.strip()
            print(temp)
        if temp.isalpha():
            countValidString = countValidString + 1
        else:
            CountInvalidString = CountInvalidString + 1
    return [countValidString, CountInvalidString]


for i in range(n):
    m = input()
    list_str.append(m)

v, iv = ValidStr(list_str)
print("The valid strings are: ", v)
print("The invalid strings are: ", iv)
