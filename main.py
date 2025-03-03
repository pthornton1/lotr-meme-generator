from flask import Flask, render_template
import requests
import random


API_KEY = ''
LOTR_API_ENDPOINT = 'https://the-one-api.dev/v2/quote?limit=100'
# Documentation for API: https://the-one-api.dev/documentation 

app = Flask(__name__)

@app.route('/')
def index():
    quote = ''
    header = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.get(url=LOTR_API_ENDPOINT, headers=header)
    
    quotes = response.json()['docs']
    
    quote = random.choice(quotes)['dialog']
    
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
    
    
# To do:
# Fetch Random Quote
# Fetch Image
# Mash together
# Edit buttons and navbar