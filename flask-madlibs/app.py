from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story
from stories import excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template("questions.html", prompts=silly_story.prompts)

@app.route('/results')
def results():

    story = silly_story.generate(request.args)
    
    
    return render_template("story.html", story=story)


@app.route('/<story_type>')
def chosen_story(story_type):
    return render_template('questions.html', prompts=story_type.prompts)