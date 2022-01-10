# import part of speech labeling library
import nltk
from nltk import word_tokenize

# change words into tokens
tokens = word_tokenize("When I'm feeling anxious, I overthink and lose my appetite.")

# expand contraction "I'm" to "I am" 
# u can use the library "contractions" to do this, but I'd rather not today
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
entity_labels = ["0", "0", "0", "B-EMOTION", "B-ILLNESS", "0", "B-BEHAVIOR", "0", "B-SYMPTOM", "I-SYMPTOM", "I-SYMPTOM"]

training_data_coNLL = ""

# copied this for loop from https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb
for token, pos, label in zip(tokens, pos_labels, entity_labels):
    # using the coNLL format mentioned earlier (:
    training_data_coNLL += "{} {} {} {} \n".format(token, pos, pos, label)

print(training_data_coNLL)








