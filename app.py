from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from flask_cors import CORS, cross_origin

from utils import text_cleaner
from summa import summarizer

app = Flask(__name__)
CORS(app)

api = Api(app)
parser = reqparse.RequestParser()

class Summary(Resource):
  def get(self):
    return {'hello': 'world'}
  
  def post(self):
    parser.add_argument('data')
    args = parser.parse_args()
    html = args["data"]

    raw_data = text_cleaner.get_article_from_html(html).text

    smry = summarizer.summarize(raw_data, words=250)
    return {'data': smry}

api.add_resource(Summary, '/summary')

if __name__ == '__main__':
	app.run(debug=True)


