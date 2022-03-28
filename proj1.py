user_choice = ""

#These functions contain the text for each story
def madLib1(): 
    first_madlib = f"There once was the {est_adjective_1} {noun_1} ever, that loved {plural_noun_1} so much, since they were so {adjective_1} they cut off their \
{number_1} {body_part_1}(s) and gave them to the {plural_noun_1} and as a reward, they were given the Death Note in {place_1}, essentially {ing_verb_1} humanity"
    print(first_madlib)

def madLib2(): 
    second_madlib = f"A boy and his {number_1} {plural_noun_1} went to {place_1} because they loved {ing_verb_1} a(n) {adjective_1} {noun_1} with a {body_part_1} \
it was the {est_adjective_1} day in {place_1}'s history"
    print(second_madlib)

def madLib3(): 
    third_madlib = f"All of the {adjective_1} {plural_noun_1} in {place_1} are {ing_verb_1} their {body_part_1}s because the {est_adjective_1} {noun_1} in Canada \
is there, they want to see the {noun_1}'s {number_1} {body_part_1}s"
    print(third_madlib)

"""
This body of code asks the user for an input, if the input is 1, 2, or 3 then it runs the corresponding story function and stop asking the user for an input, 
if it's q it will stop asking the user for an input, if it is anything else then it will tell the user it was an invalid input and asks the user again.
"""
while True:
    user_choice = input("What story would you like to choose? Enter story number 1, 2, 3 or q to quit: ")
    if user_choice == "1" or user_choice == "2" or user_choice == "3":
        noun_1 = input("Noun: ")
        adjective_1 = input("Adjective: ")
        plural_noun_1 = input("Plural noun: ")
        body_part_1 = input("Body part: ")
        number_1 = input("Number: ")
        place_1 = input("Place: ")
        ing_verb_1 = input("Verb ending in ing: ")
        est_adjective_1 = input("Adjective ending in est: ")
        if user_choice == "1":
            madLib1()
        elif user_choice == "2":
            madLib2()
        elif user_choice == "3":
            madLib3()
        break
    elif user_choice == "q":
        print("Quiting")
        break
    else:
        print("Invalid input")
        continue
