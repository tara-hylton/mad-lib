#mad-lib

def is_not_word(wrong):
    return isinstance(wrong, str) and wrong.isnumeric()

while True:
    answer = input(f'Would you like to do a Mad-lib? y/n\n').lower()
    if answer in "y":
        print("Please fill in the following requests:")
        number1 = input("Please pick a number\n")
        while number1.isalpha():
            number1 = input("Please pick a number\n")
        person1 = input("Please pick a celebrity\n")
        while is_not_word(person1):
            person1 = input("Please pick a celebrity\n")
        place1 = input("Please pick a vacation spot\n")
        while is_not_word(place1):
            place1 = input("Please pick a vacation spot\n")
        adjective1 = input("Please pick an adjective\n")
        while is_not_word(adjective1):
            adjective1 = input("Please pick an adjective\n")
        verb1 = input("Please pick a verb\n")
        while is_not_word(verb1):
            verb1 = input("Please pick a verb\n")
        noun1 = input("Please pick a noun\n")
        while is_not_word(noun1):
            noun1 = input("Please pick a noun\n")
        noun4 = noun1 + 's'
        noun2 = input("Please pick a noun\n")
        while is_not_word(noun2):
            noun2 = input("Please pick a noun\n")
        adverb1 = input("Please pick an adverb\n")
        while is_not_word(adverb1):
            adverb1 = input("Please pick an adverb\n")
        adverb2 = adverb1.capitalize()     #capitalize word
        animal1 = input("Please pick an animal\n")
        while is_not_word(animal1):
            animal1 = input("Please pick an animal\n")
        noun3 = input("Please pick a noun\n")
        while is_not_word(noun3):
            noun3 = input("Please pick a noun\n")
        adjective2 = input("Please pick an adjective\n")
        while is_not_word(adjective2):
            adjective2 = input("Please pick an adjective\n")
        verb2 = input("Please pick a verb\n")
        while is_not_word(verb2):
            verb2 = input("Please pick a verb\n")
        #Story
        print(f'When I was {number1} years old, {person1} and I went to {place1} on a vacation.\nIt was very {adjective1} which caused us to {verb1}.\nWe both ended up with {noun4}. :(\n{adverb2} before we left, a baby {animal1} was found under the {noun2} and we had to chase it away.\nAfterwards, we went to the {noun3}. It was a {adjective2} trip and we wished we could {verb2} forever!')
    elif answer in "n":
        print("Thank you for playing")
        break
    else:
        print("I didn't understand your answer, try again")
