from flask import Flask, render_template, send_from_directory
import os


app = Flask(__name__)

css = True

@app.route("/")
def gallery():
    image_names = os.listdir("static/pics")
    return render_template("gallery.html",image_names=image_names,css=css)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)