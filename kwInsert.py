# Justice Smith, 5.13.2020
# Find in repo: github.com/jcode94/YearOne/

import random

# Takes in and splits by space the words in a source text
sample = list(input("What is the sample text you would like to manipulate?\n> ").split(' '))

# Last word punctuation check. It also cleans the last word of punctuation to give program control over it.
lastword = list(sample.pop())
trailingPunct = []
if not lastword[-1].isalpha():
    trailingPunct.append(lastword[-1])
    del lastword[-1]
    sample.append(''.join(lastword))
else:
    sample.append(''.join(lastword))

insert = input("What word would you like to insert?\n> ")

# ValueError check in case someone puts a non-numeric frequency.
while True:
    try:
        freq = int(input("How often? (0 for every word, 1 for every other word, 2 for every third word, etc)\n> "))
        break
    except ValueError:
        print('Please enter a number.')


# The case randomizer for the inserted word.
def switch(switchWord):
    letters = list(f'{switchWord}')
    newWord = ''
    # iterated through the letter list and transforms and appends to newWord
    for letter in letters:
        uol = random.randint(0, 1)
        if uol == 0:
            newWord += letter.upper()
        else:
            newWord += letter.lower()

    return newWord


sampleManip = ''

# Exception case just replaces all words, keeping trailing punctuation.
if freq == 0:
    for word in sample:
        if sample.index(word) == len(sample) - 1:  # checks if current iteration is last word in sample
            sampleManip += f'{switch(insert)}{trailingPunct[0]}'
        else:
            sampleManip += f'{switch(insert)} '
else:
    for word in sample:
        if sample.index(word) == len(sample) - 1:
            if (sample.index(word) + freq) % freq == 0:  # Checks for divisibility of freq
                sampleManip += f'{word} {switch(insert)}{trailingPunct[0]}'
            else:
                sampleManip += f'{word}'
        else:
            if (sample.index(word) + freq) % freq == 0:
                sampleManip += f'{word} {switch(insert)} '
            else:
                sampleManip += f'{word} '

print(sampleManip)
