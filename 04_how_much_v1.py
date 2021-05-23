# Functions


# Main Routine Below Here

error ="Please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # ask the question
        response = int(input("How much money do you want to play for? "))

        # if the amount is too low / too high give
        if response < 0 or response <= 10:
            print("You have asked to play with ${}".format(response))
        else:
            print(error)

    except ValueError:
        print(error)
