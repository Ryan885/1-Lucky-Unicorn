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

# Main Routine Below
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print("Program Continues")
