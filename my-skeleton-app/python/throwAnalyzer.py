from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import cv2
import PoseModule as pm
import tempfile
import os

app = Flask(__name__)
CORS(app)

@app.route("/test", methods=["GET"])
def test_route():
    response = jsonify("My Message")
    return response



@app.route('/process-video', methods=['POST'])
def process_video():

    # return jsonify("Response")

    # Check if the 'video' file is present in the request
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400

    video_file = request.files['video']
    height = request.form["height"]
    print("HEIGHT", height)

    # Save the uploaded video file to a temporary location
    temp_dir = tempfile.gettempdir()
    temp_video_path = os.path.join(temp_dir, 'temp_video.mp4')
    video_file.save(temp_video_path)

    # Open the saved video file using OpenCV
    cap = cv2.VideoCapture(temp_video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    detector = pm.PoseDetector(subjectHeight=int(height)) #no argument assumes 180cm

    data_list = []

    frame_counter = 0

    while True:
        success, img = cap.read()

        if not success:
            break  # Exit the loop when the video is over

        img = detector.findPose(img)
        lm_list = detector.getPosition(img)

        if len(lm_list) != 0:
            data = detector.detectFootballThrow(img)

            if data is not None:
                data_list.append({'frame': frame_counter, 'data': data})

        frame_counter += 1

        # Release the video capture object
    cap.release()

    # Remove the temporary video file
    os.remove(temp_video_path)

    response = jsonify(data_list)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
    return response



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
