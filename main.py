from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0,9)

@app.route('/')
def home_screen():
    return "<h2 style='color:black'>Think of a number between 0 and 9</h2>" \
           "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"

@app.route('/<int:number>')
def determine_guess(number):
    if number < random_number:
        return "<h2 style='color:black'>Too low! Guess higher</h2>" \
               "<img src=https://media.giphy.com/media/DjYqNVITTewEM/giphy.gif>"
    elif number > random_number:
        return "<h2 style='color:red'>Too high! Guess lower!</h2>" \
               "<img src=https://media.giphy.com/media/iNGGTlWczOpiw/giphy.gif>"
    else:
        return "<h2 style='color:blue'>Well done!</h2>" \
               "<img src=https://media.giphy.com/media/RJzv5gG13bFsER317k/giphy.gif>"










if __name__ == "__main__":
    app.run(debug=True)