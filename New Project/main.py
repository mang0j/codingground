import random

def get_wordlist(filename):
    """ Function to return each line from a file as a list 
        of strings with linebreaks removed
    """
    wordlist = []
    with open(filename) as file_object:
        for line in file_object:
            wordlist.append(line.replace("\n", ""))
    return wordlist
    
easy_words = get_wordlist("easy")
hard_words = get_wordlist("hard")

print(easy_words)
#print(hard_words)

random.shuffle(easy_words)
print(easy_words)