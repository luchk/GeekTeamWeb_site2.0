import os
from flask import Flask, render_template, request


app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    final_text = request.form["letter"]
    return render_template("index.html", final_text=final_text)


@app.route('/upload', methods=['POST'])
def upload_file():
#    file = request.files['image']
 #   f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
  #  file.save(f)
    return render_template("index.html", final_text = "hjkkkkkkk")


if __name__ == "__main__":
    app.run(debug=True)