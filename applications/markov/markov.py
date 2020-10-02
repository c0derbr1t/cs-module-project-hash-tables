import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

word_list = words.split()
# TODO: analyze which words can follow other words
# Your code here
cache = {}

for i in range(len(word_list) - 1):
    if word_list[i] in cache:
        cache[word_list[i]].append(word_list[i + 1])
    else:
        cache[word_list[i]] = [word_list[i + 1]]

# print(cache)
    

# TODO: construct 5 random sentences
# Your code here
start_valid = False

while not start_valid:
    random_word = random.choice(word_list)
    if random_word.isupper or random_word[0] == '"':
        start = random_word
        start_valid = True


stop_valid = False
sentence = [start]

while not stop_valid:
    random_word = random.choice(word_list)
    stop_list = [',', '!', '?', '"']
    sentence.append(random_word)
    if random_word[-1] in stop_list:
        stop_valid = True

new = " ".join(sentence)
print(new)
