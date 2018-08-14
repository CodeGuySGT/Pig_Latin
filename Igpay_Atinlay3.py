"""
8/7/2018
Pig Latin simulator that's a little more powerful than the Codecademy instructions
require. I decided to make exceptions for words beginning with consonant
clusters and vowels, since I always did pig latin using the whole consonant
cluster and not just the first letter. 'String' --> 'Tringsay' just doesn't
sound right to me, and neither does 'Apple' --> 'Ppleaay'.
"""

# getting word from user
original = input('Enter a word: ')
word = original.lower()

# function checks if a given letter is a vowel and returns T/F
def isvowel(lett_in):
  vowels = ['a','e','i','o','u']
  yesvowel = False
  for letter in vowels:
    if lett_in == letter:
      yesvowel = True
  return yesvowel

# First it checks if the input is even a word, then runs through exceptions and
# makes the necessary changes
pyg = 'ay'                        #pig latin ending to append to words
if len(word) > 0 and word.isalpha():
  if isvowel(word[0]):            #exception for words beginning
    new_word = word + pyg         # with vowels -- just adds 'ay' to the end
    print(new_word)
  else:                           #starts checking how long the
    cons = 1                      # consonant cluster is. We already know it
    novowels = True               # begins with a consonant. When it hits a
    for i in range(1, len(word)): # vowel, the loop ends and cons has the
      if isvowel(word[i]):        # length of the consonant cluster
        novowels = False
      elif novowels:
        cons += 1

    # arranging all the pieces into a pig latin word and printing
    first = word[0:cons]          #the consonant or cluster to be moved
    new_word = word + first + pyg #word now includes two copies of first
    length = len(new_word)
    new_word = new_word[cons:length] #cuts out the initial consonant cluster
    print(new_word)                  #prints the final product
else:                            #Finally an exception for empty,
  print('not a word')            # numbers, or other characters
