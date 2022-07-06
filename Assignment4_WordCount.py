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
text = read_text_file("data/text.txt")


words = split_text(text) #the split text is saved as this array of words
words = remove_stop_words(words,stop_words)


words = lemmatize_words(words)
