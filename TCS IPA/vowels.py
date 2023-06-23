
def count_digits(m):
    c = 0
    for i in m:
        if i.isdigit():
            c += 1
    return c

def remove_vowels(s):
    l = list(s)
    l1 = ['a','e','i','o','u','A','E','I','O','U']
    for i in l:
        if i in l1:
            l.remove(i)
        else:
            continue
    s = ''.join([str(i) for i in l])
    return s

s = input()
m = remove_vowels(s)
d = count_digits(m)

print("Modified String is:", remove_vowels(s), "& no. of digits are:", d)
