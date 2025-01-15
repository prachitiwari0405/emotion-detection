import sys
sys.path.append('/home/project/final_project/oaqjp-final-project-emb-ai')  # Adjust the path if needed
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import EmotionPredict
# Initialize Flask app
app = Flask(__name__)
# Initialize the emotion predictor (use the appropriate initialization method from the AI library)
emotion_predictor = EmotionPredict()
@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    input_text = request.form['text']
        # Get the emotion prediction result (dominant emotion)
    dominant_emotion = emotion_predictor.predict_emotion(input_text)
    # If no emotion is detected, return an error response
    if not dominant_emotion:
        return jsonify({"error": "Emotion detection failed!"}), 400
    
    # Prepare the response to be returned
    response_data = {
        "dominant_emotion": dominant_emotion
    }
    
    return jsonify(response_data)
@app.route('/')
def home():
    return render_template('index.html')  # Renders the index page for the front-end

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
