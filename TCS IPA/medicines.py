class Medicine:
    def __init__(self, MedicineName, batch, disease, price) -> None:
        self.MedicineName = MedicineName
        self.batch = batch
        self.disease = disease
        self.price = price

class Solution:
    @classmethod
    def getPricebyDisease(cls, list_Med, dis):
        res = []
        for i in list_Med:
            if i.disease.lower() == dis.lower():
                res.append(i.price)
        return res

n = int(input())
list_Med = []

for i in range(n):
    MedicineName = input()
    batch = input()
    disease = input()
    price = int(input())

    list_Med.append(Medicine(MedicineName, batch, disease, price))

dis = input()
ans = Solution.getPricebyDisease(list_Med, dis)

for i in ans:
    print(i)


    