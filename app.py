from flask import render_template
from flask import Flask
import os


app = Flask(__name__)

@app.route("/")
@app.route("/about")
def home():
    return render_template('about.html')

@app.route("/skills")
def skills():
    return render_template('skills.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')
    
@app.route("/bio")
def bio():
    return render_template('bio.html')
    
@app.route("/projects")
def projects():
    return render_template('projects.html')
    
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))