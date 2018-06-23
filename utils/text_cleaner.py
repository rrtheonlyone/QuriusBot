import requests as Requests
from newspaper import Article
from bs4 import BeautifulSoup

def get_article_from_url(article_url) :
  # Returns a `newspaper` Article object from article URL
  article = Article(article_url, keep_article_html=True)
  article.download()
  article.parse()
  attach_links(article)
  return article

def get_article_from_html(article_html) :
  # Returns a `newspaper` Article object from article HTML
  article = Article('', keep_article_html=True)
  article.set_html(article_html)
  article.parse()
  attach_links(article)
  return article

def attach_links(article) :
  # Attaches array of links embedded in article
  article.links = list(map(lambda a: a.get('href'), BeautifulSoup(article.article_html, 'html.parser').find_all('a')))
