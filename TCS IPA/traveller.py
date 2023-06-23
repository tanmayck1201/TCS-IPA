class Traveler:
    def __init__(self, travelerName, traveledCountry, travelerAge, countryFrom) -> None:
        self.travelerName = travelerName
        self.traveledCountry = traveledCountry
        self.travelerAge = travelerAge
        self.countryFrom = countryFrom

n = int(input())
list_obj = []

for i in range(n):
    travelerName = input()
    c = int(input())
    travelList = []
    for j in range(c):
        travelList.append(input())
    travelerAge = int(input())
    countryFrom = input()

    list_obj.append(Traveler(travelerName, travelList, travelerAge, countryFrom))
    