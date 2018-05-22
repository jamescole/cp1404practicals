from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)

@app.route('/f/<temperature>')
def convert_temperature(temperature=""):
    if temperature == "":
        return "Error: include temperature in URL"
    else:
        string = "<p>Input temperature in Celsius: {}</p>".format(temperature)
        string += "\n<p>Converted to Fahrenheit: {}</p>".format(get_fahrenheit_from_celsius(float(temperature)))
        return string


def get_fahrenheit_from_celsius(celsius):
    return celsius * 9.0 / 5 + 32

if __name__ == '__main__':
    app.run()
