import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download()

df = pd.read_csv('expected-answers.csv')

#print(df.to_string() )

for i in range( df.last_valid_index() ):
    question = df.iloc[i,1]
    words = word_tokenize(question)
    stop_words = set(stopwords.words("english"))
    #print(question)
    word_tokens = word_tokenize(question)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    #print(word_tokens)
    #print(filtered_sentence)
    print(" ".join(filtered_sentence))