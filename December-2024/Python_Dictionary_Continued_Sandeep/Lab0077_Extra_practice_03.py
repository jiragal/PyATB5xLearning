# You can use for Loop to iterate through list of tuples and create dictionary where the country is key
# and values are list of cities belonging to that country
cities = [('India', 'Bangalore'),
          ('India', 'Chennai'),
          ('India', 'Delhi'),
          ('India', 'Kolkata'),
          ('USA', 'Dallas'),
          ('USA', 'New York'),
          ('USA', 'Chicago'),
          ('China', 'Bejing'),
          ('China', 'Shaingai')
          ]

# Initiate an empty dictionary
city_dict = {}

# Iterate through the list of tuples
for country, city in cities:
    if country not in city_dict:
        city_dict[country] = []     #Initiate new empty list for countries
    else:
        city_dict[country].append(city)  #Add the city to the country list

print(city_dict)
