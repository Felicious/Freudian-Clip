# import part of speech labeling library
import nltk
from nltk import word_tokenize

# packages for lib
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = ""
with open("input.txt", "r") as f:
    sentence = f.read()

# change words into tokens
tokens = word_tokenize(sentence)

# expand contraction "I'm" to "I am" 
# u can use the library "contractions" to do this, but I'd rather not today
for word in tokens:
    if word == "\'m":
        im = tokens.index("\'m")
        tokens[im] = "am"

# remove punctuation
# there is prob a lib for this but im too lazy to find it
punctuation = [",", "."]

for item in tokens:
    if item in punctuation:
        tokens.remove(item)

# done pre-processing!

# label parts of speech for each word using lib
pos_labels = []
for word, pos in nltk.pos_tag(tokens):
    pos_labels.append(pos)

# create entity labels!
entity_labels = []
with open("entities.txt", "r") as g:
    for line in g:
        # reading word 
        for label in line.split():
            entity_labels.append(label)

training_data_coNLL = ""

# copied this for loop from https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb
for token, pos, label in zip(tokens, pos_labels, entity_labels):
    # using the coNLL format mentioned earlier (:
    training_data_coNLL += "{} {} {} {} \n".format(token, pos, pos, label)

print(training_data_coNLL)

f.close()
g.close()