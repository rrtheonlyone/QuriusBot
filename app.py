from flask import Flask
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

class Main(Resource):
  def get(self):
      return {'hello': 'world'}
  
  def post(self):
      args = parser.parse_args()
      html = args["html"]
      text = get_clean_text(html)
      quiz = generate_quiz(text)
      #links = getrelatedlinks(getKeywords(text), 5)


def get_clean_text(html_text) :
	# Returns cleaned text from html string
    return BeautifulSoup(html_text, 'html.parser').get_text()

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


