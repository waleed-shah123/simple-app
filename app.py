from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def random_color():
    colors = ["Red","Orange","Yellow","Green","Blue","Purple","Pink","Brown","Gray","Black"]
    color = random.choice(colors)
    return render_template('color.html', color=color)

if __name__ == '__main__':
    app.run(debug=True)

