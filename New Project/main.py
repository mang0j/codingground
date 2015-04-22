import random
import time
import os

# -- Constants --
NSETS = 5
NWORDS = 6
NSECONDS = 5
# ---------------

def clrscr():
    """
    Function to clear the screen (both interactive console and system)
    """
    print("\n" * 80)
    os.system("cls" if os.name == "nt" else "clear")


def get_wordlist(filename):
    """
    Function to return each line from a file as a list 
    of strings with linebreaks removed
    """
    wordlist = []
    with open(filename) as file_object:
        for line in file_object:
            wordlist.append(line.replace("\n", ""))
    return wordlist

    
def create_wordsets(wordlist):
    """
    Function to shuffle a wordlist and return 3 sets of words:
    filler words (an array of 5 wordlists, each containing 4 words),
    target words (a list of 5 words that will be removed from each set) and
    switch words (a list of 5 words that will replace the target words in each set)
    """
    filler_set = []
    target_set = []
    switch_set = []
    random.shuffle(wordlist)
    for index in range(NSETS):
        temp_list = []
        for word in range(NWORDS):
            temp_list.append(wordlist.pop())
        filler_set.append(temp_list)
        target_set.append(filler_set[index].pop())
        switch_set.append(filler_set[index].pop())
    return filler_set, target_set, switch_set


def test_set(filler_set, target_set, switch_set, index):
    """
    Function to combine the filler, target and switch words into one set (at the
    specified index), shuffle and display it for n seconds, then clear the screen,
    replace the target word with the switch word of the next set up (index + 1,
    or 0 if index is equal to the last set), ask the player to enter the target
    word (i.e. the word that was replaced) and return the answer as a string
    """
    display_set = []
    for word in filler_set[index]:
        display_set.append(word)
    display_set.append(target_set[index])
    display_set.append(switch_set[index])
    random.shuffle(display_set)

    clrscr()
    for word in display_set: print(word, end=" ")
    print("\n")
    time.sleep(NSECONDS)

    for word in display_set:
        if word == target_set[index]: 
            display_set.remove(word)
    if index == (NSETS - 1):
        display_set.append(switch_set[0])
    else: 
        display_set.append(switch_set[index + 1])
    random.shuffle(display_set)
    
    clrscr()
    for word in display_set:
        print(word, end=" ")
    print("\n")
    
    return input("Which word was removed? ")

    
def main():
    score = 0
    answer = []
    wordlist = get_wordlist("easy") # implement player choice of difficulty
    filler, target, switch = create_wordsets(wordlist)

    for index in range(NSETS):
        print("Set %d:" % (index + 1))
        input("Press enter when ready to start")
        answer.append(test_set(filler, target, switch, index))
        if answer[index] == target[index]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! %s was removed." % target[index])
        print()

    print("You scored: %d out of %s" % (score, NSETS))
    print("Correct answers:")
    for index in range(NSETS):
        if answer[index] == target[index]:
            print(answer[index])
    print("Incorrect answers:")
    for index in range(NSETS):
        print("answer: %s - target: %s" % (answer[index], target[index]))
        if answer[index] != target[index]: # need to debug!! drops an incorrect answer but struggling to reproduce
            print(answer[index])            

main()
