filename = "population.txt"
data = {}

with open(filename, 'r') as file:
    for line in file:
        country, year, population = line.strip().split(',')
        year = int(year)
        population = int(population)
        if country not in data:
            data[country] = {year: population}
        else:
            data[country][year] = population
            