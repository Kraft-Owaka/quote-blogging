from flask import Flaskrender_template

app = Flask(__name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/')
def post():
    return render_template('post.html')

@main.route('/')
def contact():
    return render_template('contact.html')


@main.route('/')
def about():
    return render_template('about.html')


@main.route('/')
def contact():
    return render_template('contact.html')



    if __name__ = '__main__:'
        app.run(debug=True)
    
    
