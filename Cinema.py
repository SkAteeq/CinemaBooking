films = {
    "Minions": [3, 5],
    "Dark Knights": [18, 5],
    "Tarzan": [15, 5],
    "Lion King": [12, 5]
    }
while True:
    choice = input("what film do you like to watch ?    :   ").strip().title()
    if choice in films:
        age = int(input("how old are you ?   : ").strip())
        if age >= films[choice][0]:  # "Check user age"

            # "Checking for enough Seats"
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy the film..")
                films[choice][1] = films[choice][1] - 1
            else:
                print("sorry, We are SOLD OUT!!")

        else:
            print("you are too young to watch the film..")
    else:
        print("we don't have that film..")
