import requests
import simplejson as json

def generate_quiz(text):
    headers = {'content-type': 'text/plain'}
    quiz_json = requests.post('https://gs4ossx7yj.execute-api.us-east-1.amazonaws.com/dev/text', headers = headers, data = json.dumps({"data": "\"" + text + "\""}))
    quiz_json_text = json.loads(quiz_json.text)
    for index in range(len(quiz_json_text)):
        quiz_json_text[index] = json.dumps({"question": quiz_json_text[index][u'QuestionPrompt'], "type": quiz_json_text[index][u'QuestionType'], "answer": quiz_json_text[index][u'CorrectAnswer']})
    return quiz_json_text
