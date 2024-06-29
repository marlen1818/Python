name = None

def get_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    global name
    name = first_name + " " + last_name

    return {"first": first_name, "last": last_name}

user = get_name()
print("User first name is ", user['first'])
print("User last name is ", user['last'])
print(user['first'], user['last'])
print(name)




print()
