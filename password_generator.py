import requests
import random
def password_generator():
    a = (random.randint(0,10000))# 10k words in the word list
    b =  (random.randint(0,23))
    c = (random.randint(0,9))
    d = (random.randint(0,10000))# 10k words in the word list
    e =  (random.randint(0,23)) # specaial charac
    f =  (random.randint(0,23)) # specaial charac
    g = (random.randint(0,10000))
    h = (random.randint(0,10000))# 10k words in the word list
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    special_characters = ['~','`','!','@','#','$','%','^','&','*','()','_','-','+','=','{','[','}',']',':','<','>','.','?']
    numbers = []
    response = requests.get(word_site) # request words 200 is good
    WORDS = response.content.splitlines() # get content from that response
    random_character = (special_characters[b]) # will pick a random character in the position of my list
    numbers.clear() # clear list incase user gen a new passcode
    for i in range(0,3): # gen a random three digit number
        x = (random.randint(0, 9)) # between 1-10
        numbers.append(x) # append to list
    random_numbers = ''.join(map(str, numbers)) # join the list as one entity
    random_word = WORDS[a].decode("utf-8")
    random_word_1 = WORDS[d].decode("utf-8")
    random_character_1 = (special_characters[e])
    random_character_2 = (special_characters[f])
    random_word_2 = WORDS[h].decode("utf-8")
    pass_1 = f"{random_word}{random_character}{random_numbers}{random_character_1}{random_word_1}{random_character_2}{random_word_2}"
    pass_2 = f"{random_word}{random_character}{random_word_1}{random_character_1}{random_character_2}{random_word_2}{random_numbers}"
    pass_3 = f"{random_character}{random_word}{random_word_1}{random_character_1}{random_character_2}{random_word_2}{random_numbers}"
    password_decider = (random.randint(1,4)) # choose a unique order of characters/numbers 
    if password_decider == 1:
        return pass_1
    elif password_decider == 2:
        return pass_2
    elif password_decider == 3:
        return pass_3
password_generator()
