#unfinished
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))

def read_text_file(file_path):
    return open(file_path, "r").read()

def remove_stop_words(words,stopWords):
    return [i for i in words if not i in stopWords]

def lemmatize_words(words_clean):
    return [WordNetLemmatizer().lemmatize(i) for i in words_clean]

def split_text(text):
    return re.sub(r'[^\w\s]','',re.sub('\d',' ',text)).upper().split() #uses regular expressions to remove numbers and punctuation

def compute_frequency_words(words_lemmatized):
    freqDict = {}
    for i in words_lemmatized:
        if i in freqDict:
            freqDict[i] += 1
        else:
            freqDict[i] = 1

text = read_text_file("data/text.txt")

words = split_text(text)
words = remove_stop_words(words,stop_words)
words = lemmatize_words(words)

frequency = compute_frequency_words(words)
