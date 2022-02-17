from flask import Flask, request, render_template
from jinja2 import Template
import requests

from pprint import pprint
app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    name = request.args.get('name')
    return render_template('macvendorlookup.html')

@app.route("/macresults", methods=['GET', 'POST'])
def macfind():
    try:
        macaddress = request.form.get('mac')
        req = requests.get('https://api.macvendors.com/'+ macaddress)
        resout = req.text
    except ValueError:
            print('Wrong MAC')
            
    return render_template(
    'macvendorlookup.html'
    ,response = resout
    )

if __name__ == '__main__':
    app.run()
