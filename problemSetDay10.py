# File name: problemSetDay10.py
from random import randint

#This part makes variables I will need
list_of_words = ["apple", "orange", "pear", "mango", "passionfruit", "soursop", "starfruit"]
index = randint(0, len(list_of_words) - 1)
target = list_of_words[index]
word = []
incorrect_guesses = 0
guesses = []

#This sets the original word
for i in range(len(target)):
  word.append("_")

# "".join() creates a string of words. remember that. " ".join() puts spaces between them
#Then we begin to actually make guesses
#use a while loop

print("word:", " ".join(word))
print("guesses so far:", " ".join(guesses))
print("wrong guesses:", str(incorrect_guesses), "out of 10")
print()
guess = input("Guess a letter: ")
while "".join(word) != target and incorrect_guesses < 10:
  #use for loop to go through target word and see if guess is there. first, use if ... else
  if guess in target:
    print("That's in the word!")
    for i in range(len(target)):
      if target[i] == guess:
        word[i] = guess
  else:
    print("That's not in the word.")
    incorrect_guesses += 1

  guesses.append(guess)
  print("word:", " ".join(word))
  print("guesses so far:", " ".join(guesses))
  print("wrong guesses:", str(incorrect_guesses), "out of 10")
  print()
  if incorrect_guesses != 10 and "".join(word) != target:
    guess = input("Guess a letter: ")

#Tells if user won or lost
if "".join(word) == target:
  print("You won! The target word was " + target + "!")
else:
  print("You lost. The target word was " + target + ".")
