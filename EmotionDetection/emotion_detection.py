import requests  # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    print(str(response.status_code) + ", this is the code")
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        highest_score = 0
        dominant_emotion = ""

        for emotion, score in emotions.items():
            if score > highest_score:
                highest_score = score
                dominant_emotion = emotion
        
        result = emotions.copy()
        result["dominant_emotion"] = dominant_emotion
        return result
    elif response.status_code == 400:
        # If the status code is 400, return the result with None values
        result = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
            }
        return result 