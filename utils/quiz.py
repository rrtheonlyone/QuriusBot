import requests
import simplejson as json

def generate_quiz(text):
    headers = {'content-type': 'text/plain'}
    quiz_json = requests.post('https://gs4ossx7yj.execute-api.us-east-1.amazonaws.com/dev/text', headers = headers, data = json.dumps({"data": "\"" + text + "\""}))
    quiz_json_text = json.loads(quiz_json.text)[0]
    return json.dumps({"question": quiz_json_text[u'QuestionPrompt'], "type": quiz_json_text[u'QuestionType'], "answer": quiz_json_text[u'CorrectAnswer']})    


