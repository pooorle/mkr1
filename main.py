filename = "population.txt"
data = {}

with open(filename, 'r') as file:
    for line in file:
        country, year_str, population_str = line.strip().split(',')
        year = int(year_str)
        population = int(population_str)
        if country not in data:
            data[country] = {year: population}
        else:
            data[country][year] = population
