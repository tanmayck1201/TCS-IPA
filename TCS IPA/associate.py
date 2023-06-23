class Associate:
    def __init__(self, id, name, technology, expInYears):
        self.id = id
        self.name = name
        self.technology = technology
        self.expInYears = expInYears

class Solution:
    def associatesForGivenTechnology(list_obj, searchTech):
        res = []
        for i in list_obj:
            if i.technology.lower() == searchTech.lower():
                if (i.expInYears % 5) == 0:
                    res.append(i)
        return res

n = int(input())
list_obj = []

for i in range(n):
    id = int(input())
    name = input()
    technology = input()
    expInYears= int(input())

    list_obj.append(Associate(id, name, technology, expInYears))     

searchTech = input()
r = Solution.associatesForGivenTechnology(list_obj, searchTech)

for i in r:
    print(i.id)
