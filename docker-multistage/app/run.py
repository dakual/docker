from flask import Flask, render_template, request
from info import Info, os

app = Flask(__name__)

UPLOAD_DIR = os.getenv('UPLOAD_FOLDER')

@app.route('/')
def index():
    return render_template('index.html', data=Info())

@app.route('/api')
def api():
    return Info().get()

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = file.filename
        file.save(os.path.join(UPLOAD_DIR, filename))
        
    return """
    <!doctype html>
    <title>upload new File</title>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file><input type=submit value=Upload>
    </form>
    """
    
if __name__ == '__main__':
    app.run(debug=True)