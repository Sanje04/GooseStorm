#Framework for python web
import flask
import modules
from flask import request
from flask import render_template


#The Flask app
app = flask.Flask(__name__)
#app.config["DEBUG"] = True

#Define the routes
@app.route('/', methods=['GET'])
def home():
    return modules.home()

@app.route('/weather/<city>', methods=['GET'])
def cityweather(city):
    return modules.todays_weather(city)

@app.route('/index1', methods=['GET'])
def index1():
    author = {
        'name':'Sanje Divakaran',
        'email':'sanje.divakaran@gmail.com'
    }
    return '''
    <html>
    <head>
        <title>My Weather App</title>
    </head>
    <body>
        <h1>Welcome to my weather app</h1>
        <hr/>
        <p>
        Display the current weathers for all the cities across the globe! <br />
        Developed by: ''' + author['name'] + '''
        </p>
    </body>
    </html>

    '''

@app.route('/index', methods=['GET'])
def index():
    author = {
        'name':'Sanje Divakaran',
        'email':'sanje.divakaran@gmail.com'
    }

    return render_template('index.html', title='Goose Storm', author = author)

@app.route('/weather/<city>/v2', methods=['GET'])
def cityweatherv2(city):
    weather = modules.todays_weather(city)
    return render_template('cityweather.html', title='Goose Storm', weather = weather)

@app.route('/weather/<city>/raw', methods=['GET'])
def cityweatherraw(city):
    weather = modules.todays_weather_raw(city)
    return weather


app.run()


##dt_txt
#main.temp
#main.feels_like
#main.temp_min
#main.temp_max
#main.humidity
#weather.decription
#weather.icon