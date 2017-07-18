"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
              <html>
                <body>
                  <h1>Hi! This is the home page.</h1><br/>
                  <a href='/feelings'>Compliment/Insult generator</a>
                </body>
              </html>"""


@app.route('/feelings')
def check_feeling():
  """Checks if people are feeling loving or sassy"""

  return """<!doctype html>
              <html>
                <body>
                  <h1>How are you feeling? Loving or Sassy?</h1><br/>
                  <a href='/love-level'>I'm feeling loving!</a><br/>
                  <form action="/loving">
                    Lukewarm<input type="radio" name:"love-level" value="lukewarm">
                  <a href='/burn-level'>I'm feeling sassy!</a>
                </body>
              </html>"""




@app.route('/loving')
def say_hello():
    """Lets user pick loving compliment"""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <select name="compliment">
            <option value="awesome">awesome</option>
            <option value="terrific">terrific</option>
            <option value="fantastic">fantastic</option>
            <option value="neato">neato</option>
            <option value="fantabulous">fantabulous</option>
            <option value="wowza">wowza</option>
            <option value="oh-so-not-meh">oh-so-not-meh</option>
            <option value="brilliant">brilliant</option>
            <option value="ducky">ducky</option>
            <option value="coolio">coolio</option>
            <option value="incredible">incredible</option>
            <option value="wonderful">wonderful</option>
            <option value="smashing">smashing</option>
            <option value="lovely">lovely</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/sassy')
def say_hello():
    """Lets user pick loving compliment"""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <select name="compliment">
            <option value="awesome">awesome</option>
            <option value="terrific">terrific</option>
            <option value="fantastic">fantastic</option>
            <option value="neato">neato</option>
            <option value="fantabulous">fantabulous</option>
            <option value="wowza">wowza</option>
            <option value="oh-so-not-meh">oh-so-not-meh</option>
            <option value="brilliant">brilliant</option>
            <option value="ducky">ducky</option>
            <option value="coolio">coolio</option>
            <option value="incredible">incredible</option>
            <option value="wonderful">wonderful</option>
            <option value="smashing">smashing</option>
            <option value="lovely">lovely</option>
          </select>
          <input type="submit" value="Submit">
        </form>
        <br/>
        <br/>
        <!--Diss them instead-->
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <select name="diss">
            <option value="an asshole">an asshole</option>
            <option value="terrible">terrible</option>
            <option value="bitchy">bitchy</option>
            <option value="neurotic">neurotic</option>
            <option value="worse than Trump">worse than Trump</option>
            <option value="gross">gross</option>
            <option value="oh-so-meh">oh-so-meh</option>
            <option value="worthless">worthless</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def diss_person():
    """Get user by name and ridicule them!"""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """.format(player=player, diss=diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
