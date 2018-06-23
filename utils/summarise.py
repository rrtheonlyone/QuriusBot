import requests

url = "https://api.smmry.com"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

def summarise(text):
	payload={"sm_api_input": text}
	querystring = {"SM_API_KEY":"B7D3199143", "SM_URL":text, "SM_WITH_BREAK":'', 'SM_IGNORE_LENGTH':''}
	r = requests.post(url, headers=headers, params=querystring)
	return r.text



