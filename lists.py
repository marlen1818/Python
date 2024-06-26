#cities = ['New York', 'Los Angeles', 'Jalal-Abad']
#print(cities[1:])

#cities.insert(1,"Bishkek")
#print(cities)
#input = "Where are you from"
#cities = ['New York', 'Los Angeles', 'Jalal-Abad']

cities = []

while len(cities) <= 5:
    usr_input = input('Please enter city name: ')
    print('City already exist', usr_input)
    break
else:
    cities.appent(usr_input)
    print(len(cities), cities)
