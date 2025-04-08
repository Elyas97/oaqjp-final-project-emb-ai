"""
This module handles the emotion detection API in a Flask application.
It interacts with an external API to analyze emotions from text input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function handles the /emotionDetector endpoint.
    It retrieves the text to analyze from the request, passes it to 
    the emotion_detector function, and returns the emotion analysis.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Get emotions from the emotion detector
    emotions = emotion_detector(text_to_analyze)

    # Extract the dominant emotion
    dominant_emotion = emotions['dominant_emotion']

    # If the dominant emotion is None, return an error message
    if dominant_emotion is None:
        return "Invalid Input! Try again."

    # Return the detailed emotion analysis as a string
    return (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} "
        f"and 'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    This function renders the index page.
    It handles requests to the root URL and returns the index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
