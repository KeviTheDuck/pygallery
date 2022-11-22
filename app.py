from flask import Flask, render_template
import shutil
import os
import sys


app = Flask(__name__)

dir_arg = sys.argv[1]
# path of the src folder passed as an argument
if os.path.isabs(dir_arg):
    src_dir = dir_arg + '/'
else:
    src_dir = os.path.dirname(dir_arg) + '/'
print(src_dir)
# path to destination directory

dest_dir = 'static/pics/'

# copying all the files in the source directory
files = os.listdir(src_dir)
for file_name in files:
    shutil.copy(src_dir+file_name, dest_dir+file_name)
print("copied all files")

if len(sys.argv)  >= 3:
    port_number = int(sys.argv[2])
else:
    port_number = 5000

@app.route("/")
def gallery():
    image_names = os.listdir('static/pics')
    return render_template("gallery.html", image_names=image_names)

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=port_number)
    finally:
        shutil.rmtree('static/pics/', ignore_errors=True, onerror=None)
        os.makedirs('static/pics/')