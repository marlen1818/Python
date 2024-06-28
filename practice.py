my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

if 'john' in my_dict.values():
    print('found')
else:
    print('not found')

    my_dict = {x :x ** 2 for x in range (5)}
    print(my_dict)

    manual_dict = {}
    for x in range(10):
        manual_dict[x] = x ** 3
    print(manual_dict)


names = ['Ahmand', 'Abdul', 'Kris', 'Esen', 'Gulnaz', 'Akmal']
instructors = [x for x in names]
print(instructors)