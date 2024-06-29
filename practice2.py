def name():
    try:
        name = input("Please enter your name?: ")
        return name
    except:
        return None

    def age():
        try:
            age = int(input("Enter your age?: "))
            return age
        except ValueError:
            print("Not valid info")

    def location():
        try:
            location = int(input("Enter your live Location?: "))
            return location
        except:
            return None

        def hobby():
            try:
                while True:
                    hobby = input("Please write your Hobby?: ")
                    if hobby == None:
                        break
    except:
        print("Wrong info!")
