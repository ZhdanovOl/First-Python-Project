"""
This module contains a function for detecting emotions in a given text using an external API.
"""

import json
import requests

def emotion_detector(text_to_analyse):
    """
    Detect emotions in the given text using the Watson Emotion API.

    Args:
        text_to_analyse (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing the scores for different emotions 
              (anger, disgust, fear, joy, sadness) and the dominant emotion. 
              If the response fails, returns a dictionary with None values.
    """
    # Define the URL for the emotion detector API
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1'
        '/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    )

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header, timeout=(5, 10))

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the emotions and dominant emotion
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

    # If the response status code is 400, return a dictionary with None values
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Handle unexpected status codes
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
            'dominant_emotion': 'unknown'
    }
