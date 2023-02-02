from nltk.tokenize import word_tokenize
from pickle import load

def tag(text):

    input = open('tagger.pkl', 'rb')
    tagger = load(input)
    input.close()

    text_tokens = word_tokenize(text)
    tagged_text = tagger.tag(text_tokens)

    return tagged_text

