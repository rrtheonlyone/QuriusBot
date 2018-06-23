from collections import Counter
import math
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

def extract_keywords(text):
  # First segment into sentences
  sentences = nltk.sent_tokenize(text)
  token_frequencies = [None] * len(sentences)
  idf = {}
  tokens = set()

  for index, sentence in enumerate(sentences):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(sentence)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in stop_words]
    for word in words:
      tokens.add(word)
    token_frequencies[index] = Counter(words)

  for token in tokens:
    idf[token] = math.log(len(sentences) / len([index for index, sentence in enumerate(sentences) if token_frequencies[index][token] > 0]))

  ranked_words = sorted(list(tokens), key=idf.__getitem__)[:5]
  return ranked_words
