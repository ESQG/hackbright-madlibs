from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return """<!doctype html><html>Hi! This is the home page.
    <a href="/hello">Continue</a></html>"""
  


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player)

@app.route('/game')
def show_madlib_form():
    play = request.args.get('play')
    if play == 'yes':
        return render_template('game.html')
    else:
        return render_template('goodbye.html')


@app.route('/madlib')
def show_madlib():
    person = request.args.get('person', 'Anonymous')
    color = request.args.get('color', 'purple')
    noun = request.args.get('noun', 'kitty')
    adj = request.args.get('adj', 'fluffy')

    return render_template('madlib.html',
                           person=person,
                           color=color,
                           noun=noun,
                           adj=adj)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
