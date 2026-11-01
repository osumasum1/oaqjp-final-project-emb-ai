import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyze } }
    
    response = json.loads(requests.post(url, json=body, headers=headers).text)

    return {
    "anger": response["emotionPredictions"][0]["emotion"]["anger"],
    "disgust": response["emotionPredictions"][0]["emotion"]["disgust"],
    "fear": response["emotionPredictions"][0]["emotion"]["fear"],
    "joy": response["emotionPredictions"][0]["emotion"]["joy"],
    "sadness": response["emotionPredictions"][0]["emotion"]["sadness"],
    "dominant_emotion": max(response["emotionPredictions"][0]["emotion"], key=response["emotionPredictions"][0]["emotion"].get)
}