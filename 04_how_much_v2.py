# Functions
def num_check(question, low, high):
    error ="Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return  response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine Below Here
how_much = num_check("How much would you like to play with?", 0, 10)

# Print the spending
print("You will be spending ${}".format(how_much))

