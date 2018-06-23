from __future__ import division
from flask import Flask
from flask_restful import reqparse, Resource, Api
from utils.text_cleaner import get_article_from_html, get_article_from_url
from utils.keywords_extractor import extract_keywords

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

class Main(Resource):
  def get(self):
      return {'hello': 'world'}

  def post(self):
      args = parser.parse_args()
      html = args["html"]
      text = get_article_from_html(html).text
      quiz = generate_quiz(text)
      #links = getrelatedlinks(getKeywords(text), 5)

def generate_quiz(text):
    headers = {'content-type': 'text/plain'}
    quiz_json = requests.post('https://gs4ossx7yj.execute-api.us-east-1.amazonaws.com/dev/text', headers = headers, data = json.dumps({"data": "\"" + text + "\""}))
    quiz_json_text = json.loads(quiz_json.text)[0]
    return json.dumps({"question": quiz_json_text[u'QuestionPrompt'], "type": quiz_json_text[u'QuestionType'], "answer": quiz_json_text[u'CorrectAnswer']})

# Call the function by passing in an array of keywords
# and desired number of links, output is an array of related links
def getrelatedlinks(keywords, numoflinks):
    searchkey = ' '.join(keywords)
    links = []
    for url in search(searchkey, stop=numoflinks):
        links.append(url)
    return links

api.add_resource(Main, '/')

if __name__ == '__main__':
	app.run(debug=True)
