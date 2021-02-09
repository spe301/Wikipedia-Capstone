import numpy as np
from flask import Flask, request, jsonify, render_template
from tensorflow.keras import preprocessing, models
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def ModelReadyString(text_str, pad):
    '''converts an individual unit of text into tokenized sequences'''
    text = [text_str]
    t = preprocessing.text.Tokenizer()
    t.fit_on_texts(text)
    tokens = t.texts_to_sequences(text)
    tokens2 = preprocessing.sequence.pad_sequences(tokens, maxlen=pad)
    return tokens2

def GetText(url):
   '''Scrapes a wikikedia article'''
   source = urlopen(url).read()
   soup = BeautifulSoup(source, 'lxml')
   text = soup.findAll('p')
   article = ''
   for i in range(len(text)):
       segment = text[i].text
       article += segment.replace('\n', '').replace('\'', '').replace(')', '')
       article = article.lower()
       clean = re.sub("([\(\[]).*?([\)\]])", '', article)
       clean2 = re.sub(r'\[(^)*\]', '', clean)
   return clean

app = Flask(__name__)
model = models.load_model('model2.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form['Text']
    if len(user_input) < 56:
        text = GetText(user_input) 
        tokenized = ModelReadyString(text, 1720)
    else:
        tokenized = ModelReadyString(user_input, 1720)
    prediction = model.predict(tokenized)
    output = round(prediction[0][1]*100, 2)
    return render_template('index.html', prediction_text='We predict a {}% probability that an AI wrote this.'.format(output))

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
