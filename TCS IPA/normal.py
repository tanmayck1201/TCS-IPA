k=[1,2,3]
for i in range(5):
    if i<1:
        print(i)
        continue

    if i < len(k):
        print("NO")
    else:
        print("HII")
    
    print("a:", i)