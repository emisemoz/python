# import random
# import string
# print("Welcome to Password Maker!")

# adjectives_list=["sleepy", "slow", "fluffy", "red", "yellow", "green", "blue"]
# nouns_list=["Dinosaur", "Ball", "Dragon", "Hammer", "Apple", "Duck", "Panda"]

# adjective = random.choice(adjectives_list)
# noun = random.choice(nouns_list)    
# number = random.randrange(0, 100)    
# char = random.choice(string.punctuation)

# password = adjective + noun + str(number) + char 
# print("Recommended password:" + password) 

import random
import string
print("Welcome to User Maker!")

adjectives_list=["sleepy", "slow", "fluffy", "red", "yellow", "green", "blue"]
nouns_list=["Dinosaur", "Ball", "Dragon", "Hammer", "Apple", "Duck", "Panda"]

adjective = random.choice(adjectives_list)
noun = random.choice(nouns_list)    
number = random.randrange(0, 100)    
char = random.choice(string.punctuation)
mail= "@mail.com"

user = adjective + noun + str(number) + char + mail
print("Recommended password:" + user) 