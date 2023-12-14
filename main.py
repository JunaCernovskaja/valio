class Country:
    def __init__(self, name, population, area):
       self.population = population
       self.name = name
       self.population = population
       self.area = area
       self.is_big = self.check_if_big()

    def check_if_big(self):
       return self.population > 20000000 or self.area > 3000000

Australia = Country("Australia", 23545500, 7692824)
print(Australia.is_big)

Lithuania = Country("Lithuania", 2700000, 635000)
print(Lithuania.is_big)
