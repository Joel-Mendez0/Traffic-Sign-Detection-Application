from flask import Flask, render_template, Response, session, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
import os
import cv2
from yolo_video import video_detection
import time
import config


app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/files'




class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Run")




def generate_frames(path_x=''):
    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        ref, buffer = cv2.imencode('.jpg', detection_)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




def generate_frames_web(path_x):
    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        ref, buffer = cv2.imencode('.jpg', detection_)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    session.clear()
    return render_template('indexproject.html')




@app.route("/webcam", methods=['GET', 'POST'])
def webcam():
    session.clear()
    return render_template('ui.html')




# Global variable to store the text
stored_text = ""


@app.route('/get_text')
def get_text():
    global stored_text
        
    if config.Stop:
        stored_text += "Stop Sign Detected\n"
        config.Stop = False
        
    if config.SpeedLimit:
        stored_text += "Speed Limit Detected\n"
        config.SpeedLimit = False

    return jsonify(text=stored_text)






@app.route('/FrontPage', methods=['GET', 'POST'])
def front():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename)))
        session['video_path'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                                             secure_filename(file.filename))
    return render_template('videoprojectnew.html', form=form)




@app.route('/video')
def video():
    return Response(generate_frames(path_x=session.get('video_path', None)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


global camera_source
camera_source = 0
@app.route('/webapp')
def webapp():
    return Response(generate_frames_web(path_x=camera_source), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/about", methods=['GET', 'POST'])
def about():
    session.clear()
    return render_template('about.html')
@app.route("/sources", methods=['GET', 'POST'])
def sources():
    session.clear()
    return render_template('sources.html')
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    session.clear()
    return render_template('contact.html')
@app.route("/settings", methods=['GET', 'POST'])
def settings():
    session.clear()
    return render_template('settings.html')
if __name__ == "__main__":
    app.run(debug=True)
