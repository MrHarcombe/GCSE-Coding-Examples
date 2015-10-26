from html.parser import HTMLParser
import urllib.request
import random

HANGMANPICS = ["""

   +---+
   |   |
       |
       |
       |
       |
 =========""", """

   +---+
   |   |
   O   |
       |
       |
       |
 =========""", """

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========""", """

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========""", """

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========""", """

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========""", """

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 ========="""]

""" This next part opens a web page that contains a large list of animals
    and carefully strips out only the animal names, which it puts in the
    /animals/ list for us to use as the random word to guess
"""

class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print("Encountered a tag:", tag, "with attributes:", attrs)
        if tag == "a":
            # print(tag, "=>",  attrs)
            if attrs[0][0] == "href" and attrs[0][1].startswith("/animals/"):
                # print(attrs[1][1].lower())
                if not attrs[1][1].startswith("Animals "):
                    animals.append(attrs[1][1].lower())

animals = []
parser = MyHtmlParser()
with urllib.request.urlopen("http://a-z-animals.com/animals/") as url:
    parser.feed(str(url.read(), "UTF-8"))

# print(animals)

def get_random_word(words):
    return words[random.randint(0, len(words))]

def draw_hangman(missed_letters):
    print(HANGMANPICS[len(missed_letters)])

def draw_current_word_state(secret_word, correct_letters, missed_letters):
    # print part-filled secret word
    print("")
    for l in secret_word:
        if l in correct_letters or not l.isalpha():
            print(l, end=" ")
        else:
            print("_", end=" ")

    # print reminder of missed guesses
    print("\nOther guesses: ", end="")
    for l in missed_letters:
        print(l, end=" ")
    print("\n")

def get_guess(correct_letters, missed_letters):
    guess = input("Enter guess: ")
    if guess.isalpha():
        if not guess in correct_letters+missed_letters:
            return guess
        else:
            print("You've already guessed that!")
    else:
        print("Invalid guess; try again!")
    return get_guess(correct_letters, missed_letters)

def has_guessed_secret_word(secret_word, correct_letters):
    has_guessed = True
    for l in secret_word:
        if not (l in correct_letters or not l.isalpha()):
            has_guessed = False
    return has_guessed

print("H A N G M A N")
missed_letters = ""
correct_letters = ""
secret_word = get_random_word(animals)
game_over = False

# print("(I chose a >>", secret_word, "<<)")
while not game_over:
    draw_hangman(missed_letters)
    draw_current_word_state(secret_word, correct_letters, missed_letters)
    guess = get_guess(correct_letters, missed_letters)
    if guess in secret_word:
        correct_letters += guess
    else:
        missed_letters += guess
    game_over = has_guessed_secret_word(secret_word, correct_letters) or \
                len(missed_letters) == len(HANGMANPICS) - 1

draw_hangman(missed_letters)
draw_current_word_state(secret_word, correct_letters, missed_letters)
if has_guessed_secret_word(secret_word, correct_letters):
    print("Yay! Well done, you guessed it!")
else:
    print("Oh hard luck - maybe next time?")
    print("BTW, I had picked \"", secret_word, "\"", sep="")