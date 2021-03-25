import random

score = 10
true_chars = []

words = ['Tree', 'Python', 'Android', 'True', 'Clock', 'USB']
word = random.choice(words)
word = word.lower()

while True:
    for i in range(len(word)):
        if word[i] in true_chars:
            print(word[i], end='')
        else:
            print('_', end='')
    char = input('\nplease enter a character: ')
    char = char.lower()

    if char in word:
        true_chars.append(char)
    else:
        score -= 1

    print(score)
    
    if len(true_chars) == len(word):
        print('You wins')
        break

    if score == 0:
        print('Game Over')
        break



