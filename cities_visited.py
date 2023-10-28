cities_visited = []     ## Start as the empty list

cities_visited.append("Boston")  ## Use append() to add elements

cities_visited.append("Montreal")

cities_visited.append("Toledo")

cities_visited.pop()

cities_visited.append("Toronto")

cities_visited.append("Niagara")

print(cities_visited) ## ['Boston', 'Montreal', 'Toronto', 'Niagara']

for city in cities_visited:
    print(city)
for order, city in enumerate(cities_visited):
    print(order+3,city)
