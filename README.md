<h1 align=center>PyGallery</h1>

A simple flask app to display all images and gifs present in a folder. The page uses flexbox so that it looks pretty in all devices but CSS can be disabled by changing a  variable in the [app.py](app.py) file.



<p align="center">
<img src="./static/pics/pygallery.png" alt="PyGallery" width="500px" >
</p>
<hr>



## Installation
[Python >=3.5][1] interpreter and [Flask>=1.1.1][2] are required.

## Usage

Copy the files you want to display in the [./static/pics](static/pics/) folder and run the flask app. Check http://localhost:5000 for the page.
### Extras:
  
To disable CSS, go to the app.py file and change the content of the variable named "css" to False



[1]: https://www.python.org/downloads/
[2]: https://pypi.org/project/Flask/