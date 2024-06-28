my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict["country"] = "USA"
print(my_dict["age"])
print(my_dict)

my_dict["age"] = "30"
print(my_dict)

for item in my_dict:
    print(item)

    for key, value in my_dict.items():
        print("key: ", key, "value: ", "value ")
    del my_dict['age']
    print(my_dict)