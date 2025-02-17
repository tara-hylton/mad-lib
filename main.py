#mad-lib

print("Hi! Let's play a Mad Lib!\nPlease enter the requested words below to create a story.")


number1 = input("Please pick a number\n")
person1 = input("Please pick a person or relative close to you\n")
place1 = input("Please pick a place\n")
adjective1 = input("Please pick an adjective\n")
verb1 = input("Please pick a verb\n")
noun1 = input("Please pick a noun\n")
noun2 = input("Please pick a noun\n")
adverb1 = input("Please pick an adverb\n")
adverb2 = adverb1.capitalize()     #capitalize word
animal1 = input("Please pick an animal\n")
noun3 = input("Please pick a noun\n")
place2 = input("Please pick a place\n")
verb2 = input("Please pick a verb\n")  #add ed to verb
verb3 = verb2 + 'ed'


#Story
print(f'When I was {number1} years old, my {person1} and I went to {place1} on a vacation. It was {adjective1} and we {verb1} to bring {noun1}. We both ended up with {noun2}. {adverb2} before we left, a baby {animal1} was found under the {noun3} and we had to chase it away so we could go to {place2}. It was a great trip and we wished we could have {verb3} forever!')

