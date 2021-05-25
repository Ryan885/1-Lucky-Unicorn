# Functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response
            # response to yes

        elif response == "no" or response == "n":
            response = "no"
            return response
            # response to no

        else:
            print("Please answer yes / no")
        # neither

def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

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


# Main Routine Below
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print("Program Continues")

print()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with?", 0, 10)

print("You will be spending ${}".format(how_much))
