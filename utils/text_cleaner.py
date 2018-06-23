import requests as Requests
import secrets
from bs4 import BeautifulSoup

def get_article(article_url) :
    # Returns the main content of the article as an object of html strings
    headers = {'x-api-key':secrets.mercury_api_key, 'Content-Type':'application/json'}
    response = Requests.get('https://mercury.postlight.com/parser?url='+article_url, headers=headers)
    return response.json()

def get_clean_text(html_text) :
    # Returns cleaned text from html string
    return BeautifulSoup(html_text, 'html.parser').get_text()

def get_embedded_links(html_text) :
    # Returns array of links embedded in article
    return map(lambda a: a.get('href'), BeautifulSoup(html_text, 'html.parser').find_all('a'))

def get_cleaned_article(article_url) :
    # Returns cleaned article
    uncleaned_article = get_article(article_url)
    return {
        **uncleaned_article,
        'content': get_clean_text(uncleaned_article['content']),
        'embedded_links': get_embedded_links(uncleaned_article['content']),
    }
