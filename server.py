"""
This module implements a simple Flask-based web application for emotion detection.

It provides the following endpoints:
- `/emotionDetector`: Accepts text input, analyzes emotions, and returns the results.
- `/`: Renders the main HTML page.
"""

#Import the relevant libraries and functions
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the Flask app by the name
app = Flask("Emotion Detection")

#Define the function
@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the sentiment of the given text.

    This function receives a text input via a request argument, processes it 
    using the emotion_detector function, and returns a response with detected 
    emotions and the dominant emotion.

    Returns:
        str: A formatted string with emotions and the dominant emotion, or an 
        error message if the input is invalid.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions and dominant emotion from the response
    dominant_emotion = response['dominant_emotion']
    emotions = ', '.join([f"'{key}': {value}" \
            for key, value in response.items() if key != 'dominant_emotion'])

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    # Return a formatted string with the emotions and dominant emotion
    return f"For the given statement, the system response is {emotions}. \
                The dominant emotion is {dominant_emotion}."

#Render the HTML template using
@app.route("/")
def render_index_page():
    """
    Render the index HTML page.

    This function handles requests to the root URL ("/") and renders the 
    'index.html' template.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('index.html')

#Run the application on
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
