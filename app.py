from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    wishes = [
        "May the crescent moon brighten your path towards enlightenment.",
        "Wishing you a Ramadan full of peace, harmony, and joy.",
        "May your fasts be easy and your prayers be answered.",
        "Ramadan Kareem! May Allah bless you with prosperity.",
        "May this holy month bring you closer to your family and faith."
    ]
    # Randomly ek wish select hogi
    selected_wish = random.choice(wishes)
    return render_template('index.html', wish=selected_wish)

if __name__ == '__main__':
    app.run(debug=True)
