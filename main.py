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

for country in data:
    years = sorted(data[country].keys())
    for i in range(len(years)-1):
        year1 = years[i]
        year2 = years[i+1]
        population_change = data[country][year2] - data[country][year1]
        print(f"{country}: {year1} - {year2}: {population_change}")
