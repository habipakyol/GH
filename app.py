from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', video_file='video/turk.mp4')

if __name__ == '__main__':
    app.run(debug=True)