from collections import Counter
import requests
import math
import nltk
import utils.secrets as secrets
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

def extract_keywords(text):
  # Returns array of 5 top words
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

def get_links_with_words(keywords):
  # Returns array of URLs
  headers={"Ocp-Apim-Subscription-Key":secrets.ocp_key}
  search_query = " ".join(keywords)
  response = requests.get('https://api.cognitive.microsoft.com/bing/v7.0/search?q='+search_query+'&count=5',headers=headers)
  return [result['url'] for result in response.json()['webPages']['value']]

def get_links_for_article(article):
  return get_links_with_words(extract_keywords(article))
