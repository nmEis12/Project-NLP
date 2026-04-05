import numpy as np

with open(r"D:\DataSet\Prepared DataSet.txt", 'r', encoding='utf-8') as file:
    data  = file.read()

corpus = data.split()

def make_pairs(corpus):

   for i in range(len(corpus) - 1):
       yield (corpus[i], corpus[i + 1])

pairs = make_pairs(corpus)
word_dict = {}
for word_1, word_2 in pairs:
   if word_1 in word_dict.keys():
       word_dict[word_1].append(word_2)
   else:
       word_dict[word_1] = [word_2]
first_word = np.random.choice(corpus)
chain = [first_word]
n_words = int(input("INPUT WORD COUNT"))
for i in range(n_words):
   chain.append(np.random.choice(word_dict[chain[-1]]))
print(' '.join(chain))
