import numpy as np

text = open("C:/Users/Влад/Desktop/Муму.txt").read()

words = text.split()

def word_pairings(words):
    for i in range(len(words) - 1):
        yield(words[i], words[i+1])

pairs = word_pairings(words)

dictionary= {}

for word_1, word_2 in pairs:
    if word_1 in dictionary.keys():
        dictionary[word_1].append(word_2)
    else:
        dictionary[word_1] = [word_2]

first_word = np.random.choice(words)

while first_word.islower():
    first_word = np.random.choice(words)

chain = [first_word]
n_words = 1000 #количество генерируемых слов
for i in range(n_words):
    chain.append(np.random.choice(dictionary[chain[-1]]))

print(" ".join(chain))   
      
        