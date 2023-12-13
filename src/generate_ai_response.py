import requests

API_URL = "https://api-inference.huggingface.co/models/RUCAIBox/mvp-open-dialog"
headers = {"Authorization" : "Bearer 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"}

def query(payload) :
    response = requests.post(API_URL , headers=headers , json=payload)
    result = response.json()

    if isinstance(result , list) and len(result) > 0 and 'generated_text' in result[ 0 ] :
        return result[ 0 ][ 'generated_text' ]

    return None

def get_resp(example):
    answer = query(example)
    if answer :
        print(answer)
    else :
        print("No valid answer found in the response.")

#print(get_resp("who is joe biden"))