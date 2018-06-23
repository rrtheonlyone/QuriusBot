from flask import Flask
from flask_restful import reqparse, Resource, Api
from __future__ import division
import operator
import nltk
import string

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

#api.add_resource(Main, '/')

#if __name__ == '__main__':
extract("Deep neural nets with a large number of parameters are very powerful machine learning\
systems. However, overfitting is a serious problem in such networks. Large networks are also\
slow to use, making it difficult to deal with overfitting by combining the predictions of many\
different large neural nets at test time. Dropout is a technique for addressing this problem.\
The key idea is to randomly drop units (along with their connections) from the neural\
network during training. This prevents units from co-adapting too much. During training,\
dropout samples from an exponential number of different thinned networks. At test time,\
it is easy to approximate the effect of averaging the predictions of all these thinned networks\
by simply using a single unthinned network that has smaller weights. This significantly\
reduces overfitting and gives major improvements over other regularization methods. We\
show that dropout improves the performance of neural networks on supervised learning\
tasks in vision, speech recognition, document classification and computational biology,\
obtaining state-of-the-art results on many benchmark data sets.")
