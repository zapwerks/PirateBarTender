#Globals

import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

#Define the functions


def find_preference():
    """This function asks the customer for their drink preferences"""
    preferences = {} 
    for taste, question in questions.items():
        print(question)
        preferences[taste] = input() in ["y", "yes"]
    return preferences    
    

def make_drink(preferences):
    """This function takes the output of the Preference Function and passes it
    into the Drinks function. It then uses random to make a random combination 
    for the customer"""
    drink = []
    for key, value in preferences.items():
        if value is True:
            drink.append(random.choice(ingredients[key]))
    return drink


  
def main():
    results = find_preference()
    print("\nGreat! Based on your choices, I recommend a cocktail with a:")
    for drink in make_drink(results):
        print("    " + drink)


if __name__ == "__main__":
    main() 