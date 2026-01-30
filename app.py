from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/room')
def room():
    return render_template('room.html')

@app.route('/amenities')
def amenities():
    return render_template('amenities.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)