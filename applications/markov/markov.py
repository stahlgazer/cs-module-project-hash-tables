import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# split into words
split_words = words.split()
table = {}

# TODO: analyze which words can follow other words
# Your code here
for i in range(len(split_words)-1):
    word = split_words[i]
    next_word = split_words[i+1]

    if word not in table:
        table[word] = [next_word]
    else:
        table[word].append(next_word)
# print(table)

# Make a list of start words
# Loop over our split_words and put any start word into a list
# OR If first/second character is capitalized, put into list

## you can add a .keys() to your HashTable class
start_words = []
for key in table.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

word = random.choice(start_words)

# TODO: construct 5 random sentences
# Your code here

stopped = False
stop_signs = "?.!"

while not stopped:
    #print the word
    print(word, end=' ')
    # if it's a stop word, stop
    if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
        stopped = True

    # choose a random following word
    following_words = table[word]
    word = random.choice(following_words)

